# QA_Auto_2024

## Table Of Contents

* [Description](#description)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Credits](#credits)

## Description

A Python test automation framework created as a pet project during the Automation Software Testing course. The goal behind this framework's creation was to learn the basics of the automation test design using Pytest, SQLite, and Selenium as the main tools. This project includes tests for api (http and database) testing, and UI testing.

## Requirements

To run tests on this framework, you will need to:
- Install the latest **Python** build from the [official website](https://www.python.org/downloads/).
- Install **Pytest** module using this console command:
```
pip3 install pytest -U
```
- Install **Selenium** using this console command:
```
pip3 install selenium --user
```
or
```
sudo pip3 install selenium --user
```
- This project uses Selenium WebDriver for Google Chrome version 115 or newer, which is included in the [drivers folder](/drivers).

## Installation

Clone the repo to your local machine.

## Usage

You can run all the tests by executing `pytest` command in the repo's root directory. For running certain sets of tests, all the automation tests were marked accordingly. For example, to run tests for the GitHub part of the api tests, use this console command:
```
pytest -m github
```
To run the entire UI section, use `pytest -m ui` command, and to run only the tumblr set use `pytest -m tumblr`.

> [!TIP]
> All the valid markers can be found in the [pytest.ini](pytest.ini)

## Credits

The Automation Software Testing course is an e-learning course provided by prometheus.org.ua.
