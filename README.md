# DnDGPT

# Setup
1. Install [Python](https://www.python.org/downloads/)
2. Setup environment variables by creating a `.env` file, use the `.env.example` as an example for what values are needed
3. Using command line of your choice (bash/powershell), navigate to the root of the project directory: `cd .\DnDGPT`
4. Install packages: `py -m pip install -r requirements.txt`
5. Apply migrations: `py manage.py migrate`
6. Start the project: `py manage.py runserver`
