---
currentMenu: getting_started
---
#Getting started

Getting started with Python can be a little confusing, hopefully this page helps to get you going.

##Installing Python

In this class, we will be using Python 3.6.  If you want to use a different version, you can try, but the material provided in class may not run with your different version.  In particular, if you are using Python 2, you are particularly likely to see things not work.  We recommend having some Python 3 interpreter available.

In the terminal, you can check which python version you are currently using with
```bash
python -V # -V is the same as --version
```
You may have a python 2 interpreter as well as a python 3 interpreter.  Often these can be invoked as
```bash
python2 -V # python 2 version
python3 -V # python 3 version
```

Following are a variety of methods you can use to install Python.  As far as this course is concerned, you can use whatever you want (if you already have system python or anaconda working for you, don't change just for the course).

If you are new to Python, I recommend using Anaconda, regardless of operating system.  You can always change your mind later.  [Conda environments](https://conda.io/docs/user-guide/tasks/manage-environments.html) are enough of a reason to at least give it a try.

###Homebrew (Mac only)

If you want a bit more control over your Python distribution, then using Homebrew to install Python is useful.

It also installs the package manager *pip* for you, which is very useful.

However, it does not come with additional modules, such as *numpy* or *scipy*,
though they can be installed easily using *pip*.

A short tutorial can be found [here](http://docs.python-guide.org/en/latest/starting/install/osx/).

###Anaconda

One convenient method to set up your Python environment is using a free, pre-packaged distribution, such as [Anaconda](https://www.anaconda.com/download/).

This has the advantage that many relevant packages come pre-installed, possibly saving you some headaches later on. It also includes *pip*, the Python package manager.

Note that while Anaconda also comes with the Anaconda launcher and a bunch of other tools, you should not be using any of these for this course.
We only use Anaconda for the convenience of installation of Python and the main packages, not the other stuff that comes with it as well.

If you are a Windows user, Anaconda is recommended, as Windows is notorious for not playing nice with Python.

### System Package Manager (Linux)

If you're running Linux, you can just use your package manager (*apt-get*, *dnf*, etc.) to install Python. You can also often use your package manager to install Python packages instead of *pip*, but you may run into issues doing this.

##Editor

To write code, you need an editor.
While there are many options, old and new, [Atom](https://atom.io/) is (generally) what I use.

A script is a simple file with text, such as

```python
a = 'Hello,'
b = 'world!'
print a + ' ' + b
```

which you can save to your *filesystem* using the editor.

##Running code

Now that you know how to write Python scripts, it's time to learn how to run them using Python.

###Mac

Open the *terminal*, for example by searching for terminal using the spotlight search function.

To open the interpreter, simply enter *python* (this is the interactive mode).

To run a script, navigate to the folder that contains your script. Then simply run `python script.py`, given that `script.py` is the name of your script.

Online, you can find some good resources that introduce the terminal, such as
* [How to Use Terminal: The Basics](http://mac.appstorm.net/how-to/utilities-how-to/how-to-use-terminal-the-basics/)
* [Navigating the Terminal: A Gentle Introduction](http://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855)
* [25 Terminal Tips Every Mac User Should Know](http://www.maclife.com/article/feature/25_terminal_tips_every_mac_user_should_know)
* [Getting started with Linux, Section 3 and beyond](http://jolts.stanford.edu/48/getting_started_with_linux) (Note that Linux and Mac have the same terminal)
* [Stanford course CS 1U 'Practical Unix'](https://practicalunix.org/)

###Windows

Open the *command prompt* by searching for `cm`+ in the Start menu.
This is the Windows version of the terminal.

To open the interpreter, similar to the Mac terminal, we simply run +python+.

To run a script, navigate to the folder that contains your script, and then run `python script.py`, given that `script.py` is the file name.

For Windows, there are some good resources about the command prompt

* [Command Prompt Basics - A Getting Started Guide](http://dosprompt.info/)
* [Windows Command Prompt in 15 Minutes](http://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html)

If you are using Windows and you're having trouble setting up Python, I recommend using Python *in the cloud*, as I'll discuss later.

##Pip

To install new modules, make sure you have `pip` installed.
It comes with both Anaconda and Homebrew, so if you have used either of them, you are good.
Otherwise, it is also rather straightforward to install `pip`: See the [documentation](http://pip.readthedocs.org/en/latest/installing.html).

Then, open the terminal / command prompt, and run `pip install module`, where `module` is the name of the module.

**Note that you cannot run this from inside the Python interpreter.**

##Python in the cloud

When you have trouble getting Python up and running, or if you have Windows and
would like to use a Unix environment, then there is an alternative: using your browser.
There are several possibilities, but to be on the same page, I suggest you use [c9.io Cloud 9].
Cloud 9 will host your development environment on the cloud for free.

Please create an account at [Cloud 9](http://c9.io) if you are not able to run Python locally,
so you can at least get started.

##Windows Users

If you are a Windows user and are serious about taking this *and* other computer classes, I recommend using the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).  In general, much scientific computing is done on clusters running some form of Linux.  The sooner you start using Linux, the better.

If the install guides for Anaconda fail, and some Googling leads to nothing of utility, I highly suggest running with a cloud-based option.

##Farmshare
Another option available to everyone is [farmshare](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/Main_Page). You simply need to `ssh` in, and you will have a full working installation of python. This requires some Linux skills, so follow [this guide](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/User_Guide) to getting started.
