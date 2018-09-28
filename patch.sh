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
