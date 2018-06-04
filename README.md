# Agnostic Calculator

![Travis](https://travis-ci.com/carawarner/agnostic-calculator.svg?branch=master) [![PyPI version](https://badge.fury.io/py/agnostic-calculator.svg)](https://badge.fury.io/py/agnostic-calculator)

A Python3 library that parses strings representing mathematical expressions. The `Calculator` takes a `converter` by which means you can specify numerical types other than regular base 10 numbers. There is one converter available: `roman`.

## How to install

_Using pip_:

```
pip install agnostic-calculator
```

_Manually_:
```
git clone git@github.com:carawarner/calculator.git
cd calculator/calculator
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to run tests

This libary uses [pytest](https://docs.pytest.org/en/latest/), a powerful but lightweight testing tool for Python.

```
cd calculator
pytest
```

## How to use

WARNING: Don't use `agnostic-calculator` in production. The calculator library calls Python's `eval()` on user input. **It's not safe.**

```python
from calculator.calculator import Calculator
import calculator.converters.roman as converter

calculator = Calculator(converter)
result = calculator.evaluate(expression)
```

