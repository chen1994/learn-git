SOURCE目录下有.patch文件
使用patch命令：
1. 加patch
	# patch -p数字 < patch_file
	注：-p数字 ： patch_file里面列出的文件名（目录的截取）
				例：/root/rpmbuild/SOURCES/debrand-single-cpu.patch
					---
					 arch/x86/kernel/setup.c | 2 +-
					 这个arch/x86/kernel/setup.c就是patch_file,
					 即该patch就是对源码中的这个文件进行了修改
					 -p数字，这个数字就代表在这个路径中去掉几个/的意思（从左往右）
					 -p0 : x86/kernel/setup.c
					 -p1 : kernel/setup.c
					 -p2 : setup.c
					 这个数字的取值根据执行patch命令的目录来定
		patch_file : xxx.patch 文件内是对该patch修改的文件的diff结果
					可以使用相对路径
	例：# patch -p0 < /root/rpmbuild/SOURCES/debrand-single-cpu.patch

2. 还原patch（减patch）
	# patch -R < patch_file

3. 例题
	如果有一个很旧版本的软件，这个软件官网已经更新到很新的版本，
	例如kernel，此时可以使用patch file来更新吗？
	
	首先确定旧版本与新版本之间“确实有释出patch file”
	比如kernel 2.2.xx 与kernel 2.4.xx, 这两者基本上的架构都已经不同了，
	所以这两者间是无法用patch file 来更新的。
	但是kernel 2.2.xx 与kernel 2.2.yy 就可以。
	不过因为kernel每次推出的patch file都仅针对前一个版本而已，
	所以要假设kernel 2.2.20升级到kernel 2.2.26
	就必须要使用patch 2.2.21,2.2.22直至patch 2.2.26这6个文件来依序更新才可以。
	但是如果有人帮你将2.2.20与2.2.26比对过，那自然可以直接使用该patch file直接更新。

4. 函数库
	很多软甲之间都会互相取用彼此提供的函数库来进行特殊功能的运行，
	例如验证身份的程序使用PAM模块提供的验证机制，网络连线机制使用SSL函数库来进行连线加密。
	函数库根据是否被编译进程序内部而分为动态与静态函数库。

	4.1 动态(Dynamic) VS 静态(Static) 函数库
	【静态函数库】：
		扩展名：.a	通常为 libxxx.a
		编译行为：	静态函数库在编译的时候直接整合到执行程序中，
					所以利用静态函数编译成的文件会稍大
		独立执行的状态：编译成功的可执行文件可以独立执行，
						而不需要再向外部要求读取函数库(动态函数库)
		升级难易度：若函数库升级，所以使用该函数库的可执行文件都要重新编译
	【动态函数库】：
		扩展名：.so	通常为 libxxx.so
		编译行为：	动态函数在编译的时候，在程序里只有一个“指向(Pointer)”的位置。
					只有当可执行程序使用到函数库的机制时，程序才会去读取函数库来使用。
		独立执行的状态：编译成功的可执行文件不能独立执行，且运行可执行文件时，
						必须保证相关的动态函数库文件存在且所在目录没有变动。
						所以动态函数库不能随意移动或删除，否则会影响很多程序软件。
		升级难易度：升级前后如果函数库文件名和路径没有变，则可执行文件不需要重新编译

5. ldconfig 与 /etc/ld.so.conf
	内存的存取速度是硬盘的好几倍，所以如果将常用的动态函数库先载入内存当中
	(高速缓存，cache),这样当软件要取用动态函数库时就无需从硬盘里面读，
	也就是能提高动态函数库的读取速度。

	将动态函数库载入高速缓存内存中：
	1. 将想载入cache中的动态函数库的 目录 写入 /etc/ld.so.conf
	2. 利用 ldconfig 这个可执行文件将 /etc/ld.so.conf 的数据读入高速缓存中
	3. 同时也会将数据记录一份在 /etc/ld.so.cache 中

	打印cache信息（列出目前所有函数库数据内容，即/etc/ld.so.cache 中的数据）：
	# ldconfig -p

	/etc/ld.so.conf 中一般只有一句话：
	include ld.so.conf.d/*.conf
	所以真正的conf都放在 ld.so.conf.d/*.conf
	
6. 可执行程序的动态函数库解析：ldd
	6.1. 查看可执行程序的函数库数据
	# ldd /usr/bin/passwd
	...
    libpam.so.0 => /lib64/libpam.so.0 (0x00007f8771219000)
    libpam_misc.so.0 => /lib64/libpam_misc.so.0 (0x00007f8771015000)
    libaudit.so.1 => /lib64/libaudit.so.1 (0x00007f8770dec000)
    libselinux.so.1 => /lib64/libselinux.so.1 (0x00007f8770bc5000)
    libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f87709a9000)
	...
	可以看到passwd使用了pam模块

	6.2. 查看函数库的其他相关函数库
	# ldd -v /lib64/libpam.so.0
	...
    libcap-ng.so.0 => /lib64/libcap-ng.so.0 (0x00007f298d66a000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f298e279000)

    Version information:
    /lib64/libpam.so.0:
            libdl.so.2 (GLIBC_2.2.5) => /lib64/libdl.so.2
	...
	
	6.3. 其他用途
	安装RPM包时，有时会报某些函数库之间存在依赖、冲突，
	此时就可以使用ldd来查看这个函数库相关的函数库，
	加上 -v 还可以直接表示该函数库来自哪个软件：
	比如上面的：libdl.so.2 (GLIBC_2.2.5) 这个函数库就可以支持GLIBC_2.2.5等版本

7. 检验软件正确性
	md5sum, sha1sum, sha256sum
	即使是从官网上下载的软件也有可能被篡改过，所以要使用这些命令重新计算hash值，
	再与官网给出的值进行比对，确保正确
	
	为了保证文件系统的安全，可以对如下这些文件进行指纹记录：
	/etc/passwd
	/etc/shadow （假如你不让使用者改密码了）
	/etc/group
	/usr/bin/passwd
	/sbin/rpcbind
	/bin/login （这个也很容易被骇！）
	/bin/ls
	/bin/ps
	/bin/top
	因为许多木马程序运行时，还是会有“执行序，PID”，为了怕被root追查出来，所以都会修改这些检查调度的文件，所以就需要我们将这些文件的指纹记录下来，然后常以shell脚本的方式自动检查指纹表是否变化。
	1. 创建文件列表
	# ls /etc/{passwd,shadow,group} > important.file
	# find /usr/sbin /usr/bin -perm /6000 >> important.file

	2. 创建脚本,计算important.file中文件的hash，并将结果设置为不可修改
	# vim md5.checkfile.sh
	#!/bin/bash
	
	for filename in $(cat important.file)
	do
		md5sum $filename >> finger.file
	done

	# sh md5.checkfile.sh
	# chattr +i finger.file

	3. 修改脚本，用于以后定期检查
	# vim md5.checkfile.sh
	#!/bin/bash

	if [ "$1" == "new" ]; then
		for filename in $(cat important.file)
		do
			md5sum $filename >> finger.file
		done
		echo "New file finger.file is created."
		exit 0
	fi

	if [ ! -f finger1.file ]; then
		echo "file: finger.file NOT exist."
		exit 1
	fi

	[ -f finger_new.file ] && rm finger_new.file

	for filename in $(cat important.file)
	do
		md5sum $filename >> finger_new.file
	done

	testing = $(diff finger.file finger_new.file)

	if [ "$testing" != "" ]; then
		diff finger.file finger_new.file | mail -s 'finger trouble..' root
	fi

	# vim /etc/crontab
	30 2 * * * root cd /root; sh md5.checkfile.sh
	注意: 如果变动是正常的，比如系统的自动升级，这种情况下就得重做finger.file

8. xxx.rpm 与 xxx-devel-xxx.rpm
	RPM的用于一般使用和开发使用的两类，一般devel都不会安装，
	因为终端用户大部分不会去开发软件
	
