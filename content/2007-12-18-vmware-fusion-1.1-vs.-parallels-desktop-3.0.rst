VMWare Fusion 1.1 vs. Parallels Desktop 3.0
###########################################

I've been using Parallels ever since it first came out. I've been very pleased
with the ability to run the 3 or 4 Windows applications that I use without
having to reboot out of OS X. The cost is acceptable because performance
degradation is not very noticeable, especially considering that virtualized
applications still run faster than my desktop PC.

Even with Parallels version 3.0, there are some major issues that prompted me to
try VMWare Fusion again; I had tried betas in the past and was hopeful that
their RTM would be solid. The biggest problem with Parallels is keyboard
handling. The big show-stopper was the F11 key not functioning properly. This is
a huge problem for me since I use Visual Studio on a regular basis. F11 and
Shift-F11 are used for debugging, specifically to 'step into' and 'step out of'
functions. I was able to finally get F11 with hints from the following:

 - `Anyone using Visual Studio in Parallels`_
 - `Parallels Support Forum`_

But this one I didn't try yet:

 - `Enable access for assistive devices`_

I also saw reports_ that even the pre-release of Fusion was performing better
than Parallels. So, I just downloaded the 30-day evaluation of Fusion; I'm
pleased!

First off, the keyboard works perfectly with Fusion. But it didn't come without
its own set of problems. It was an extremely easy migration from Parallels to
Fusion. I think the reason for this, in my case, is that I'm running my VM on
the Boot Camp partition; no need for any kind of conversions. However, when I
first booted in my Windows XP guest from Fusion, I couldn't enter my password
into the login dialog box. In fact, the keyboard was completely unresponsive.
Apparently this is a `known issue`_ by the VMWare folks. It turns out that I was
running an app in the background that was using the `SecureInput API`_, which is
also used by Fusion to process keyboard input. The problem is that many Mac OS X
apps don't use this interface correctly, as was the case with `Last.fm`_, which
I had running in the background. Apple recommends that apps `play nicely`_ with
each other. So, as soon as I killed Last.fm, my keyboard worked perfectly inside
the guest. Problem #1 solved.

Next I wanted to see if their 'Unify' functionality was similar to the
'Coherence' mode that Parallels offers. I must say, given that this is VMWare's
first foray into VMs on the Mac at least, they seem to be just as far along (if
not more so) as 3rd version of Parallels. This is probably due to VMWare's long
running experience with VM technology in general. I would imagine that porting
their system to the Mac wasn't as hard as Parallels having to develop it from
scratch. So Unify works great, except for a few nitpicks.

I use QuickSilver_ to enable me to launch applications very quickly.
Unfortunately, I was not able to get this to work nicely for launching Windows
applications as I did with Parallels. One of the nice things Parallels does is
export all of the Windows applications that it finds within the guest as a set
of aliases in a directory on the host. This allows me to make a custom catalog
in QuickSilver to point to this directory. Unify has a nice little Launch
window, by using Cmd-L, but this just isn't as fast as QuickSilver. Also, I
found that getting to the Start Menu is sometimes necessary. I don't want to
have the Windows task-bar shown; I prefer the Mac dock. I have trouble trying to
get to the Start Menu quickly from a 'Unify'-ed running app.

Aside from a few other minor gripes, I'd have to say Fusion is looking in good
shape right now. Performance does seem to be a bit better, AND the guest
actually has access to both cores! I have yet to determine whether this is
actually better or not. It's possible that letting the guest use both cores will
actually degrade overall performance because the context switching overhead is
most assuredly more expensive for virtual-threads than for native ones.

So for now, I'm using Fusion in full-screen mode. All is well, let's see how
long that lasts.

.. _Anyone using Visual Studio in Parallels: http://weblogs.asp.net/jeff/archive/2006/07/20/Anyone-using-Visual-Studio-in-Parallels-on-a-MacBook-Pro_3F00_.aspx
.. _Parallels Support Forum: http://forum.parallels.com/showthread.php?t=18198
.. _Enable access for assistive devices: http://forum.parallels.com/archive/index.php/t-6546.html
.. _reports: http://www.iunknown.com/2007/06/vmware_fusion_r.html
.. _known issue: http://communities.vmware.com/message/616384#616384
.. _SecureInput API: http://developer.apple.com/documentation/Carbon/Reference/Carbon_Event_Manager_Ref/Reference/reference.html#//apple_ref/c/func/EnableSecureEventInput,
.. _Last.fm: http://www.last.fm/
.. _play nicely: http://developer.apple.com/technotes/tn2007/tn2150.html
.. _QuickSilver: http://en.wikipedia.org/wiki/Quicksilver_%28software%29