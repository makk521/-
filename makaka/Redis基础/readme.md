



#### 安装

基于Ubuntu系统安装:

##### 安装Redis服务器

```
sudo apt-get install redis-server
```

##### 启动Redis服务器:

一般来说，当安装完成后，Redis服务器会自动启动，可以通过以下命令检查是否启动成功。（ps：如果Active显示为 active(running) 状态：表示redis已在运行，启动成功）

```
service redis-server status
```

![1695114030527](image/readme/1695114030527.png)

检查当前进程，查看redis是否启动。（ps: 可以看到redis服务正在监听6379端口）

```
ps -aux|grep redis-server
```

![1695114071584](image/readme/1695114071584.png)

上面的127.0.0.1 是redis服务器的 IP 地址，6379 是 Redis 服务器运行的端口。



### 命令
