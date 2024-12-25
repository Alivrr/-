import asyncio
import aiohttp

async def tunnel_to_host():
    url = "https://api.roamless.com"
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(url) as response:
                    print(f"Status: {response.status}")
                    print(f"Headers: {response.headers}")
                    content = await response.text()
                    print(f"Content: {content}")
            except Exception as e:
                print(f"An error occurred: {e}")
            await asyncio.sleep(0)  # 5 saniye bekleyip tekrar dene

if __name__ == "__main__":
    asyncio.run(tunnel_to_host())
