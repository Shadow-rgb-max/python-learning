import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()  # или .json(), если ответ в JSON

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "https://example.com")
        print(html[:200])

asyncio.run(main())