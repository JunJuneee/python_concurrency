import aiohttp
import asyncio


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


loop = asyncio.get_event_loop()
# 코루틴 비동기로 생성
coroutines = [get("http://example.com") for _ in range(8)]

results = loop.run_until_complete(asyncio.gather(*coroutines))

print("Results: %s" % results)
