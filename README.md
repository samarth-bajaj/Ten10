# Interest Calculator UI Tests (Selenium + pytest + POM)

Test automation framework for a web Interest Calculator using Selenium and pytest with Page Object Model (POM).

## Stack
- Python + pytest
- Selenium WebDriver (Chrome via Selenium Manager)
- Page Object Model

## Project Structure
```
conftest.py                  # Pytest driver fixture (opens the site in Chrome)
settings.py                  # BASE_URL, USERNAME, PASSWORD for the app
pages/
  __init__.py
  common.py                  # CommonOps
  login_page.py              # LoginPage
  interest_calculator_page.py# InterestCalculatorPage
tests/
  test_interest_calculator.py
pytest.ini                   # Pytest config/markers
requirements.txt             # Dependencies
```

## Setup
1) Create and activate a virtual environment
- Windows (PowerShell)
  - `python -m venv .venv`
  - `.\.venv\Scripts\Activate.ps1`
- macOS/Linux (bash)
  - `python -m venv .venv`
  - `source .venv/bin/activate`

2) Install dependencies
- `pip install -r requirements.txt`

3) Configure the target app and credentials
- Edit `settings.py`:
  - `BASE_URL = "http://3.8.XXX.61"`
  - `USERNAME = "your-email@example.com"`
  - `PASSWORD = "your-password"`

## Running Tests
- Run all tests
  - `pytest`
- Run a single test by node id
  - `pytest tests/test_interest_calculator.py::test_login`
- Run a single parametrized case (e.g., rate 13)
  - `pytest -q tests/test_interest_calculator.py::test_dropdown_rate[13]`

## Page Objects
**CommonOps** (`pages/common.py`)

**LoginPage** (`pages/login_page.py`)

**InterestCalculatorPage** (`pages/interest_calculator_page.py`)

## Tests Included
- Login
- Dropdown options present (parametrized)
- Dropdown selection updates label (parametrized)
- Interest calculation triggers
- Interest validation (to 2 decimals)
- Consent negative
