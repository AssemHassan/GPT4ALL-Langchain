# GPT4ALL-Langchain
## pre-requisite
Install Poetry, a Python package manager alternative to pip. For installation instructions, refer to the official installer documentation: [Installing with the official installer](
https://python-poetry.org/docs/#installing-with-the-official-installer)

## Install dependencies
If you would like all packages to be installed in the local cache, run the following command in your terminal:
```shell
 <kbd>$</kbd> poetry shell
```

This command will start a new environment for Poetry and create a virtual environment.

To confirm that the local environment is being used, you can list all configurations and look for `virtualenvs.in-project = true` by running the following command:
 
```shell
$ poetry config --list
```

To install the dependencies, run the following command:
```shell
$ poetry install
```

## running the app in web interface
To run the app in the web interface, use the following command:

```shell
$ streamlit run app.py
```
