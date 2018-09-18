1. 设置git仓库的用户名和Email
    --global参数使这台机器上所有git仓库都使用这个配置
    $ git config --global user.name "Your Name"
    $ git config --global user.email "email@example.com"
2. 创建一个空目录，初始化git仓库
    # git init
    init之后当前目录下多了一个.git的目录，这个目录是Git来跟踪管理版本库的，不要随意修改
3. 创建一个文件,添加到仓库，并提交
    # vim readme.txt
    git add告诉Git，把文件添加到仓库
    # git add readme.txt
    git commit告诉Git，把文件提交到仓库,-m后面输入的是本次提交的说明
    # git commit -m 'wrote a readme.txt'
    commit可以一次性提交多个文件（多次add后一次性commit）
4. 查看仓库当前状态
    # git status
5. 查看上次修改的内容,历史记录
    # git diff readme.txt
    git log查看历史记录
    # git log
    只显示commit id和提交的说明（commit -m）
    # git log --pretty=oneline
6. 版本回退：
    # git reset --hard HEAD^
    注：HEAD后面多少个^就代表回退多少个版本，回退的版本太多比如回退到往上100个版本：HEAD~100
    git版本回退的速度非常快，因为git内部有个指向当前版本的HEAD指针，当你回退版本时，git仅仅是把HEAD指针指向你想回退的那个版本
7. 回退后再恢复：
    1. 使用git reset命令，需要知道未来版本的commit id(id不用写全，写前几个字母就好了)
    # git reset --hard xxxx
    2. 使用git reflog命令,该命令用来记录你的每一次命令
    # git reflog
    找到对应版本的id,然后使用git reset命令恢复
8. 暂存区和工作区
    git add将文件从工作区添加到暂存区
    git commit一次性将暂存区的所有内容提交到仓库
    对于你的修改，如果没有使用add添加到暂存区就commit，那是不会被提交到仓库的
9. 撤销修改
    9.1. 撤销没有add到暂存区的修改
    # git checkout -- readme.txt
    9.2. 撤销已经add到暂存区的修改，重新放回工作区
    # git reset HEAD readme.txt
    9.3. 撤销已经commit到本地仓库的修改（版本回退）
    # git reset --hard HEAD
10. 删除文件
    # git rm readme.txt
    # git commit -m "rm readme.txt"
11. 创建SSH Key
    # ssh-keygen -t rsa -C '913869524@qq.com'
    保存到自己指定的目录，会生成两个密钥文件：id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。
12. 在github上添加ssh key
    GitHub需要识别你提交的推送确实是你推送的，而不是别人冒充的，Git支持SSH协议，所以Git只要知道了你的公钥，就可以确认你的身份。如果你有多台电脑，可以把每台电脑的key添加到GitHub（git上免费托管的仓库是每个人都可以看到的，所以不要放入敏感信息）
    登陆GitHub，步骤：settings --> SSH and GPG Keys --> New SSH key --> 粘贴id_rsa.pub问价的内容 --> Add SSH Key
13. 在GitHub上创建git仓库
    步骤：New Repository --> name --> create
14. 关联本地已有的仓库
    # git remote add origin git@github.com:chen1994/learngit.git
    只有GitHub上我的仓库的账户列表中有本地SSH Key时，本地才能推送
    关联后，远程库的名字就是origin（git的默认叫法，也可以自定义）
    fnst没有git认证，所以用不了git@github.com，只能使用https：
    # git config --list
    core.repositoryformatversion=0
    core.filemode=true
    core.bare=false
    core.logallrefupdates=true
    remote.origin.url=git@github.com:chen1994/learngit.git
    remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
    # git config --unset remote.origin.url
    # git config --unset remote.origin.fetch
    # git config --list
    core.repositoryformatversion=0
    core.filemode=true
    core.bare=false
    core.logallrefupdates=true
    # git remote add origin https://github.com/chen1994/learn-git.git
    # git config --list
    core.repositoryformatversion=0
    core.filemode=true
    core.bare=false
    core.logallrefupdates=true
    remote.origin.url=https://github.com/chen1994/learn-git.git
    remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
15. 将本地库的所有内容推送到远程库中
    # git push -u origin master
    第一次推送master分支，需要加上-u参数，git会将本地的master分支内容推送到远程新的master分支，并且将本地master分支和远程master分支关联，以后再推送就可以简化命令。
    本地init之后，要先有commit的更新，再push推送到远程仓库
    以上是现有本地库再有远程库时，如何关联远程库
16. 先创建远程库，再从远程库clone
    16.1. GitHub上创建仓库时勾选"Initialize this repository with a README"
    16.2. # git clone https://github.com/chen1994/learn-git.git
    git支持多种传输协议，其中git默认的git://使用ssh, 使用https协议是因为公司内部只开放了http端口，缺点就是速度慢且每次推送都必须要输入口令。
17. 分支与主分支
    可以创建属于自己的分支，推送到远程库，以免影响同时在使用主分支的小伙伴，之后等分支开发完毕，再与主分支合并
    git将每次提交串成一条时间线，这条时间线再git里叫做主分支，即master分支。master指向最新提交，HEAD指向master。
    创建一个新的分支dev，git会新建一个dev指针，指向master当前提交的位置，然后改变HEAD的指向，将HEAD指向dev，这样master分支不会变，以后对工作区的修改和提交，就是针对dev分支的了，每提交一次，dev指针前进一步，而master指针不变。
    等到dev分支上的工作完成了，合并分支时，git就只需要将master指向dev当前的提交。
    合并分支完成后，就可以删除dev分支，git的操作就只是将dev指针删掉就可以了。
    17.1. 创建dev分支
    # git checkout -b dev
    Switched to a new branch 'dev'
    创建的同时自动切换到dev分支，之后工作区的所有提交都会提交到dev分支
    -b表示branch
    17.2. 查看当前分支
    # git branch
    * dev
      master
    git branch 命令会列出所有分支，*号标识当前分支
    17.3. 提交learn-git.sh
    # git add learn-git.sh
    # git commit -m 'update learn-git.sh'
    17.4. 切换回master分支
    # git checkout master
    此时查看learn-git.sh发现刚才的修改不见了，这是因为刚才的提交在dev分支上，master分支此刻的提交点没有变。
    17.5. 将dev分支的工作成果过合并到master分支
    # git merge dev
    Updating ef3bacd..0464290
    Fast-forward
     learn-git.sh | 47 +++++++++++++++++++++++++++++++++++++++++++++++
      1 file changed, 47 insertions(+)
    merge用于合并指定分支到master分支
    Fast-forward 信息代表本次合并是'快进模式',也就是直接将master指向dev当前的提交，所以速度非常快。（这只是其中一种合并方式）
    17.6. 删除dev分支（合并完成后）
    # git branch -d dev
    Deleted branch dev (was 0464290).
    # git branch
    * master
    17.7. 当master分支和dev分支各自有新的提交时
    从dev切换回master分支时会提示当前master分支比远程master分支要超前一个提交：
    # git checkout master
    Switched to branch 'master'
    Your branch is ahead of 'origin/master' by 1 commit.
      (use "git push" to publish your local commits)
    此时git无法进行快速合并，如果试图将各自的修改合并起来，就可能会有冲突
    # git merge feature1
    Auto-merging learn-git.sh
    CONFLICT (content): Merge conflict in learn-git.sh
    Automatic merge failed; fix conflicts and then commit the result.
    此时只能手动解决冲突后再提交，使用git status可以看到是哪些文件导致了冲突
    此时再次打开learn.git.sh查看可以看到：git用如下类似diff的分隔符来标记冲突差异部分：
    <<<<<<< HEAD
    # changes in master
    =======
    # changes in dev
    >>>>>>> dev
    修改后重新提交 
    此时使用git log可以查看分支合并情况：
    # git log --graph --pretty=oneline --abbrev-commit
    *   b3431ee update learn-git.sh after test conflicts
    |\
    | * d9d5dd2 update learn-git.sh in dev
    * | de7c9bd update learn-git.sh in master
    |/
    * 0464290 update learn-git.sh
    * ef3bacd add learn-git.sh
    最后再将dev分支删除
18. 使用fast forward模式合并分支时，删除分支后，会丢掉分支信息。
    如果强制禁用Fast forward模式，git在merge时会生成一个新的commit，这样就可以从分支历史上看出分支信息。
    # git merge --no-ff -m 'merge with no-ff' dev
    Merge made by the 'recursive' strategy.
     learn-git.sh | 13 +++++++++++++
      1 file changed, 13 insertions(+)
    因为本次合并要创建一个新的commit，所以使用-m参数把commit的描述写进去。
    查看分支历史：
    # git log --graph --pretty=oneline --abbrev-commit
    *   a5beb66 merge with no-ff
    |\
    | * 15e3565 update learn-git.sh in dev
    |/
    *   b3431ee update learn-git.sh after test conflicts
    正式作业的时候，应该有个master分支，用于发布新版本，平时不在上面干活；
    再有个dev分支，所有人都在dev分支上干活，每个人都有自己的分支，时不时将自己的分支网dev分支上合并就行了。
19. bug分支
    当你在自己分支上的工作进行到一半，还没有提交到dev分支时，突然出现一个bug,要你紧急修复，可以为bug创建一个新的临时分支来修复，修复后合并分支，再删除临时分支
    问题就是当前在dev分支上的工作还没有结束（工作还没完成，没法提交）
    git提供了一个stash功能，将当前工作现场隐藏起来，等以后恢复现场后继续工作：
    # git branch
    * dev
      master
    # git status
    ...
    #       modified:   learn-git.sh
    ...
    当前工作现场的文件还没有提交
    # git stash
    Saved working directory and index state WIP on master: a5beb66 merge with no-ff
    HEAD is now at a5beb66 merge with no-ff
    # git status
    此时再看工作区就是干净的，可以放心的创建分支来修复bug
    首先需要确定要在哪个分支上修复bug，比如要在master分支上修复:
    # git checkout master
    创建临时bug修复分支：
    # git checkout -b bug-1
    xxx进行bug修复工作，修复完成后commit
    回到master分支merge:
    # git checkout master
    # git merge --no-ff -m 'merge bug fix bug1' bug-1
    再回到dev分支恢复工作现场：
    # git checkout dev
    # git stash list
    stash@{0}: WIP on dev: 15e3565 update learn-git.sh in dev
    工作现场还在，只是git把stash内容存在某个地方了，需要恢复，有两种办法恢复：
    1. 恢复工作现场，但不删除stash内容
    # git stash apply
    ...
    #          modified:   learn-git.sh
    ...
    # git stash list
    stash@{0}: WIP on dev: 15e3565 update learn-git.sh in dev
    需要手动删除stash：
    # git stash drop
    Dropped refs/stash@{0} (e82485e7f6d2b8aa1634bb9b03e55eecc6fcee41)
    2. 恢复的同时将stash内容一起删除
    # git stash pop
    指定stash：
    # git stash pop stash@{0}
20. 删除临时分支及临时分支中未合并的内容
    在开发新功能时，一般会新建一个feature分支来开发，完了再合并到dev分支
    但是当feature分支中已经commit，还没有合并到dev分支时，却通知该新功能不需要了，此时这个新功能的内容也不能保存得删除
    使用git branch -d feature是不能删掉的
    # git branch -d feature1
    error: The branch 'feature1' is not fully merged.
    If you are sure you want to delete it, run 'git branch -D feature1'.
    得用-D强制删除：
    # git branch -D feature1
    Deleted branch feature1 (was fd168cd).
21. 查看远程库信息
    # git remote
    origin
    # git remote -v
    origin  https://github.com/chen1994/learn-git.git (fetch)
    origin  https://github.com/chen1994/learn-git.git (push)
    如果没有推送权限，就看不到push
22. 推送分支
    将本地所有的commit推送到origin库
    # git push origin master
    推送其他分支（如dev）：
    # git push origin dev
23. 抓取分支
    多人协作开发时，小伙伴使用另一台电脑/同一台电脑的不同目录，需先从远程克隆：
    # git clone https://github.com/chen1994/learn-git.git
    # git branch
    * master
    默认只能看到本地的master分支，如果要在dev分支上开发，就必须创建远程origin的dev分支到本地：
    # git checkout -b dev origin/dev
    现在小伙伴就可以在dev上进行修改和推送
    # git add xxx, # git commit -m 'xxx', # git push origin dev
    因为小伙伴已经向origin/dev分支推送了他的提交，如果碰巧你对同样的文件做了修改，此时你再推送的时候失败：
    # git push origin dev
    Username for 'https://github.com': chen1994
    Password for 'https://chen1994@github.com':
    To https://github.com/chen1994/learn-git.git
     ! [rejected]        dev -> dev (fetch first)
     error: failed to push some refs to 'https://github.com/chen1994/learn-git.git'
     hint: Updates were rejected because the remote contains work that you do
     hint: not have locally. This is usually caused by another repository pushing
     hint: to the same ref. You may want to first merge the remote changes (e.g.,
     hint: 'git pull') before pushing again.
     hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    根据提示使用git pull将最新的提交从origin/dev抓下来，在本地合并，解决冲突后再推送：
    # git pull 
    There is no tracking information for the current branch.
    Please specify which branch you want to merge with.
    See git-pull(1) for details

        git pull <remote> <branch>

    If you wish to set tracking information for this branch you can do so with:

        git branch --set-upstream-to=origin/<branch> dev
    根据提示，设置远程分支与本地分支的连接：
    # git branch --set-upstream-to=origin/dev dev
    Branch dev set up to track remote branch dev from origin.
    再重新pull，如果pull时有冲突，再手动解决冲突后再push
    如果git pull提示no tracking information，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream-to=origin/dev dev
24. 将分支提交历史显示为一条直线
    # git log --graph --pretty=oneline --abbrev-commit
    *   ec443cf Merge branch 'dev' of https://github.com/chen1994/learn-git into dev
    |\
    | * 3ee2958 update by another pattner,add title
    * | 0b2dfd9 update learn-git.sh
    * | 3700393 update learn-git.sh
    |/
    ...
    这是由于多个人在同一个分支上操作，有些冲突或者合并操作，导致历史不是一条直线
    这样看起来不方便，使用git rebase命令，将历史变成一条直线：
    # git rebase
25. 清空git log
    方法1：git reset
        --soft (仅删除log，保留提交所做的更改)
        删除最近一次提交的log：
        # git reset --soft HEAD^
        删除最近三次提交的log：
        # git reset --soft HEAD~3
        --hard (删除log的同时不保留删除记录所做的更改)
    方法2：git rebase（可用于删除中间的记录）
        将master分支删除最近三个提交
        # git rebase --onto master~3 master~1 master        
26. 清空git reflog
    # git reflog expire --expire=now --all
27. 删除远程库文件
    # git rm -r -n --cached 文件/文件夹名称
    -n这个参数不会删除任何文件，只是打印出文件列表预览
    确认无误后，再删除：
    # git rm -r --cached 文件/文件夹名称
    提交到本地，并添加提交说明
    # git commit -m 'rm bug1'
    # git push origin master
28. 修改最近一次的提交
	# git commit --amend
29.
30.
