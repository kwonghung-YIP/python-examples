import asyncio

async def coroutine_without_return():
    print("calling into coroutine_without_return...")
    for i in range(5):
        await asyncio.sleep(1)
        print (i)

async def coroutine_with_return():
    print("calling into coroutine_with_return...")
    ttl = 0
    for i in range(5):
        await asyncio.sleep(1)
        print (i)
        ttl += i*i
    return ttl

async def coroutine_with_exception():
    print("calling into coroutine_with_exception...")
    for i in range(4,-1,-1):
        await asyncio.sleep(1)
        print(i)
        r = 10/i

async def coroutine_without_await():
    await asyncio.sleep(9999)

async def coroutine_for_create_task():
    print("This part is executed while calling asyncio.create_task...")
    await asyncio.sleep(1)
    print("This part is executed after putting the task with await statement...")

async def async_main():
    # calling the async function return a coroutine object,
    # a coroutine object is ready for executed by the event-loop,
    # and by putting it with the await statement, it is wrapped by
    # a task and scheduled to be executed by the event-loop

    coroutine1 = coroutine_without_return()
    print(f"type of coroutine_without_return: {type(coroutine1)}")

    print("await coroutine_without_return...")
    await coroutine1

    coroutine2 = coroutine_with_return()
    print("await coroutine_with_return...")
    ttl = await coroutine2
    print(ttl)

    try:
        coroutine3 = coroutine_with_exception()
        print("await coroutine_with_exception...")
        await coroutine3
    except ZeroDivisionError as err:
        print(err)

    # raise the RuntimeWarning after exit the program if a coroutine never been "await"
    #coroutine4 = coroutine_without_await()
    #print("await coroutine_without_await...")

    coroutine5 = coroutine_for_create_task()
    task = asyncio.create_task(coroutine5)
    print("put task into await statment...")
    await task

if __name__ == "__main__":
    asyncio.run(async_main())