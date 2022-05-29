import asyncio


async def add_42(number):
    print("Adding 42")
    return 42 + number


async def hello_world():
    print("hello world!")
    # 코루틴 안에서 다른 코루틴 호출 가능
    result = await add_42(23)
    return result

event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(hello_world())
    print(result)
finally:
    event_loop.close()
