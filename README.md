# Python Tutorial
[![CI Build](https://github.com/chungmuen/Find_Circularity/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/chungmuen/Find_Circularity/actions/workflows/build.yml)
[![Docstring](./docs_badge.svg)](https://github.com/chungmuen/Find_Circularity/actions/workflows/build.yml)
[![Documentation Status](https://readthedocs.org/projects/find-circularity/badge/?version=latest)](https://find-circularity.readthedocs.io/en/latest/?badge=latest)

# python tutorial about testing

Objective Unit test: test business logic of the code, and only our own code, not library/framework.
ex: using sqlalchemy to create an entry in a DB. creating an object from the model, and commit the object with session.commit(Object). 
when testing there is no DB, to make the test work, there are a couple of solutions: ex: in memory DB - such as sqlite, or "Mock" the session.commit() function.
Whenever session.commit is called, execute the "mock function" the is defined by us.

all the tests are suppose to run isolated, ie, from outside services. This is because the test should not be dependent on the status of external service.

by convention, "self" points to the object itself, a class is the template of an object.
"cls" is used to point to the class itself.

using patch we can mock external functions, and test whether the input given to the external function is correct

## 20240125
### ToDo
- Lookup the testcase built in methods
- Try it with own code
- Review Linting
- lookup PEP257 specification - python documentation 

ctrl + click beings you to function def

reference material:
https://github.com/terazus/curated-tools/blob/NewTutorial/new_python_project.md
https://github.com/terazus/curated-tools/blob/main/python.md

### mylib is not a proper name in real life

rst is an extension of markdown, stands for restructured text

## 20240130
conditional debugger: for example in a for loop, we can do "i==4"
ex: when iterating over a dict, we can set the breakpoint at dict[key]=="some value"
javascript transpiling

### docstring badge
docstr-coverage libs/ --fail-under=100 --badge="./docs_badge.svg"


### generate readthedocs
.\docs\make.bat html

python tutorial about testing

### next time
- commit the badge inside our github action (need a special tocken from inside github)
- codacy for coverage report and general code quality report
- codacy scans the code, detect for replicated fragments
- host the doc on readthedocs, and let readthedocs build our documentation

## 20240215

No need to add docstring for tests
look documentation: in python terminal, import a module, then type help(module_name)
right - click on folder "test" : more Run/Debug - run python test with coverage
Profiling - rather advanced for developers in python
you can have many small commits, and then squash them during pull requests

It's ok to make mistakes, but it is VERY IMPORTANT to be consistant!!
Github understand that PascalCase needs to be two separate words for branch names, so when creating new branches in terminal, we can give names in PascalCases 