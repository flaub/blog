Treating javascript like assembly
#################################

The idea is not new, but it hasn't really caught on yet either. If a browser is
the preferred development environment (for a variety of reasons: cross-platform,
ease-of-deployment, etc), and if javascript engines are getting faster all the
time, why can't our AJAX/web 2.0 applications do anything that platform specific
client apps do. I'm going to posit that it has to do with tools. I don't want to
get into a religious war about javascript (dynamic) vs C#/Java (static), but I
do want to note that as applications begin to scale up in size and complexity,
static languages begin to offer many advantages. It's not really the language
that matters, but the tools and environment that these languages exist in.

Enter the Google Web Tookit (GWT). I believe these folks are on the right track.
They view the browser as just another virtual machine to execute code in. But in
this case, the bytecodes are actually javascript statements and expressions.
Here's the only downside, it is built on Java.

Well how about something for the .NET developers? This is what I can find so
far:

Script#
  This project goes half-way, in that it allows developers to write their client
  code in C#. However, it does nothing to help developers test and debug this
  code, which I believe is required if you want to create complicated AJAX style
  applications.

jsc
  Like Script#, only it is able to convert any .NET assembly into Javascript,
  thereby allowing you to use any .NET language you want. However, no debugging
  environment exists.

Volta
  This sounds promising, but it looks like either MS is trying to turn this into
  a real project, or they pulled the plug (since Sept 8, 2008).

It looks like Volta is what I want, however I don't want to wait. Luckily I've
already got a MSIL -> Javascript converter completed!
