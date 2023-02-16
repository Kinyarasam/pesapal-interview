#!/usr/bin/env python3
"""TCP server that accepts and holds a maximum of N clients
"""
import socket
import asyncio


# Standard loopback interface address (localhost)
HOST = socket.gethostbyname(socket.gethostname())
# port to listen on (non-priveleged ports are > 1023)
PORT = 5040
BUFF_SIZE = 1024


async def handle_client(
        reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
    """
    ###

    Args:
        reader (asyncio.StreamReader): ###
        writer (asyncio.StreamWriter): ###

    Returns:
        None.
    """
    data = None

    while data != 'quit':
        data = await reader.read(BUFF_SIZE)
        message = data.decode()
        addr, port = writer.get_extra_info("peername")
        print(f'Received the message from: {addr} {port} {message!r}')

        writer.write(data)
        await writer.drain()

    writer.close()
    await writer.wait_closed()


async def run_server() -> None:
    """

    Returns:
        Nothing.
    """
    server = await asyncio.start_server(handle_client, HOST, PORT)

    async with server:
        print("Listening . . .")
        await server.serve_forever()

        # tasks = []

        # for client in range(10):
            # try:
                # asyncio.create_task(handle_client(*asyncio.open_connection(sock=client)))
                # await asyncio.gather(*tasks)
            # except Exception as e:
                # print("[{}] {}".format(e.__class__.__name__, e))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_server())
