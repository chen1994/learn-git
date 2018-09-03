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
15. 将本地库的所有内容推送到远程库中
    # git push -u origin master
    第一次推送master分支，需要加上-u参数，git会将本地的master分支内容推送到远程新的master分支，并且将本地master分支和远程master分支关联，以后再推送就可以简化命令。


