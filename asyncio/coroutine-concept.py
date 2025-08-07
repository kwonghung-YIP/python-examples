import asyncio

async def coroutine_without_await():
    for i in range(5):
        print (i)

async def async_main():
    coroutine1 = coroutine_without_await()
    print(f"type of coroutine_without_await: {type(coroutine1)}")

    print("create task")
    task = asyncio.create_task(coroutine1)

if __name__ == "__main__":
    asyncio.run(async_main())