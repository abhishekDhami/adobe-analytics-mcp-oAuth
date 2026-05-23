import asyncio
import os

import httpx
from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

load_dotenv()

MCP_URL = "https://aa-mcp.adobe.io/mcp"

HEADERS = {
    "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}",
    "x-api-key": os.getenv("CLIENT_ID"),
    "x-gw-ims-org-id": os.getenv("ORG_ID"),
    "Content-Type": "application/json"
}


async def main():

    async with httpx.AsyncClient(
        headers=HEADERS,
        timeout=30.0
    ) as http_client:

        async with streamable_http_client(
            url=MCP_URL,
            http_client=http_client
        ) as (
            read_stream,
            write_stream,
            _
        ):

            async with ClientSession(
                read_stream,
                write_stream
            ) as session:

                print("\nConnecting to Adobe Analytics MCP...\n")

                await session.initialize()

                print("Connected successfully.\n")

                tools = await session.list_tools()

                print("Available MCP Tools:\n")

                for tool in tools.tools:
                    print(f"- {tool.name}")


if __name__ == "__main__":
    asyncio.run(main())