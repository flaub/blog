New development environment
###########################

:date: 2007-12-13

Today is the first day I'm actually sitting down with Visual Studio again. It's
my first time using the new 2008 version. It doesn't seem to like boost, gotta
figure out what to do about that. Found a neat tool called SharpKeys so that I
could remap the right apple-key to the left-windows key. Then I disabled the
left-windows key. Now I can use coherence and switch between Mac OS X and
Windows XP tasks using apple-tab and not have the stupid Windows Start Menu
popup everytime!

Having trouble using boost with VC9. It looks like it can't figure out which
compiler it is. Looking into it... OK, fixed, added the following to
``<boost/config/compiler/visualc.hpp>``

line 156:

.. code-block:: c++

  # elif _MSC_VER == 1500
  # define BOOST_COMPILER_VERSION 9.0

then line 172 should be:

.. code-block:: c++

  #if (_MSC_VER > 1500)

Found out some handy new keyboard shortcuts for VC++:
 - CTRL+SHIFT+G: Opens document when path is under the cursor
Made my own customizations:
 - CTRL+SHIFT+K: Customize keyboard
 - CTRL+SHIFT+D: Edit.GoToDefinition
 - CTRL+SHIFT+E: Edit.GoToDeclaration

My fingers almost never leave the keyboard now!


Great reference for Visual Studio tips!

http://www.catch22.net/tuts/vctips.asp
