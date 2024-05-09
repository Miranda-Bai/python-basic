import socket
from scapy.all import *
from scapy.layers.l2 import Ether

# catch all the network traffics

# Linux-like OS only
# socket.AF_PACKET only works on Linux-like OS
# sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

# interface = "eth0"
# sniffer_socket.bind((interface, 0))

# try:
#     while True:
#         raw_data, addr = sniffer_socket.recvfrom(65535)
#         packet = Ether(raw_data)
#         print(packet.summary())

# except KeyboardInterrupt:
#     sniffer_socket.close()

# =========================

# Windows (not work properly)
# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packets
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a packet
print(s.recvfrom(65565))

# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)