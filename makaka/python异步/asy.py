# import asyncio
# import time

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))

#     task2 = asyncio.create_task(
#         say_after(2, 'world'))

#     print(f"started at {time.strftime('%X')}")

#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2

#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())





# import asyncio

# async def nested():
#     return 42

# async def main():
#     # Nothing happens if we just call "nested()".
#     # A coroutine object is created but not awaited,
#     # so it *won't run at all*.
#     nested()

#     # Let's do it differently now and await it:
#     print(await nested())  # will print "42".

# asyncio.run(main())



# import asyncio
# import datetime

# async def display_date():
#     loop = asyncio.get_running_loop()
#     print(loop,type(loop))
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)

# asyncio.run(display_date())

# import asyncio
# async def main():
#     print('hello')
#     await asyncio.sleep(1)
#     print('world')
# asyncio.run(main())

# import asyncio
# import time
# async def display_time(num, timeout):
#     print(f'hello world {num}')
#     await asyncio.sleep(timeout)
# async def main():
#     print(f"started at {time.strftime('%X')}")
#     await asyncio.create_task(
#         display_time(1, 1))
#     await display_time(2,2)
#     print(f"end at {time.strftime('%X')}")

# asyncio.run(main())

# 最终执行时间为两个协程执行时间最小公约数
# import asyncio
# import time

# async def display_time(num:int, timeout:int):
#     print(f'hello world {num}')
#     await asyncio.sleep(timeout)
#     return num

# async def main():
#     print(f"started at {time.strftime('%X')}")
#     ls =await asyncio.gather(display_time(1, 1), display_time(2, 2))
#     print(f"end at {time.strftime('%X')}")
#     print(ls)

# asyncio.run(main())

# # 当display_time函数运行时长超出asyncio.timeout()时报TimeoutError
# import asyncio
# async def display_time(timeout):
#     await asyncio.sleep(timeout)
#     print('OK')

# async def main():
#     try:
#         await asyncio.wait_for(display_time(3), timeout=2)
#     except TimeoutError:
#         print("The long operation timed out, but we've handled it.")

#     print("This statement will run regardless.")
# asyncio.run(main())

# import asyncio

# async def my_coroutine():
#     print("开始执行协程任务")
#     await asyncio.sleep(1)
#     print("任务结束")
# async def main():
#     print("开始主程序")
#     task = asyncio.create_task(my_coroutine())
#     await asyncio.sleep(2)
#     print("继续执行主程序")
#     await task
#     print("协程任务执行完成")

# asyncio.run(main())


# # create_task自动调度执行协程函数
# import asyncio
# async def nested():
#     return 42

# async def main():
#     task = asyncio.create_task(nested())
#     await task
#     print(task.result())

# asyncio.run(main())

# import asyncio

# async def my_coroutine():
#     loop = asyncio.get_running_loop()
#     print(f"当前事件循环：{loop}")

# async def main():
#     await my_coroutine()

# asyncio.run(main())
# asyncio.get_running_loop().

# # 将同步阻塞函数转换成可等待对象，使得其可以并发执行
# import asyncio, time
# def blocking_io():
#     print(f"start blocking_io at {time.strftime('%X')}")
#     # Note that time.sleep() can be replaced with any blocking
#     # IO-bound operation, such as file operations.
#     time.sleep(1)
#     print(f"blocking_io complete at {time.strftime('%X')}")

# async def display_time(timeout):
#     await asyncio.sleep(timeout)
#     print('OK')

# async def main():
#     print(f"started main at {time.strftime('%X')}")

#     await asyncio.gather(
#         asyncio.to_thread(blocking_io),
#         display_time(2))

#     print(f"finished main at {time.strftime('%X')}")

# asyncio.run(main())

import asyncio

async def my_coroutine():
    print("Running coroutine")
    await asyncio.sleep(1)
    return "Coroutine completed"

async def main():
    task = asyncio.create_task(my_coroutine())
    print("Task created")

    await asyncio.sleep(0.5)

    if task.done():
        result = task.result()
        print(f"Task result: {result}")

asyncio.run(main())
