"""
AI-COMPANY
dashboard/backend/websocket.py

WebSocket Server
"""

from fastapi import WebSocket
from typing import List
import asyncio
from datetime import datetime


class ConnectionManager:

    def __init__(self):

        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):

        await websocket.accept()

        self.connections.append(websocket)

        print("[WEBSOCKET] Client Connected")

    def disconnect(self, websocket: WebSocket):

        if websocket in self.connections:

            self.connections.remove(websocket)

            print("[WEBSOCKET] Client Disconnected")

    async def send(self, websocket: WebSocket, message):

        await websocket.send_json(message)

    async def broadcast(self, message):

        disconnected = []

        for connection in self.connections:

            try:

                await connection.send_json(message)

            except Exception:

                disconnected.append(connection)

        for connection in disconnected:

            self.disconnect(connection)


manager = ConnectionManager()


async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:

        while True:

            message = {

                "system": "ONLINE",

                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

                "dashboard": {

                    "total_agents": 0,

                    "active_tasks": 0,

                    "completed_today": 0,

                    "system_health": "Healthy"

                }

            }

            await manager.send(

                websocket,

                message

            )

            await asyncio.sleep(2)

    except Exception:

        manager.disconnect(websocket)
