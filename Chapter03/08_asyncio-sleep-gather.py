import asyncio


async def hello_world():
    print("hello world!")


async def hello_python():
    print("hello Python!")
    await asyncio.sleep(2)


event_loop = asyncio.get_event_loop()
try:
  # gather을 사용하면 리스트 안에 내용이 다 실행되야,
  # 다음줄 실행 가능
    result = event_loop.run_until_complete(asyncio.gather(
        hello_world(),
        hello_python(),
    ))
    print(result)
finally:
    event_loop.close()
