# Branch分支
## 查看当前分支

```git branch```

在主分支
```
> git branch
* master
  zhuheran
```
在zhuheran分支下
```
> git branch
  master
* zhuheran
```




- 分支的创建、删除和查看
git branch fetch 创建一个分支fetch
git branch 查看当前系统的分支,和正在使用的分支
git branch -d 删除已经被当前分支合并了的分支，也可以指定“fetch分支”,如：git branch -d fetch
git branch -d fetch 清除fetch分支
git branch -D crazy-idea 强制删除未合并的分支

分支的切换
git checkout master 切换到master分支
git checkout master && git merge fetch 切换到master分支，并合并fetch分支
git checkout v1.2
git checkout tags/v1.2

分支的合并
git merge fetch 将分支fetch并入当前分支
git merge <branch> --squash 将指定分支（即<branch>分支）的所有提交合并成一个，然后并入当前分支,最后提交（git commit -m ‘’）###

分支的重置
git reset --hard HEAD 回到合并前状态
git reset --hard ORIG_HEAD 放弃修改当前的冲突，这条命令可以回到合并前状态
git reset --hard ORIG_HEAD 已经把合并后的代码提交，然后想把它们撒销（有危险，如果别人已经合并了你的代码）
其它
git fetch origin 当远程仓库有更新，但我们并不想合并到本地仓库，只想把代码拿下来看看
git reflog reflog是记录引用变化的一种机制，比如记录分支的变化或者是HEAD引用的变化，当忘记分支名的时候也可以使用