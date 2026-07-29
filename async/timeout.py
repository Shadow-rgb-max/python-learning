import asyncio

async def slow_task():
    await asyncio.sleep(5)
    return 'готово'

async def main():
    await asyncio.wait_for(slow_task(), 2)

try:
    asyncio.run(main())
except TimeoutError:
    print('timeout')