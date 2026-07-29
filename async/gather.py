import asyncio
import time

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)
    return f"done: {message}"

async def risk(n: int) -> int:
    if n % 2 == 0:
        return n
    else:
        raise ValueError('risk')

async def main():
    print(f"started at {time.strftime('%X')}")

    results = await asyncio.gather(
        risk(2),
        risk(6),
        risk(7),
        risk(6),
        risk(8),
        return_exceptions=True
    )

    print(results)
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())