# Intro-to-Computer-Science-CSCI-1030U-Lecture-Notes

Here you will find all the in-class lecture code that we go over. This repository is a comprehensive collection of code examples, projects, and exercises designed to complement the material covered in the intro to computer science lectures.

## Getting Started

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

## Running the tests

To run the tests, you can use the following command in Windows:

`pytest`

You can use this equivalent command in Linux or MacOS:

`python3 -m pytest`

If you want to see the code coverage, then you can use the following command in Windows:

`pytest --cov`

You can use this equivalent command in Linux or MacOS:

`python3 -m pytest --cov`

## How to Submit

First, ensure that your code passes the tests (see the section **Verifying Correctness** for details). If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Demo lab completed code"
git push origin main
```
