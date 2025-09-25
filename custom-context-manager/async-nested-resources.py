import contextlib
import asyncio

class AsyncResourceA:
    def __init__(self):
        print("AsyncResourceA __init__")
    
    async def __aenter__(self):
        print("AsyncResourceA __aenter__")
        await asyncio.sleep(0.5)
        self.name = "AsyncResourceA"
        return self
    
    async def __aexit__(self,except_type,except_value,traceback):
        print("AsyncResourceA __aexit__")
        await asyncio.sleep(0.5)
        if except_type is not None:
            print(f"ResourceA catch exception:{except_type}-{except_value}")
            # return True # ResourceA suppress the exception and won't propagate to ResourceB

class AsyncResourceB:
    def __init__(self):
        print("AsyncResourceB __init__")
    
    async def __aenter__(self):
        print("AsyncResourceB __aenter__")
        self.name = "AsyncResourceB"
        await asyncio.sleep(0.5)
        return self
    
    async def __aexit__(self,except_type,except_value,traceback):
        print("AsyncResourceB __aexit__")
        await asyncio.sleep(0.5)
        if except_type is not None:
            print(f"ResourceB catch exception:{except_type}-{except_value}")

async def main():
    with contextlib.suppress(ZeroDivisionError): #suppress 100/0 error
        async with AsyncResourceB() as b, AsyncResourceA() as a:
            print("main...")
            print(f"{a.name},{b.name}")
            y = 100/0

    print("statements after with...")

if __name__ == "__main__":
    asyncio.run(main())