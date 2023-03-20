# Virtualbox Network Setting Guide
https://www.nakivo.com/blog/virtualbox-network-setting-guide/


## Which network mode in VirtualBox can be used to emulate unplugging the Ethernet cable from the network?
Not attached, when you install in a VM but the connection is missing. Useful for testing.

## Which network mode would be best if you wanted to run a server on a VM that could be fully accessible from your physical local area network?
Bridged Adapter, This mode is used for connecting the virtual network adapter of a VM to a physical network to which a physical network adapter of the VirtualBox host machine is connectedThis mode is used for connecting the virtual network adapter of a VM to a physical network to which a physical network adapter of the VirtualBox host machine is connected

## What are the three options of promiscuous mode and what does each do?
- Deny. Any traffic that is not intended to the virtual network adapter of the VM is hidden from the VM. This option is set by default.
- Allow VMs. All traffic is hidden from the VM network adapter except the traffic transmitted to and from other VMs.
- Allow All. There are no restrictions in this mode. A VM network adapter can see all incoming and outgoing traffic.

## What is Port Forwarding?
> Port forwarding is a process of intercepting traffic addressed to the appropriate IP address and port in addition to redirecting that traffic to a different IP address and/or port.

# Other notes
VirtualBox Network Modes
 - Not Attached: the network connection is missing, much like when you unplug the Ethernet network cable when using a physical network adapter

 - Nat: This network mode is enabled for a virtual network adapter by default. A guest operating system on a VM can access hosts in a physical local area network (LAN) by using a virtual NAT (Network Address Translation) device. 

 - NAT network: This mode is similar to the NAT mode that you use for configuring a router. If you use the NAT Network mode for multiple virtual machines, they can communicate with each other via the network.

 - Bridged Adpater: This mode is used for connecting the virtual network adapter of a VM to a physical network to which a physical network adapter of the VirtualBox host machine is connected.

 - Internal Network: Virtual machines whose adapters are configured to work in the VirtualBox Internal Network mode are connected to an isolated virtual network. VMs connected to this network can communicate with each other, but they cannot communicate with a VirtualBox host machine, or with any other hosts in a physical network or in external networks.

 - Host-only Adapter: This network mode is used for communicating between a host and guests. A VM can communicate with other VMs connected to the host-only network, and with the host machine.

 - Generic driver: This network mode allows you to share the generic network interface. A user can select the appropriate driver to be distributed in an extension pack or be included with VirtualBox.
 