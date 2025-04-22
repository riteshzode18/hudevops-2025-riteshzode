HashedIn University Linux Advance Assignment 

1. DNS


A. When you perform an nslookup for a domain name, the DNS resolution process involves 
multiple stages, starting from the root DNS servers down to the authoritative name servers. 
Using appropriate tools or commands, how can you trace the full DNS resolution path and 
identify all the intermediate DNS servers (like root, TLD, and authoritative servers) involved in 
resolving a domain name (Hashedin.com, Deloitte.com, dna.hashedin.com)? Please explain the 
steps and provide the command(s) used along with the output interpretation.

answer:

```
dig +trace hashedin.com
```
Explain:

use dig +trace domain.com to trace DNS resolution step by step to root, TLD and authoritative servers

![alt text](image.png)


 
B. On a Linux system perform the below tasks:


i) Add a custom entry in a file in linux file system where it should point to loopback address when 
you enter “mypc.test”. 


commands:
```
sudo nano /etc/hosts
sudo cat /etc/hosts
```
![alt text](image-1.png)

explain:
point mypc.tst to localhost (127.0.0.1)
127.0.0.1   mypc.test


ii) Verify that the domain “mypc.test” resolves to your loopback address using necessary linux

commands:

```
ping mypc.test
```

![alt text](image-2.png)


iii) Temporarily comment out the entry in the file and the test the resolution again. What do you 
observe?

commands:

```
nano /etc/hosts -- comments the entry
ping mypc.test

```

![alt text](image-3.png)



C. Update your nameserver resolver to a dummy IP(such as 8.8.8.1) and try accessing the 
hashedin.com domain.
commands:
```
ping hashedin.com
sudo cp /etc/resolv.conf /etc/resolv.conf.bk  -- to save backup
sudo nano /etc/resolv.conf -- replace nameserver with dummy ip (8.8.8.1)
ping hashedin.com -- this will give errror
sudo cp /etc/resolv.conf.bk /etc/resolv.conf  -- copy original nameservers from backup
ping hashedin.com -- it will work
```


![alt text](image-4.png)


2. Network Analysis

How can I capture and analyze HTTP traffic generated on a locally hosted server(running on port 
8080) under synthetic load to understand request patterns, response behavior, and overall 
network activity?

i) What methods can be used to capture only HTTP traffic on a specific port for detailed 
inspection of requests and responses?

```
sudo tcpdump -i any tcp port 8080 -w capture.pcap
```

ii) How can one isolate and interpret different HTTP methods and status codes from a larger 
volume of captured traffic? 
iiI) What techniques allow extraction of specific HTTP header fields, such as Host, User_agent, or 
the request URL. 
iv) How can the captured network traffic be summarized to highlight patterns in HTTP requestresponse interactions, especially under heavy load? 
v) List the TCP handshake and session initiation for the HTTP traffic on port 8080? 
 
3. Simulate two isolated network namespaces be created on a single host, such that each 
environment runs a separate process and both are connected via a common virtual bridge, 
allowing them to communicate with each other (e.g., ping each other)? 

```
Explain:
1. create 2 network namespace
2. create a virtual bridge
3. connect both namespace to bridge
4. assign ips and bring up interface
5. check communication 
6. delete all network and bridge
```
![alt text](image-6.png)
 
4. Spin up two Ubuntu VMs in Vmware – VM1 and VM2.
4.1 Configure a custom route in VM1 to forward traffic to 9.9.9.9 to be forwarded to 
VM2 and verify using tcpdump. Make sure that ping to 9.9.9.9 receives reply by 
configuring VM2 to forward the packets.
4.2 Get the ARP cache of both the VMs. Delete the current IP address. Pick a /24 network 
from the private IP range 172.16.0.0/16 and assign a static IP address manually to both 
the VMs. Ensure that the VMs can ping each other. Now delete the IP addresses and use 
DHCP to automatically assign IP addresses to the interfaces.
Configure a custom route in VM1 to forward traffic to 9.9.9.9 to be forwarded to VM2 and verify 
using tcpdump. Make sure that ping to 9.9.9.9 receives reply by configuring VM2 to forward the 
packets.
 
5. Build and validate a PKI setup using your Own CA. The PKI should be used to secure an NGINX 
server and perform certification verification.
