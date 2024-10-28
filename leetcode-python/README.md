# Leetcode Solutions implemented in Python

I followed the instructions provided at https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code, then ran:

```bash
pip install pytest
pip install hypothesis
pip install sympy
```

Visual Studio code will use Pytest _or_ Unittest, but not both. I've preferred Pytest
for the more economical parameterized testing it allows. On the minus side, tests have
to be in a file called `test*.py`. Sympy is used for verification in numerical tests.
