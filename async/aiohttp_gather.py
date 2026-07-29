import asyncio
import aiohttp
import time

start_time = time.time()

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            fetch(session, 'https://jsonplaceholder.typicode.com/posts/1'),
            fetch(session, 'https://jsonplaceholder.typicode.com/posts/2'),
            fetch(session, 'https://jsonplaceholder.typicode.com/posts/3'),
        )
    return results

print(asyncio.run(main()))
program_time = time.time() - start_time
print(f'время выполнения {program_time:.2f}')