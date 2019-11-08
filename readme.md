> 操作系统: Windows/Linux  
> 上次使用: 2019/10/01

### 常用代码托管平台
github 访问速度比较慢,但用户量大,公开仓库多,很多公开仓库可做学习交流使用.  
gitee 为国内平台,访问速度快,但公开仓库很少,一般只做代码托管  
### git配置

##### 一.安装
在 [git官网](https://git-scm.com/downloads?_blank "git官网") 下载git并安装

##### 二.验证安装
打开 CMD(windows下) 或 terminal(linux下) 输入命令git出现如下图帮助提示说明安装完成
![image.png](https://i.loli.net/2019/10/16/bADXdYeM2USkPCW.png)

##### 三.配置账号
配置本地仓库的账号和邮箱
```bash
git config --global user.name "Your Name"
git config --global user.email "Jesse@v2et.cn"
```

### 创建项目

##### 一.在托管平台创建新的仓库拉到本地
1. 在代码托管平台创建项目,
2. 从托管平台clone项目代码
3. 将远程仓库克隆到本地,
```bash
git clone https://github.com/Jesse201147/v2et.git
```

##### 二.将本地项目上传到git
1. 打开 CMD/Terminal 进入项目根目录
2. 初始化仓库 & 本地提交
```bash
git init    # 初始化本地git仓库,会在根目录自动创建.git文件夹
git add *    # 将项目中所有文件add到暂存区(可以理解为加关注)
git commit -m 'init repo'    # 将本地文件提交到本地版本库,本次提交的备注信息为 init repo
```
3. 在git/gitee创建仓库
4. 将本地仓库关联到远程仓库
```bash
git remote add origin https://xxx.git
```
5. 拉远程仓库和本地合并 & 将本地仓库推送到远程
```bash
git pull --rebase origin master
git push -u origin master
```
三. 添加与提交改动(到本地版本库)
```bash
git add <filename>  # add * 可以自动添加所有文件 
git commit -m 'something'    # 将改动提交到本地版本库
```
四. 推送改动
```bash
git push origin master
```
五. 更新与合并
```bash
git pull    # 从远端更新本地仓库
git merge <branch>    # 将远端改动合并到当前分支
```
六. 舍弃本地改动
```bash
git fetch origin    # 将本地分支指向远端最新分支
git reset --hard origin/master 
```
七. 图形界面工具  
1. git for windows 自带图形界面工具: 界面很简洁, 功能很少, 不太好用  
2. TortoiseGit 小乌龟: 适用于windows 功能很全, 操作很简洁, 很好用  
3. pycharm 自带VSC工具: ***强烈推荐***, 功能全面, 无需单独安装, 配置简单, 操作无脑