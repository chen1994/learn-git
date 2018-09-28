1. 下载最新的kernel
https://www.kernel.org/

2. 解压
# tar -Jxf linux-4.18.8.tar.xz -C /usr/src/kernels
注：-J : --xz
	/usr/src/kernels : Linux kernel源代码一般建议放置于 /usr/src/kernels/ 目录下

3. 目录
	arch ：		与硬件平台有关的项目，大部分指的是 CPU 的类别，例如 x86, x86_64, Xen 虚拟支持等；
	block ：	与区块设备较相关的设置数据，区块数据通常指的是大量储存媒体！还包括类似ext3 等文件系统的支持是否允许等。
	crypto ：	核心所支持的加密的技术，例如 md5 或者是 des 等等；
	Documentation ：	与核心有关的一堆说明文档，若对核心有极大的兴趣，要瞧瞧这里！
	drivers ：	一些硬件的驱动程序，例如显卡、网卡、PCI 相关硬件等等；
	firmware ：	一些旧式硬件的微指令码 （固件） 数据；
	fs ：		核心所支持的 filesystems ，例如 vfat, reiserfs, nfs 等等；
	include ：	一些可让其他程序调用的标头 （header） 定义数据；
	init ：		一些核心初始化的定义功能，包括挂载与 init 程序的调用等；
	ipc ：		定义 Linux 操作系统内各程序的沟通；
	kernel ：	定义核心的程序、核心状态、线程、程序的调度 （schedule）、程序的讯号（signle） 等
	lib ：		一些函数库；
	mm ：		与内存单元有关的各项数据，包括 swap 与虚拟内存等；
	net ：		与网络有关的各项协定数据，还有防火墙模块 （net/ipv4/netfilter/*） 等等；
	security ：	包括 selinux 等在内的安全性设置；
	sound ：	与音效有关的各项模块；
	virt ：		与虚拟化机器有关的信息，目前核心支持的是 KVM （Kernel base Virtual Machine）

4. 保持干净的源代码
因为不清楚到下面载下来的源代码当中有没有保留目标文件 （*.o） 以及相关的配置文件存在，所以需要先清理下：
# make mrproper
CLEAN   scripts/basic
CLEAN   scripts/kconfig
CLEAN   include/config include/generated
注：make mrproper会将以前进行过的核心功能选择文件也删除，所以只有第一次进行kernel编译前才进行这个动作，之后删除前一次编译过程的残留数据请使用：make clean(仅会删除类似目标文件之类的编译过程产生的中间文件，而不会删除配置文件)

5. 挑选核心功能
/boot下面的config-xxx文件就是当前kernel的核心功能列表文件，核心功能的挑选最后会在/usr/src/kernels/linux-xxx/下面生成一个.config的隐藏文件，该文件就是将来的/boot/config-xxx
生成.config的方式：
· make menuconfig	最常使用的，是文字模式下面可以显示类似图形接口的方式，
					不需要启动 X Window 就能够挑选核心功能菜单！
· make oldconfig	通过使用已存在的 ./.config 文件内容，使用该文件内的设置值为默认值，
					只将新版本核心内的新功能选项列出让使用者选择， 可以简化核心功能的挑选过程！
					对于作为升级核心源代码后的功能挑选来说，是非常好用的一个项目！
· make xconfig		通过以 Qt 为图形接口基础功能的图形化接口显示，需要具有 X window 的支持。
					例如 KDE 就是通过 Qt 来设计的 X Window，
					因此你如果在 KDE 画面中，可以使用此一项目。
· make gconfig		通过以 Gtk 为图形接口基础功能的图形化接口显示，需要具有 X window的支持。
					例如 GNOME 就是通过 Gtk 来设计的 X Window，
					因此你如果在 GNOME 画面中，可以使用此一项目。
· make config		最旧式的功能挑选方法，每个项目都以条列式一条一条的列出让你选择，
					如果设置错误只能够再次选择，很不人性化啊！

# cp /boot/config-xxx .config
# make menuconfig
· General setup		与 Linux 最相关的程序互动、核心版本说明、是否使用发展中程序码等信息
					不要随便取消任何一个默认选中的项目
	其中注意如下几项：
	1. Local version - append to kernel release
	[*] Automatically append version information to the version string
	# 我希望我的核心版本成为4.18.8 ，那这里可以就这样设置！
	Kernel compression mode （Bzip2）
	# 建议选择成为 Bzip2 即可，因为压缩比较佳！
	2. Kernel .config support
	[ ] Enable access to .config through /proc/config.gz （NEW）
	# 让 .config 这个核心功能列表可以写入实际的核心文件中！所以就不需要保留 .config 文件啰！
	（20） Kernel log buffer size （16 =&gt; 64KB, 17 =&gt; 128KB）
	# CentOS 7 增加了核心的登录文件容量！占用了 2 的 20 次方，大概用了 1MB 的容量！
	3. 
	[*] Initial RAM filesystem and RAM disk （initramfs/initrd） support
	（） Initramfs source file（s）
	# 这是一定要的！因为要支持开机时载入 initail RAM disk 嘛！
· loadable module	让kernel支持动态的核心模块
	注意以下选项可以选：
	[*] Forced module unloading
		这个默认是不选的，但是为了防止无法卸载模块（kernel认为卸载该模块是unsafe的，
		force卸载时不会等待任何使用该模块的程序结束使用），可以选上
· block layer		支持块设备层
	注意以下选项可以选：
	Partition Types
	[*] Windows Logical Disk Manager （Dynamic Disk） support
		这个是用于支持LDM，可以选上，参考Documentation/ldm.txt
	IO Schedulers		磁盘伫列的处理方式
· Processor type and features	CPU 的类型与功能选择
	注意以下选项改一下：
	Preemption Model （No Forced Preemption （Server）
	默认是desktop（桌面电脑），我们用于server就选server
	Timer frequency （300 HZ）	kernel针对某个事件立即回应的速度
	默认是desktop的1000HZ，用于server300HZ就够了
· Power management and ACPI options	电源管理功能
· Bus options （PCI etc.）	总线(bus)相关选项
	PCI Stub driver	虚拟化相关模块	
· Executable file formats / Emulations	编译后可执行文件的格式
	<M> IA32 a.out support
	[*] x32 ABI for 64-bit mode	防止有些比较旧的软件，还需要仿真32位的功能
· Networking support	kernel的网络功能
· Device Drivers	各个设备的驱动程序
· File systems	文件系统的支持
· Kernel hacking	kernel骇客
· Security Options	信息安全
· Cryptographic API	密码应用

6. 编译kernel与kernel模块
查看所有可用的编译参数：
# make help
基本功能如下：
	# make vmlinux	未经压缩的kernel
	# make modules	仅kernel模块
	# make bzImage	经压缩过的kernel（默认）
	# make all		进行上述三个动作
依次进行如下操作：
# make -j 4 clean					<==先清除暂存盘
# make -j 4 bzImage					<==先编译核心
# make -j 4 modules					<==再编译模块
# make -j 4 clean bzImage modules	<==连续动作！
注：-j 4意思是让本机上的4个CPU同时进行编译工作（本机上有至少4个CPU（包括超线程））

