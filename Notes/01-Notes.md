# Layers of OSI Model 
https://www.geeksforgeeks.org/layers-of-osi-model/

## What does “OSI” stand for?
Open Systems Interconnection. It is a 7 layer architecture with each layer having specific functionality to perform. All these 7 layers work collaboratively to transmit the data from one person to another across the globe. 

## List the 7 layers of the OSI model and what each one is responsible for.
 1 Physical layer - contains infomation in the form of bits. Responsible for transmitting individual bits for one node to the next.
    - Bit snychronization 
    - Bit rate control
    - Physical topologies
    - Transmission mode


 2 Data Link layer: The data link layer is responsible for the node-to-node delivery of the message. The main function of this layer is to make sure data transfer is error-free from one node to another, over the physical layer. 
    - Framing
    - Physical addressing
    - Error Control
    - Flow Control


 3 Networker Layer: The network layer works for the transmission of data from one host to the other located in different networks. It also takes care of packet routing i.e. selection of the shortest path to transmit the packet, from the number of routes available. 
    - Routing
    - Logical Addressing


 4 Transport layer: The transport layer provides services to the application layer and takes services from the network layer. The data in the transport layer is referred to as Segments. It is responsible for the End to End Delivery of the complete message. The transport layer also provides the acknowledgement of the successful data transmission and re-transmits the data if an error is found
    - Segmentation and Reassembly
    - Serive point addressing
Serives provided by the transport layer:
    - Connection-oriented Service
    - Connectionless service


 5 Session Layor: This layer is responsible for the establishment of connection, maintenance of sessions, authentication, and also ensures security. 
    - Session establishment, maintenance, and termination
    - Synchronization
    - Dialog Controller


 6 Presentation Layer: The presentation layer is also called the Translation layer. The data from the application layer is extracted here and manipulated as per the required format to transmit over the network. 
    - Translation
    - Encryption / Decryption
    - Compression


 7 Application Layer: At the very top of the OSI Reference Model stack of layers, we find the Application layer which is implemented by the network applications. These applications produce the data, which has to be transferred over the network. This layer also serves as a window for the application services to access the network and for displaying the received information to the user. 
    - network virtual terminal
    - FTAM-File transfer access and management
    - Mail Services
    - Directory Services
 


## Which layers are the “hardware layers”? What does that mean?
https://www.comptia.org/content/articles/what-is-wireshark-and-how-to-use-it


### Hardware layers
 - Network layer
 - Data Link layer
 - Physical layer


### Which layers are the “software layers”? What does that mean?
 - Application layer
 - Presentation layer
 - Session layer


# What is WireShark
## What is Wireshark?
Wireshark is a network protocol analyzer, or an application that captures packets from a network connection, such as from your computer to your home office or the internet


## What is a packet?
Packet is the name given to a discrete unit of data in a typical Ethernet network.


## What 3 high-level things does Wireshark accomplish?
- Packet Capture: Wireshark listens to a network connection in real time and then grabs entire streams of traffic – quite possibly tens of thousands of packets at a time.
- Filtering: Wireshark is capable of slicing and dicing all of this random live data using filters. By applying a filter, you can obtain just the information you need to see.
- Visualization: Wireshark, like any good packet sniffer, allows you to dive right into the very middle of a network packet. It also allows you to visualize entire conversations and network