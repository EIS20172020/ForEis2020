# Git的几个基本操作

参考博客：

[如何使用git把本地代码上传（更新）到github上](https://baijiahao.baidu.com/s?id=1619544681032320225&wfr=spider&for=pc)

[一个小时学会Git](https://www.cnblogs.com/best/p/7474442.html)



### 1.初始化

在文件管理器中新建一个文件夹，进入该文件夹，右键选择`Git Bash Here`打开Git命令行

输入命令`git init`，初始化本地仓库



### 2.建立本地仓库与远程仓库的连接

```shell
git remote rm origin

git remote add origin <仓库地址>
```



### 3.将本地仓库更新到远程仓库

```shell
git status

git add --all

git commit -m "first commit"

git push -u origin master
```



### 4.更新本地仓库(将远程Git仓库拉取到本地)

```shell
git pull
```





 