# Lexus Web App Test Automation

## Overview
This repo automates the tests for the following scenarios:

- Verify masthead banner
- Verify video demo/feature section on a vehicle model's page
- Fill a test drive form successfully

## How to set up the framework on your local

🔵 Add <b><a href="https://www.python.org/downloads/">Python</a></b> and <b><a href="https://git-scm.com/">Git</a></b> to your System PATH.

🔵 Using a <a href="https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/virtualenv_instructions.md">Python virtual env</a> is recommended.

### Install the dependencies
After setting up python and a virtual environment you can install the requirements via `requirements.txt`
```bash
pip install -r requirements.txt
```

## How to run the tests
By default, the test runs headless meaning there will be no browser appearing on your local when running the basic test execution script
```bash
pytest -vv
```
 To see a browser execute the test simple run the test with the following CLI command:
```bash
pytest --demo -vv
```