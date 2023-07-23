# DnDGPT

# Setup

1. Install [Python](https://www.python.org/downloads/)
1. Using command line of your choice (bash/powershell), navigate to the root of the project directory: `cd .\DnDGPT`
1. Install packages: `py -m pip install -r requirements.txt`
1. (Optional) Generate a secret key: `py -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
1. Setup environment variables by creating a `.env` file, use the `.env.example` as an example for what values are needed
1. Apply migrations: `py manage.py migrate`
1. Start the project: `py manage.py runserver`

# Troubleshoot

- For MacOS, you may have to use `python3` command instead of `py`
