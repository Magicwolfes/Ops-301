# What is a Virtual Private Cloud VCP
A virtual private cloud (VPC) is a secure, isolated private cloud hosted within a public cloud

## How can one host within a VPC any services that need to be public?

## What are examples of services that would live in the publicly-accessible part of the VPC? The privately-accessible part?

### Public
- Web servers
- Load balancer
- Bastion hosts
### Private
- Database
- App Servers
- Caching servers

## What are the trade-offs of using a VPC vs traditional infrastructure?
Security risks: VPCs are subject to the same security risks as any other cloud-based infrastructure, and may require additional security measures to ensure data and network security
Complexity: VPCs can be more complex to set up and manage than traditional infrastructure, as they require knowledge of cloud-specific networking and security concepts.

### Notes
A private cloud is a cloud service that is exclusively offered to one organization. A virtual private cloud (VPC) is a private cloud within a public cloud; no one else shares the VPC with the VPC customer.

The key technologies for isolating a VPC from the rest of the public cloud are:
- Subnets
- VLAN
- VPN

Some VPC providers offer additional customization withNetwork Address - Translation (NAT): This feature matches private IP addresses to a public IP address for connections with the public Internet. With NAT, a public-facing website or application could run in a VPC.
- BGP route configuration: Some providers allow customers to customize BGP routing tables for connecting their VPC with their other infrastructure.

# Advantages
- Scalability
- Easy hybrid cloud deployment
- better performance
- better sevurity

Cloudfare
Cloudflare makes it easy to use any cloud service by providing a single plane of control for performance, security, and reliability services, including bot management, DNS, SSL, and DDoS protection
