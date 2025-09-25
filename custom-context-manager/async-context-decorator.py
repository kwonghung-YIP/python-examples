import contextlib
import asyncio

class myAsyncContextDecorator(contextlib.AsyncContextDecorator):
    def __init__(self):
        print("myAsyncContextDecorator __init__")

    async def __aenter__(self):
        print("myAsyncContextDecorator __aenter__")
        await asyncio.sleep(0.5)
        return self
        
    async def __aexit__(self, except_type, except_value, traceback):
        print("myAsyncContextDecorator __aexit__")
        await asyncio.sleep(0.5)
        if except_type is not None:
            print(f"myAsyncContextDecorator catch exception:{except_type}-{except_value}")
            #return True # suppress exception
        
@myAsyncContextDecorator()
async def funcA():
    print("funcA()....")
    await asyncio.sleep(0.5)
    y = 100/0

if __name__ == "__main__":
    asyncio.run(funcA())