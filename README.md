# API test automation framework with Python for Membership Api

## Setup

```zsh
# Activate virtualenv
pipenv shell
# Install all dependencies in your virtualenv
pipenv install
```

## Application under test
Swagger: https://app-membershipapi-test.azurewebsites.net/swagger/index.html

## How to run

```zsh
# Launch pipenv
pipenv shell

# Install all packages
pipenv install

# Run tests via pytest (single threaded)
python -m pytest

# Run tests in parallel
python -m pytest -n auto

# Run tests in selected environments: test, qa, test_rs, qa_rs
python -m pytest --env test

# Report results to report portal Allure
python -m pytest -n auto --alluredir=report_allure/

# Run Allure report
allure serve report_allure/
```


NOTES to incorporate in the framework. 
Will be deleted
# Env Viriables environ
# single assertions vs multiple
# if statement and combination in the final assertion. Create and violations in JSON for each assertion.
# check more complicate tool for errors and assertion

# Work with Antonio about project structure
# Objet enheritense for future use
# Comprehensiveness - data generators
# returns - returns vs yield (help to continue (not like break - return))
# fixtures - pytest concepts  - all that my test needs
# Markers concept - Labeling
# decorators approach
# axe python for accessibility testing
# multiple assertions call a method to save results of assertion as dict or array. log the error data
