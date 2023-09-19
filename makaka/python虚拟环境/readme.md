
```shell
sudo apt/yum install python3-venv  # 安装env工具

python -m venv myenv   # 创建虚拟环境名为myenv
source myenv/bin/activate  # 激活虚拟环境
pip3 freeze > requirements.txt # 将安装的库及版本导出到txt文件中
deactivate     # 退出

  
```


经测试，将虚拟环境直接打包移到另一个平台上的结论：

树莓派到ubuntu  --> 丢失，在ubuntu上激活后，出现了未安装的库，安装的库也消失了

ubuntu 到 ubuntu，不同版本 --> pip直接找不到了

树莓派到树莓派  --> 成功
