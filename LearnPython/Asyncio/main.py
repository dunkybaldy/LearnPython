import asyncio


async def function_one():
    print("1")
    await asyncio.sleep(10)
    print("11")


async def function_two():
    while True:
        print("2")
        await asyncio.sleep(2)
        print("22")


loop = asyncio.get_event_loop()
loop.create_task(function_one())
loop.create_task(function_two())
# loop.run_until_complete(function_two())  # run until function_two has completed, function_one() will still run
# loop.run_forever()  # the loop will run forever, but the functions will not be repeated
# Imagine the event loop is a thread from a pool which has been assigned to this program.
loop.run_until_complete(function_one())  # will print out "2" and "22" a lot but once "11" is printed then the
# program will stop
