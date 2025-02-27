import asyncio
import threading 
import time

async def fetch_data(s): await asyncio.sleep(2); print(f"Async task result: Data fetched from {s}.")

def print_thread():
    for i in range(1, 6): time.sleep(1); print(f"Thread: {i} sec elapsed...")

async def main():
    t = threading.Thread(target=print_thread)
    t.start()
    await asyncio.gather(fetch_data("A"), fetch_data("B"))
    t.join()

asyncio.run(main())
