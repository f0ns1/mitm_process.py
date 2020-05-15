## MitM attack manage packages

    Allow /Reject traffic package on:
        
            FORWARDING --ip_forwarding redirect
            INBOUND --INPUT packages
            OUTBOUND --OUTPUT packages

    For all traffic and all protocols...Maybe, future virtual fw/ proxy using iptables and NFQUEUES andverify package contents

# Run attack 

    root@kali:~/PycharmProjects/mitm_process.py# python mitm.process.py -q 0 -o Allow
    [*] Start program ....MitM 
    [*] Traffic type = Allow
    Enable Iptables queue for input target packets ... on queue number 0
    
    UDP packet, 60 bytes
    UDP packet, 60 bytes
    UDP packet, 60 bytes
    UDP packet, 76 bytes
    TCP packet, 60 bytes
    TCP packet, 44 bytes
    TCP packet, 40 bytes
    TCP packet, 518 bytes
    TCP packet, 1464 bytes
    TCP packet, 40 bytes
    TCP packet, 1500 bytes
    TCP packet, 40 bytes
    TCP packet, 554 bytes
    TCP packet, 40 bytes
    TCP packet, 114 bytes
    TCP packet, 425 bytes
    TCP packet, 40 bytes
    TCP packet, 119 bytes
    TCP packet, 40 bytes
    TCP packet, 119 bytes
    TCP packet, 40 bytes
    TCP packet, 1216 bytes
    TCP packet, 40 bytes
    TCP packet, 80 bytes
    TCP packet, 80 bytes
    TCP packet, 40 bytes
    TCP packet, 40 bytes
    TCP packet, 40 bytes
    TCP packet, 64 bytes
    TCP packet, 40 bytes
    ^C[*] CRTL +C Detecting ... Flush queue for Iptables on local machine 
    [*] End program 