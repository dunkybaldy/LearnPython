import asyncio


async def function_one():
    while True:
        print("1")
        await asyncio.sleep(10)
        print("11")


async def function_two():
    while True:
        print("2")
        await asyncio.sleep(2)
        print("22")


async def function_three():
    while True:
        print("3")  # no await keyword? asynchronicity goes out the window, can't free up loop to run other functions
        await asyncio.sleep(0.1)
        print("33")


async def main():
    loop = asyncio.get_event_loop()
    loop.create_task(function_one())
    loop.create_task(function_two())
    loop.create_task(function_three())  # only creating tasks

loop = asyncio.get_event_loop()
loop.run_forever()
# asyncio.run(main())  # The same as writing run_until_complete(main())
