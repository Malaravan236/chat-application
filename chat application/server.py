import asyncio
import websockets

# List to store connected clients
clients = []

async def chat_handler(websocket, path):
    # Register a new user
    clients.append(websocket)
    try:
        async for message in websocket:
            # Broadcast the message to other connected users
            for client in clients:
                if client != websocket:
                    await client.send(message)
    finally:
        # Unregister the user on disconnection
        clients.remove(websocket)

# Start WebSocket server
async def main():
    async with websockets.serve(chat_handler, "localhost", 8768):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

asyncio.run(main())
