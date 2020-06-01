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
        print("3")
        await asyncio.sleep(0.1)
        print("33")


async def main():
    try:
        tasks = [function_one(), function_two(), function_three()]
        await asyncio.gather(*tasks)
    except KeyboardInterrupt as kiex:
        print(f"KeyboardInterrupt: {kiex}")
    except Exception as appFailure:
        print(f"Application failure. Reason: {appFailure}")
    finally:
        print("Program shutting down...")

asyncio.run(main())