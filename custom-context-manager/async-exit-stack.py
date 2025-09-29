import contextlib
import asyncio

class MyAsyncResource:
    def __init__(self,name):
        print(f"MyAsyncResource({name}) __init__")
        self.name = name

    async def __aenter__(self):
        print(f"MyAsyncResource({self.name}) __aenter__")
        await asyncio.sleep(0.5)
        return self
    
    async def __aexit__(self,except_type,except_value,traceback):
        print(f"MyAsyncResource({self.name}) __aexit__")
        await asyncio.sleep(0.5)
        if except_type is not None:
            print(f"MyAsyncResource catch exception:{self.name}:{except_type}-{except_value}")

async def callback(paramA,paramB):
    print(f"callback({paramA},{paramB})")
    await asyncio.sleep(0.5)

async def main():
    # order of the exitStack callback, __aexit__, (last register fist call)
    async with contextlib.AsyncExitStack() as exitStack:
        resA = await exitStack.enter_async_context(MyAsyncResource("ResourceA"))
        resB = await exitStack.enter_async_context(MyAsyncResource("ResourceB"))
        resC = await exitStack.enter_async_context(MyAsyncResource("ResourceC"))

        # "push_async_exit" similar to "push", it registers the __aexit__ of
        # resourceD into the exit stack, but does not invoke the __aenter__ 
        resD = exitStack.push_async_exit(MyAsyncResource("ResourceD"))

        try:
            await asyncio.sleep(0.5)
            print(f"{resA.name},{resB.name},{resC.name},{resD.name}")

            # "push_async_callback" similar to "callback", it registers the
            # async callback into the callback stack
            exitStack.push_async_callback(callback,"A","B")
            exitStack.push_async_callback(callback,"B","C")

            y = 100/0

        finally:
            print("final statement in with block")


if __name__ == "__main__":
    asyncio.run(main())
