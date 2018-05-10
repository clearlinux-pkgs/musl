#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x56BCDB593020450F (musl@libc.org)
#
%define keepstatic 1
Name     : musl
Version  : 1.1.19
Release  : 14
URL      : https://www.musl-libc.org/releases/musl-1.1.19.tar.gz
Source0  : https://www.musl-libc.org/releases/musl-1.1.19.tar.gz
Source99 : https://www.musl-libc.org/releases/musl-1.1.19.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: musl-bin
Requires: musl-lib
Patch1: 0001-Don-t-use-cross-compile-ar-or-ranlib.patch

%description
musl libc
musl, pronounced like the word "mussel", is an MIT-licensed
implementation of the standard C library targetting the Linux syscall
API, suitable for use in a wide range of deployment environments. musl
offers efficient static and dynamic linking support, lightweight code
and low runtime overhead, strong fail-safe guarantees under correct
usage, and correctness in the sense of standards conformance and
safety. musl is built on the principle that these goals are best
achieved through simple code that is easy to understand and maintain.

%package bin
Summary: bin components for the musl package.
Group: Binaries

%description bin
bin components for the musl package.


%package dev
Summary: dev components for the musl package.
Group: Development
Requires: musl-lib
Requires: musl-bin
Provides: musl-devel

%description dev
dev components for the musl package.


%package lib
Summary: lib components for the musl package.
Group: Libraries

%description lib
lib components for the musl package.


%prep
%setup -q -n musl-1.1.19
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519394405
%configure  --target=x86_64-generic-linux --prefix=/usr/lib64/musl --exec-prefix=/usr --includedir=/usr/lib64/musl/include --libdir=/usr/lib64/musl/lib64
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1519394405
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/lib/ld-musl-x86_64.so.1
/usr/lib64/musl/lib64/Scrt1.o
/usr/lib64/musl/lib64/crt1.o
/usr/lib64/musl/lib64/crti.o
/usr/lib64/musl/lib64/crtn.o
/usr/lib64/musl/lib64/libc.a
/usr/lib64/musl/lib64/libcrypt.a
/usr/lib64/musl/lib64/libdl.a
/usr/lib64/musl/lib64/libm.a
/usr/lib64/musl/lib64/libpthread.a
/usr/lib64/musl/lib64/libresolv.a
/usr/lib64/musl/lib64/librt.a
/usr/lib64/musl/lib64/libutil.a
/usr/lib64/musl/lib64/libxnet.a
/usr/lib64/musl/lib64/musl-gcc.specs
/usr/lib64/musl/lib64/rcrt1.o

%files bin
%defattr(-,root,root,-)
/usr/bin/musl-gcc

%files dev
%defattr(-,root,root,-)
/usr/lib64/musl/include/aio.h
/usr/lib64/musl/include/alloca.h
/usr/lib64/musl/include/ar.h
/usr/lib64/musl/include/arpa/ftp.h
/usr/lib64/musl/include/arpa/inet.h
/usr/lib64/musl/include/arpa/nameser.h
/usr/lib64/musl/include/arpa/nameser_compat.h
/usr/lib64/musl/include/arpa/telnet.h
/usr/lib64/musl/include/arpa/tftp.h
/usr/lib64/musl/include/assert.h
/usr/lib64/musl/include/bits/alltypes.h
/usr/lib64/musl/include/bits/endian.h
/usr/lib64/musl/include/bits/errno.h
/usr/lib64/musl/include/bits/fcntl.h
/usr/lib64/musl/include/bits/fenv.h
/usr/lib64/musl/include/bits/float.h
/usr/lib64/musl/include/bits/hwcap.h
/usr/lib64/musl/include/bits/io.h
/usr/lib64/musl/include/bits/ioctl.h
/usr/lib64/musl/include/bits/ioctl_fix.h
/usr/lib64/musl/include/bits/ipc.h
/usr/lib64/musl/include/bits/limits.h
/usr/lib64/musl/include/bits/link.h
/usr/lib64/musl/include/bits/mman.h
/usr/lib64/musl/include/bits/msg.h
/usr/lib64/musl/include/bits/poll.h
/usr/lib64/musl/include/bits/posix.h
/usr/lib64/musl/include/bits/reg.h
/usr/lib64/musl/include/bits/resource.h
/usr/lib64/musl/include/bits/sem.h
/usr/lib64/musl/include/bits/setjmp.h
/usr/lib64/musl/include/bits/shm.h
/usr/lib64/musl/include/bits/signal.h
/usr/lib64/musl/include/bits/socket.h
/usr/lib64/musl/include/bits/stat.h
/usr/lib64/musl/include/bits/statfs.h
/usr/lib64/musl/include/bits/stdint.h
/usr/lib64/musl/include/bits/syscall.h
/usr/lib64/musl/include/bits/termios.h
/usr/lib64/musl/include/bits/user.h
/usr/lib64/musl/include/byteswap.h
/usr/lib64/musl/include/complex.h
/usr/lib64/musl/include/cpio.h
/usr/lib64/musl/include/crypt.h
/usr/lib64/musl/include/ctype.h
/usr/lib64/musl/include/dirent.h
/usr/lib64/musl/include/dlfcn.h
/usr/lib64/musl/include/elf.h
/usr/lib64/musl/include/endian.h
/usr/lib64/musl/include/err.h
/usr/lib64/musl/include/errno.h
/usr/lib64/musl/include/fcntl.h
/usr/lib64/musl/include/features.h
/usr/lib64/musl/include/fenv.h
/usr/lib64/musl/include/float.h
/usr/lib64/musl/include/fmtmsg.h
/usr/lib64/musl/include/fnmatch.h
/usr/lib64/musl/include/ftw.h
/usr/lib64/musl/include/getopt.h
/usr/lib64/musl/include/glob.h
/usr/lib64/musl/include/grp.h
/usr/lib64/musl/include/iconv.h
/usr/lib64/musl/include/ifaddrs.h
/usr/lib64/musl/include/inttypes.h
/usr/lib64/musl/include/iso646.h
/usr/lib64/musl/include/langinfo.h
/usr/lib64/musl/include/lastlog.h
/usr/lib64/musl/include/libgen.h
/usr/lib64/musl/include/libintl.h
/usr/lib64/musl/include/limits.h
/usr/lib64/musl/include/link.h
/usr/lib64/musl/include/locale.h
/usr/lib64/musl/include/malloc.h
/usr/lib64/musl/include/math.h
/usr/lib64/musl/include/memory.h
/usr/lib64/musl/include/mntent.h
/usr/lib64/musl/include/monetary.h
/usr/lib64/musl/include/mqueue.h
/usr/lib64/musl/include/net/ethernet.h
/usr/lib64/musl/include/net/if.h
/usr/lib64/musl/include/net/if_arp.h
/usr/lib64/musl/include/net/route.h
/usr/lib64/musl/include/netdb.h
/usr/lib64/musl/include/netinet/ether.h
/usr/lib64/musl/include/netinet/icmp6.h
/usr/lib64/musl/include/netinet/if_ether.h
/usr/lib64/musl/include/netinet/igmp.h
/usr/lib64/musl/include/netinet/in.h
/usr/lib64/musl/include/netinet/in_systm.h
/usr/lib64/musl/include/netinet/ip.h
/usr/lib64/musl/include/netinet/ip6.h
/usr/lib64/musl/include/netinet/ip_icmp.h
/usr/lib64/musl/include/netinet/tcp.h
/usr/lib64/musl/include/netinet/udp.h
/usr/lib64/musl/include/netpacket/packet.h
/usr/lib64/musl/include/nl_types.h
/usr/lib64/musl/include/paths.h
/usr/lib64/musl/include/poll.h
/usr/lib64/musl/include/pthread.h
/usr/lib64/musl/include/pty.h
/usr/lib64/musl/include/pwd.h
/usr/lib64/musl/include/regex.h
/usr/lib64/musl/include/resolv.h
/usr/lib64/musl/include/sched.h
/usr/lib64/musl/include/scsi/scsi.h
/usr/lib64/musl/include/scsi/scsi_ioctl.h
/usr/lib64/musl/include/scsi/sg.h
/usr/lib64/musl/include/search.h
/usr/lib64/musl/include/semaphore.h
/usr/lib64/musl/include/setjmp.h
/usr/lib64/musl/include/shadow.h
/usr/lib64/musl/include/signal.h
/usr/lib64/musl/include/spawn.h
/usr/lib64/musl/include/stdalign.h
/usr/lib64/musl/include/stdarg.h
/usr/lib64/musl/include/stdbool.h
/usr/lib64/musl/include/stdc-predef.h
/usr/lib64/musl/include/stddef.h
/usr/lib64/musl/include/stdint.h
/usr/lib64/musl/include/stdio.h
/usr/lib64/musl/include/stdio_ext.h
/usr/lib64/musl/include/stdlib.h
/usr/lib64/musl/include/stdnoreturn.h
/usr/lib64/musl/include/string.h
/usr/lib64/musl/include/strings.h
/usr/lib64/musl/include/stropts.h
/usr/lib64/musl/include/sys/acct.h
/usr/lib64/musl/include/sys/auxv.h
/usr/lib64/musl/include/sys/cachectl.h
/usr/lib64/musl/include/sys/dir.h
/usr/lib64/musl/include/sys/epoll.h
/usr/lib64/musl/include/sys/errno.h
/usr/lib64/musl/include/sys/eventfd.h
/usr/lib64/musl/include/sys/fanotify.h
/usr/lib64/musl/include/sys/fcntl.h
/usr/lib64/musl/include/sys/file.h
/usr/lib64/musl/include/sys/fsuid.h
/usr/lib64/musl/include/sys/inotify.h
/usr/lib64/musl/include/sys/io.h
/usr/lib64/musl/include/sys/ioctl.h
/usr/lib64/musl/include/sys/ipc.h
/usr/lib64/musl/include/sys/kd.h
/usr/lib64/musl/include/sys/klog.h
/usr/lib64/musl/include/sys/mman.h
/usr/lib64/musl/include/sys/mount.h
/usr/lib64/musl/include/sys/msg.h
/usr/lib64/musl/include/sys/mtio.h
/usr/lib64/musl/include/sys/param.h
/usr/lib64/musl/include/sys/personality.h
/usr/lib64/musl/include/sys/poll.h
/usr/lib64/musl/include/sys/prctl.h
/usr/lib64/musl/include/sys/procfs.h
/usr/lib64/musl/include/sys/ptrace.h
/usr/lib64/musl/include/sys/quota.h
/usr/lib64/musl/include/sys/reboot.h
/usr/lib64/musl/include/sys/reg.h
/usr/lib64/musl/include/sys/resource.h
/usr/lib64/musl/include/sys/select.h
/usr/lib64/musl/include/sys/sem.h
/usr/lib64/musl/include/sys/sendfile.h
/usr/lib64/musl/include/sys/shm.h
/usr/lib64/musl/include/sys/signal.h
/usr/lib64/musl/include/sys/signalfd.h
/usr/lib64/musl/include/sys/socket.h
/usr/lib64/musl/include/sys/soundcard.h
/usr/lib64/musl/include/sys/stat.h
/usr/lib64/musl/include/sys/statfs.h
/usr/lib64/musl/include/sys/statvfs.h
/usr/lib64/musl/include/sys/stropts.h
/usr/lib64/musl/include/sys/swap.h
/usr/lib64/musl/include/sys/syscall.h
/usr/lib64/musl/include/sys/sysinfo.h
/usr/lib64/musl/include/sys/syslog.h
/usr/lib64/musl/include/sys/sysmacros.h
/usr/lib64/musl/include/sys/termios.h
/usr/lib64/musl/include/sys/time.h
/usr/lib64/musl/include/sys/timeb.h
/usr/lib64/musl/include/sys/timerfd.h
/usr/lib64/musl/include/sys/times.h
/usr/lib64/musl/include/sys/timex.h
/usr/lib64/musl/include/sys/ttydefaults.h
/usr/lib64/musl/include/sys/types.h
/usr/lib64/musl/include/sys/ucontext.h
/usr/lib64/musl/include/sys/uio.h
/usr/lib64/musl/include/sys/un.h
/usr/lib64/musl/include/sys/user.h
/usr/lib64/musl/include/sys/utsname.h
/usr/lib64/musl/include/sys/vfs.h
/usr/lib64/musl/include/sys/vt.h
/usr/lib64/musl/include/sys/wait.h
/usr/lib64/musl/include/sys/xattr.h
/usr/lib64/musl/include/syscall.h
/usr/lib64/musl/include/sysexits.h
/usr/lib64/musl/include/syslog.h
/usr/lib64/musl/include/tar.h
/usr/lib64/musl/include/termios.h
/usr/lib64/musl/include/tgmath.h
/usr/lib64/musl/include/threads.h
/usr/lib64/musl/include/time.h
/usr/lib64/musl/include/uchar.h
/usr/lib64/musl/include/ucontext.h
/usr/lib64/musl/include/ulimit.h
/usr/lib64/musl/include/unistd.h
/usr/lib64/musl/include/utime.h
/usr/lib64/musl/include/utmp.h
/usr/lib64/musl/include/utmpx.h
/usr/lib64/musl/include/values.h
/usr/lib64/musl/include/wait.h
/usr/lib64/musl/include/wchar.h
/usr/lib64/musl/include/wctype.h
/usr/lib64/musl/include/wordexp.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/musl/lib64/libc.so
