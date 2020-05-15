#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

ack_list = []
extension =".png"


def process_packet(packet):
    scapy_packet= scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            if extension in scapy_packet[scapy.Raw].load:
                print("[+] donwload pdf file Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            if extension in scapy_packet[scapy.Raw].load:
                if scapy_packet[scapy.TCP].seq in ack_list:
                    print("[+] response downlad file pdf type")
                    print(scapy_packet.show())
    packet.accept()




queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

