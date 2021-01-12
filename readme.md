# 作业-分布式系统与云计算  
   
卜一凡    201804213019        CUC_Eliot
  
## 作业1：配置虚拟机/云服务器
（*由于VirtualBox在电脑上无法正常安装Ubuntu，选用了阿里云ECS云服务进行实验-学生认证试用*）  
  
### ECS概况
i-2zebgg7ge2poc9g7w03r（murlight）  
2 vCPU 4GiB (I/O优化) 1Mbps   
ip地址（公）：39.105.163.103  
ip地址（私有）：172.27.165.193  
![Image text](https://github.com/Murmansker/Django-example/blob/master/image-homework/ECS-1.jpg)  
ECS-1  
  
### 安全组概况
![Image text](https://github.com/Murmansker/Django-example/blob/master/image-homework/ECS-2.jpg)  
ECS-2  
  
### 云服务器连接状况
![Image text](https://github.com/Murmansker/Django-example/blob/master/image-homework/ECS-3.jpg)  
ECS-3  
![Image text](https://github.com/Murmansker/Django-example/blob/master/image-homework/ECS-4.jpg)  
ECS-4  
  
### 尝试PING通
![Image text](https://github.com/Murmansker/Django-example/blob/master/image-homework/ECS-5.jpg)  
ECS-5  
  
### 更新操作系统
`apt updata`  
`apt upgrade`  
  
### 安装git,python等
`apt install git`  
`apt install python3`  

### 测试http server服务  
![Image text](https://github.com/Murmansker/Django-example/blob/master/image-homework/ECS-6.jpg)  
ECS-6  
![Image text](https://github.com/Murmansker/Django-example/blob/master/image-homework/ECS-7.jpg)  
ECS-7  
可以正常访问，所有链接无异常  
  
  
  
  
## 作业2：django-clouddisk-example
  
### 前期准备与环境配置
1、已有github仓库，地址如下：  
Murmanskerのgithub主站 https://github.com/Murmansker 
![Image text](https://github.com/Murmansker/Django-example/blob/master/image-homework/CD-1.jpg)  
CD-1  
2、在本地git bash中命令行中运行命令生成公私钥对ssh-keygen  
3、将 ~/.ssh/id_rsa.pub私钥的内容复制到github服务器的ssh私钥中  
4、git clone服务器中的仓库地址到本机  
`git clone git@github.com:Murmansker/Django-example.git`  
5、通过终端控制台在仓库中增加文件：readme.md；增加app：news、polls  
  
**常用git命令  
  
'''  
git add .  
git status  
git commit -m " "  
git push  
'''  

### 利用Django框架尝试编写应用
参考教程：编写你的第一个Django应用
https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/
