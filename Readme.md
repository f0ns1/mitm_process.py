## MITM Manage packets 

That python program manage inbound traffic from target ip server to the router forwarding by mitm host.

For  make this task the application use OS command system Iptables and netfilterqueue of python.

Itables at the init of the program enable NFQUEUE on local inbound traffic and python library consume all packets 
like a virtual fw/proxy/balancer  or other... 
In that case the interceptor has option of modify the packet before accept or drop it.

# How to use

    root@kali:~/PycharmProjects/mitm_process.py# python mitm.process.py -h
    [*] Start program ....MitM 
    Usage: mitm.process.py [options]
    
    Options:
       -h, --help            show this help message and exit
       -q QUEUE, --queue=QUEUE
                        Queue Number of Iptables for ingping traffic
        -o TRAFFIC, --option=TRAFFIC
                        Allow/Drop packages

# Execution 

    root@kali:~/PycharmProjects/mitm_process.py# python mitm.process.py -q 0 -o Allow
    [*] Start program ....MitM 
    [*] Traffic type = Allow
    Enable Iptables queue for input target packets ... on queue number 0
    UDP packet, 74 bytes
    UDP packet, 181 bytes
    TCP packet, 52 bytes
    TCP packet, 44 bytes
    TCP packet, 40 bytes
    TCP packet, 255 bytes
    TCP packet, 1500 bytes
    TCP packet, 40 bytes
    TCP packet, 204 bytes
    TCP packet, 40 bytes
    ^C[*] CRTL +C Detecting ... Flush queue for Iptables on local machine 
    [*] End program 

# dependencies

    netfilterqueue
    subprocess
    optparse

 
