# Asynchronous programming with asyncio
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched!")

async def process_data():
    print("Processing data...")
    await asyncio.sleep(1)
    print("Data processed!")

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(process_data())
    
    await task1
    await task2

# Running the async main function
asyncio.run(main())
