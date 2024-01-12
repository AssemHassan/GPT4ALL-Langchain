# GPT4ALL-Langchain
## pre-requisite
Install Poetry a Python package manager alternative to pip
https://python-poetry.org/docs/#installing-with-the-official-installer

## Install dependencies
If you would like all packages to be installed in local cashe, run
```
> poetry shell

this should start a new enviroenment for poetry and create a virtual env.

To confirm local env is used, list all configrations and look for `virtualenvs.in-project = true`
```
> poetry config --list

Install dependencies
```
> poetry install

## running the app in web interface
```
> streamlit run app.py
