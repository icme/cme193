---
currentMenu: jupyter
---
**note** all commands on this page are invoked from a bash shell (terminal), not from an interactive Python session.

# Jupyter Notebooks

[Jupyter notebooks](https://jupyter.org/) are used to mix code and markdown (for exposition) in a single place.

Jupyter comes bundled with Anaconda, but you can download it for whatever python you are using using `pip` (doens't have to be anaconda python).

From a terminal:
```bash
pip install jupyter
```

Note that Jupyter is **not** Python.  You can use python in a variety of other ways (e.g., through the command line).  Additionally, you can use Jupyter notebooks with other programming languages.

## Launching Jupyter

Once you have Jupyter installed, you can launch a notebook server.

From a terminal:
```bash
jupyter notebook
```

This should launch a notebook server on your computer, and open a tab on your browser.

**Note** You can launch Jupyter from the Anaconda launcher.  This may work, but I advise that you don't rely on the launcher and instead do it from a terminal.

# Using Jupyter with a Conda virutal environment

You don't need to install Jupyter in every virtual environment.  However, you do need to install a `ipykernel` for every virtual environment.

First, you may wish to install `nb_conda`

Next, you need to install an `ipykernel` for your virtual environment.  This looks like the following:

From a terminal:
```bash
conda install nb_conda
source activate cme193 # cme193 virtual env
conda install ipykernel # installs a python kernel for this environment
```

Now, when you launch a Jupyter notebook server (even without your environment activated), you should see a `Python [conda env:cme193]` option in the kernel menu.
