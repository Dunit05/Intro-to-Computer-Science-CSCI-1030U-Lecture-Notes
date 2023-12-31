# Intro-to-Computer-Science-CSCI-1030U-Lecture-Notes

Here you will find all the in-class lecture code that we go over. This repository is a comprehensive collection of code examples, projects, and exercises designed to complement the material covered in the intro to computer science lectures.

## References/Tools

- [Python](https://www.python.org/)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
- [Textbook](https://runestone.academy/runestone/books/published/thinkcspy/index.html)

### Classes (Declaration)

- Public: `class ClassName:`
- Private: `class __ClassName:`
- Protected: `class _ClassName:`

## Folder Structure

The workspace contains folders labeled by `date (name)` by default, where:

- `Notes`: the folder contains the days lecture notes, with an executable jupyter notebook file `index.ipynb`. (Code examples are broken down into sections and can be run individually)
- `Exercises`: the folder contains the days exercises, with an executable python files `(exerciseName).py`.

## Getting Started

Clone any repository to your local machine using the following command in Windows:

```
git clone (url)
cd (folder name)
```

You can use this equivalent command in Linux or MacOS:

```
git clone (url)
cd (folder name)
```

Install pytest, which is a module for Python that allows you to verify that your code is correct before you submit, using the following command in Windows:

```
pip install pytest
pip install pytest-cov
```

You can use this equivalent command in Linux or MacOS:

```
sudo -H pip3 install pytest
sudo -H pip3 install pytest-cov
```

If you have previously installed `pytest`, then you can skip this step.

## Adding test files

To add a test file, you can create a test file using the naming convention `test_*.py` or `*_test.py`. For example, if you have a file called `my_file.py`, then you can create a test file called `test_my_file.py` or `my_file_test.py`.

## Running the Tests

To run the tests, you can use the following command in Windows:

`pytest`

You can use this equivalent command in Linux or MacOS:

`python3 -m pytest`

If you want to see the code coverage, then you can use the following command in Windows:

`pytest --cov`

You can use this equivalent command in Linux or MacOS:

`python3 -m pytest --cov`

## Verifying Correctness

To verify that your code is correct, you can run the tests. If your code passes all of the tests, then you can be confident that your code is correct. However, if your code fails any of the tests, then you will need to fix your code and try again.

### Generating a Coverage Report

To generate a coverage report, you can use the following command in Windows:

`pytest --cov --cov-report html`

You can use this equivalent command in Linux or MacOS:

`python3 -m pytest --cov --cov-report html`

This will generate a folder called `htmlcov` that contains a file called `index.html`. You can open this file in your web browser to see the coverage report.

## How to Submit

First, ensure that your code passes the tests (see the section **Verifying Correctness** for details). If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
pytest (Make sure all tests pass)
git add .
git commit -m "Demo lab completed code"
git push origin main
```
