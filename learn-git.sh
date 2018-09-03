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
    只显示commit id和提交的说明（commit -m)
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
    17.3. 切换回master分支
    # git checkout master


