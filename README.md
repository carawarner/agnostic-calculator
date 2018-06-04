# Agnostic Calculator

![Travis](https://travis-ci.com/carawarner/calculator.svg?token=aYRBXZ7uA2bt85y6RMqu&branch=master)

A Python3 library for evaluating mathematical expressions wheren numbers are not expected to be base-10. 

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

