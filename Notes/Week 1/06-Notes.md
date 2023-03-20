# Network Address Translation (Nat)
https://www.geeksforgeeks.org/network-address-translation-nat/


## What is the main purpose for implementing NAT on a network?
The idea of NAT is to allow multiple devices to access the Internet through a single public address. To achieve this, the translation of a private IP address to a public IP address is required. he idea of NAT is to allow multiple devices to access the Internet through a single public address. To achieve this, the translation of a private IP address to a public IP address is required.


## At what layer of the OSI model does NAT happen?
Layer 4, because it is modifying the IP header.


## What happens to packets when NAT runs out of addresses in the pool of available IPs?
Port Address Translation (PAT) – This is also known as NAT overload. In this, many local (private) IP addresses can be translated to a single registered IP address. Port numbers are used to distinguish the traffic i.e., which traffic belongs to which IP address. This is most frequently used as it is cost-effective as thousands of users can be connected to the Internet by using only one real global (public) IP address. 


## What disadvantage does using NAT pose for routers?
Disadvantage of NAT – 

Translation results in switching path delays. 
 
Certain applications will not function while NAT is enabled. 
 
Complicates tunneling protocols such as IPsec. 
 
Also, the router being a network layer device, should not tamper with port numbers(transport layer) but it has to do so because of NAT. 