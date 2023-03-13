# What is a Port Scanner and how does it work?
https://www.varonis.com/blog/port-scanning-techniques

## What is a port?
A port scanner is a computer program that checks network ports for one of three possible statuses – open, closed, or filtered.
Port scanners are valuable tools in diagnosing network and connectivity issues. 
A port scanner sends a network request to connect to a specific TCP or UDP port on a computer and records the response.
A port is a virtual location where networking communication starts and ends (in a nutshell).

## What does a port scanner send to a port to check the current status?
Ping scanner. you are looking for any ICMP replies, which indicates that the target is alive


## When a port scanner sends a request to connect, what are the three possible responses? Describe them.
> Open, Accepted: The computer responds and asks if there is anything it can do for you.
> Closed, Not Listening: The computer responds that “This port is currently in use and unavailable at this time.”
> Filtered, Dropped, Blocked: The computer doesn’t even bother to respond.


## What is the difference between TCP and UDP?
TCP and UDP are the most common use for IP networks. TCP sends each pack in order, error check, verfiy, and 3-way handshake to comfirm success. However a UDP does not have an error check but is faster. Live streams and gaming often 
# Common Ports
https://www.professormesser.com/network-plus/n10-008/n10-008-video/common-ports-n10-008/

- Telnet
    Telecommunication network protocol, TCP port 23. Console access to that device, no encryption.

- SSH
    Secure Shell, TCP port 22. More secure protocol.

- DNS
    Domain Name System, TCP port 53. Convert the name you type in to a IP address.

- SMTP
    Simple Mail Transfer protocol, TCP port 25. Encrypted form of SMTP that uses TLS that uses TCP port 587. Emails (mobile)

- HTTP
    Hypertext transfer Protocol, TCP port 80

- HTTPS
    Hypertext transfer Protocol Secure, TCP port 443
    > This encrypted communication historically used SSL, or Secure Sockets Layer, although newer web servers will use a newer version of SSL called TLS, or Transport Layer Security.

- RDP
    Remote Desktop Protocol, TCP port 3389. remote access software.

- Ping
    Uses "echo request" message and provkes a "echo response" TCP port 7

TLS - Transport Layer Security
TCP - Transmission Control Protocol

I had to google the last three as I couldnt find them in the reading