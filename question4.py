import asyncio;

async def  fetch_data_1():
  print("fetched data1") 
  await asyncio.sleep(2)
  print("completed fetching data1") 
  return
async def fetch_data_2():
  print("fetched data2")
  await asyncio.sleep(3)
  print("completed fetching data2") 
  return

async def main():
  # print("Debug1")
  await asyncio.gather(fetch_data_1(),fetch_data_2())
  # return res

# asyncio.run(fetch_data_1())
# asyncio.run(fetch_data_2())
asyncio.run(main())