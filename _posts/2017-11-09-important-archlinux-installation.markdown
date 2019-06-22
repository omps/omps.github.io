---
layout: post
title: "arch linux setup"
date: 2017-11-09
category: linux
tags: arch, linux, hdisk, mutlilaptop
comments: true
published: true
---

Found a old compaq laptop from previous life, this may be 8/10 years old. The laptop came with a working motherboard and a failed battery. Everything worked fine except the OS is not getting detected and the harddisk was with corrupt sectors. I happen to swap my Thinkpad 500GB IDE harddisk with an 120 GB SSD one. All the day tried to get multiple oses installing on to the USB drive and tried to boot the laptop with those multiple oses.

I choose to move ahead with damnsmall linux. After making a bootable ISO from the downloaded ISO image the particular version disappointed me by not only booting. Then went with puppylinux, issue is something similar, after searching for files it ended up in the pause state. Sorry, i missed to take the screenshot but yeah that happened for real. finally frustated tried my luck with Arch Linux and I must say it just booted up as if this is as normal as anything. THough I was surpriesed I had work to finish which is to make this OS work again. After going ahead and booting with arch ISO i figured out that the laptop has got a bad disk. Well all this RND took significant time of my day. Finally realized I had an old working arch installed disk which was previously taken from my THiinkpad and kept in store. Decided to make use of it. After another 30 minutes and and some hardware time finally got my disk detcted with this laptop.

After the disk is detected the OS decided not to boot up. since it was arch I was pretty sure I will be getting all the issues fixed. Started to boot arch in the failsafe mode. the Failsafe mode worked pretty fine. Now this boosted my confidence I was sure the system is going to work, though this is going to take a little while. But somehow got the system booted. The issue with normal boot was the initramfs was not able to detect my disk or partitions and was failing with "unknown root disk error".

After doing extensive search on google from my mobile, i did figured it out that I may need to reinstall the grub re-create its configuration file.

so here i did it.
```
# grub-install --target=i386-pc /dev/sdx
```

do a grub mkconfig and generate a ```grub.cfg```:
```
# grub-mkconfig -o /boot/grub/grub.cfg
```

So even after doing all this the erros persisted.

It seems I need to regenrate the initramfs

By using the default configration as per the ```/etc/mkinitcpio.conf``` regenerated the initramfs. 
```
# mkinitcpio -g /boot/linux-custom2.img -k 3.3.0-ARCH
```

Incase if you happen to change or use an alternate configuration make a copy to the configuration file and use.
```
# mkinitcpio -c /etc/mkinitcpio-custom.conf -g /boot/linux-custom.img
```

Well made some changes in grub.cfg file to use this new initramfs. 

rebooted the system and voilla all worked well in the default mode.

Now comes another challenging task. Being this a dell laptop it has some propriteory wireless lan card which is not being loaded at the boot time. Arch Linux wiki suggested to install some packages, since the device is not having any network I had to think how to do it. I thought downloading on one machine and copying to another but that would be a tedious task. I need to go everytime back to download dependecies and come back and copy and install in this laptop. A simpler approach is to connect over the LAN. sadly i did not have a lan cable available with me, now this again left me in vain, after so much effort setting everything up now feeling some solution to get the wireless drivers installed and make internet work.

So finally after puutting a lot of thought did the most usual thing connected my android  device on the Laptop and did a USB tethering. Steps are indeed simple, but writing again for my notes.

1. Connect your android device with your laptop USB port.
2. Enable USB tethering on the device.
3. Do a IP link show to identify the new device.
4. The name of the device should be en0sp2xxxx
5. run a dhcpcd <devicename> to configure and bring it up with DHCP.

A good documentation for same can be found here https://wiki.archlinux.org/index.php/android_tethering


Once the tethring is done and google is responding to my ping requests.

the next thing to do was configure wireless networking and install the right drivers.


Documetaions for my broadcomm wireless device. https://wiki.archlinux.org/index.php/broadcom_wireless

short way is
1. Identify the drivers
```
$ lspci -vnn -d 14e4: 
```

2. install the drivers.
``` yaourt broadcom-wl ```

3. Reboot the system

4. Do a ip link show to see the newly discovered wireless device.

5. run wifi-menu and connect to internet. (requires sudo)


Note: I am writing this blog from the same compaq notebook.
