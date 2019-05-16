---
currentMenu: getting_started
---
#Getting started

In this class, we will mostly be using Jupyter Notebook to run Python code. Jupyter Notebook stores Python code in *notebooks*, which have the `.ipynb` extension. The lectures will be provided this way so that you can follow along during lecture (see the syllabus page to download them).

There are two ways to run these notebooks: locally or in the cloud. Although it's easier to get started with Python in the cloud, I recommend you install Python and Jupyter Notebook locally. This is because eventually you'll want to customize your Python installation (for example, installing packages for your coursework/research), which is much easier with a local installation.

## Running notebooks locally
The simplest way to get started on your own computer is to install [Anaconda](https://www.anaconda.com/distribution/). In this class, we will use Python 3.7. Installing Anaconda will install Python, Jupyter Notebook, as well as some common packages common in scientific computing.

Once Anaconda is installed, you can test your installation by opening Terminal on Mac and Linux or the Anaconda Prompt on Windows and running the following command:
```bash
python -V
```
The output should give the current version of Python (3.7 if all goes well).

To launch Jupyter Notebook, from the same terminal, run:
```bash
jupyter notebook
```
This should either pop open the Jupyter Notebook interface in your web browser. If it doesn't pop up immediately, look at the output of the command and find the URL beginning with `http://` and copy-paste that into your web browser. Use the web interface to navigate to the notebook (`.ipynb` file) that you want to open, and click it to launch the notebook.

To execute Python code inside a cell, click on the cell and press Ctrl-Enter (or Cmd-Enter on Mac). To insert a new cell, press B, or click Insert > Insert Cell Below in the menu at the top.

## Running notebooks in the cloud
Google provides a service called [Colab](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true) that allows you to run notebooks in your browser without any prior setup, sort of like Google Docs but for Python notebooks. Typically, I will also provide links to shared Colab notebooks (in addition to the `.ipynb` files). Simply click the link, and click "Open in Playground" in the top left to launch the notebook.

To execute Python code inside a cell, click on the cell and press Ctrl-Enter (or Cmd-Enter on Mac). To insert a new cell, click the button labelled "+ Code" in the top left.
