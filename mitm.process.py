#!/usr/bin/ebv python
import netfilterqueue
import subprocess
import optparse


def process_packet(packet):
    print(packet)
    packet.accept()

def deny_packet(packet):
    print(packet)
    packet.drop()

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-q", "--queue", dest="queue", help="Queue Number of Iptables for ingping traffic")
    parser.add_option("-o", "--option", dest="traffic", help="Allow/Drop packages")
    (options,arguments)=parser.parse_args()
    if not options.queue :
        parser.error("[-] Please specify a queue number for iptables  -q ")
    if not options.traffic:
        parser.error("[-] Please specify a trrafic operations option Allow[accept packets] or Deny[Drop packets] -o ")
    return options


print("[*] Start program ....MitM ")
options=get_arguments()
traffic= options.traffic
print("[*] Traffic type = "+traffic)
print("Enable Iptables queue for input target packets ... on queue number 0")
subprocess.check_output(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", options.queue])
queue = netfilterqueue.NetfilterQueue()
if traffic == "Allow":
    queue.bind(int(options.queue), process_packet)
else:
    queue.bind(int(options.queue), deny_packet)
try:
    queue.run()
except KeyboardInterrupt:
    print("[*] CRTL +C Detecting ... Flush queue for Iptables on local machine ")
    subprocess.check_output(["iptables", "--flush"])
    print("[*] End program ")