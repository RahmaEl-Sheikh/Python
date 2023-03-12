import time

def task1():
    print("Task 1 started")
    time.sleep(2) # wait for 2 seconds
    print("Task 1 finished")

def task2():
    print("Task 2 started")
    time.sleep(1) # wait for 1 second
    print("Task 2 finished")

# Run the tasks synchronously
task1()
task2()

################################################333

import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2) # wait for 2 seconds asynchronously
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1) # wait for 1 second asynchronously
    print("Task 2 finished")

# Run the tasks asynchronously
async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
