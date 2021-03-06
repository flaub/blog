Multiple hard disks in Parallels
################################

So I have this USB drive that I have with a bunch of WinXP apps on it. In fact,
the drive is formatted as NTFS. Mac doesn't have a problem mounting it on its
own; I've got the NTFS-3G driver for that. Parallels can actually see this
drive, but the ordering has to be just right. What I mean is that when you
startup Parallels, you can't have the USB drive plugged in, even if OS X has it
unmounted. This is because the default setup and UI for Parallels is silly and
can't understand that you have more than one *real* hard disk. So there are two
options for working around this problem:

Approach one, ordering
----------------------

 #. Startup Parallels
 #. Now plugin the USB drive
 #. Unmount the drive from OS X
 #. Associate the USB drive with Parallels by going to USB/Devices/USB2.0 Storage Device (YMMV).

Approach two, config file hackery
---------------------------------

The trick with this is that the config file (.pvs) for your virtual machine is
actually capable of dealing with multiple hard disks. For some reason, the
Parallels UI team decided not to expose this functionality. So, we'll have to
manually edit the .pvs file. What we need to do is make a set of entries like
this:

::

  [IDE Devices]
  Disk 0:0 = 1
  Disk 0:0 enabled = 1
  Disk 0:0 media = 1
  Disk 0:0 connected = 1
  Disk 0:0 image = Boot Camp;disk0s3
  Disk 0:0 cylinders = 0
  Disk 0:0 heads = 0
  Disk 0:0 sectors = 0
  
  Disk 1:1 = 1
  Disk 1:1 enabled = 1
  Disk 1:1 media = 1
  Disk 1:1 connected = 1
  Disk 1:1 image = Boot Camp;disk1s1
  Disk 1:1 cylinders = 0
  Disk 1:1 heads = 0
  Disk 1:1 sectors = 0

Notice that we are using the 'Boot Camp' style image. The value after the
semicolon is actually the device identifier for the partition that you want the
virtual machine to mount. You can get this by running @diskutil list@. So, your
partition might actually live somewhere else (be careful of this). Also notice,
that we have to specifically modify the Disk 0:0 image line to specify where the
first HDD is at. If you don't do this, starting up Parallels will freak out
saying there is more than one Boot Camp disk (which is apparently unsupported).
Also, we are attaching this secondary drive to IDE channel 1:1, so you might
have to change this if you've already got a CD-ROM drive or something mapped to
it.

Be careful, if you don't understand what partitions are, you should probably
steer clear of this. In any case, use this at your own risk!