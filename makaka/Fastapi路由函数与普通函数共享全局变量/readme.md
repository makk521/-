### 问题：

Fastapi的路由函数与普通函数之间无法共享队列，因为uvicorn运行时会重新定义新队列！

```python
import logging
import time
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
import uvicorn
import queue
from  threading import Thread

logger = logging.getLogger(__name__)
app = FastAPI()
counter = 0
q = queue.Queue()

@app.get('/')
def hello():
    q.put(1)
    print(q, q.qsize())
    return 'Hello'

def printIfo():
    global q
    while(1):
        print(q, q.qsize())
        time.sleep(3)

if __name__ == "__main__":
    Thread(target = printIfo).start()
    # 一直开启api接口
    Thread(uvicorn.run('test:app', host='0.0.0.0', port=5000, reload=True)).start # 阻塞的
```

运行后发现两个线程操作的q不是同一个，无法进行共享，原因就是uvicorn这个线程又定义了一次。

### 解决方法

```python
import logging
import time
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
import uvicorn
import queue

logger = logging.getLogger(__name__)
app = FastAPI()
counter = 0
q = queue.Queue()

@app.get('/')
def hello():
    q.put(1)
    print(q, q.qsize())
    return 'Hello'

@app.on_event("startup")
@repeat_every(seconds=1, logger=logger, wait_first=True)
def periodic():
    while True:
        print(q,q.qsize())
        time.sleep(3)

if __name__ == "__main__":
    uvicorn.run("Constan_exe:app", host="0.0.0.0", port=8000, workers=1)
```

将另一个线程写入repeat_every中，类似于进程，此时就可以队列共享

repeat_every : 在后台执行着，每隔seconds秒执行一次，项目中需要socket，则连接后进入死循环即可。


### 参考链接

[中文版](https://cloud.tencent.com/developer/ask/sof/106410807)
