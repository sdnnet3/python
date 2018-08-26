import socket
import asyncio

loop = asyncio.get_event_loop()

async def send_my_msg(address, message):
    sock = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
        )
    sock.setblocking(False)
    await loop.sock_connect(sock, address)

    #call something like a sender function loop, socket, sender
    #tries to send data,
    await sock.sendall(sock, message)
