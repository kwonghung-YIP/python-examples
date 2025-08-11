import asyncio

async def callback(future:asyncio.Future):
    print("start callback...")
    await asyncio.sleep(5)
    #future.set_result("abcd1234")
    future.set_exception(RuntimeError("runtime error"))
    print("finish callback!")

async def main():
    print("create future...")
    future = asyncio.Future()

    print(f"future done? {future.done()}")

    asyncio.create_task(callback(future))
    print(await future)

    print(f"future done? {future.done()} result: {future.result()}")

if __name__ == "__main__":
    asyncio.run(main())
