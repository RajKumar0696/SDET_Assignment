# SDET_Assignment

This repository has automation testing for a webapp

# Tech Stack
1. Python
2. Selenium Webdriver
3. Pytest
4. Page Object Model
5. Hybrid framework
# Prerequisites

* python 3.7.X
* pip and setuptools
* [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment:~:text=Installing%20virtualenv%C2%B6)

# Installation

1. Download or clone the repository 
2. Open a terminal
3. Go to the project root directory "/SDET_Assignment/".
4. Create a virtual environment for your OS: [create venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment:~:text=Creating%20a%20virtual%20environment%C2%B6)
5. Activate the virtual environment for your OS: [activate venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment:~:text=Activating%20a%20virtual%20environment%C2%B6)
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`

# Test Execution

1. Open a terminal
2. From the project root directory run: 

    `pytest -v --capture=tee-sys  --html=Reports/report.html`

# Configuration

By default, tests will be executed in Chrome (normal mode).

# Results

To check the report, open the '/Reports/report.html' file once the execution has finished.

   
   