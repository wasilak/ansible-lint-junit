[ansible-lint](https://github.com/willthames/ansible-lint) to JUnit converter [![Build Status](https://travis-ci.org/wasilak/ansible-lint-junit.svg?branch=master)](https://travis-ci.org/wasilak/ansible-lint-junit)[![Total alerts](https://img.shields.io/lgtm/alerts/g/wasilak/ansible-lint-junit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/wasilak/ansible-lint-junit/alerts/)[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/wasilak/ansible-lint-junit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/wasilak/ansible-lint-junit/context:python)
---

### Installation
via pip;
```shell
# In case of Python 2.x, you have to first run:
# pip install lxml

pip install ansible-lint-junit
```

### Updating
via pip:
```shell
pip install ansible-lint-junit --upgrade
```

### Usage:
1. you can pipe output of `ansible-lint`:
    ```shell
    # less verbose
    ansible-lint playbook.yml -p --nocolor | ansible-lint-junit -o ansible-lint.xml

    # more verbose
    ansible-lint playbook.yml --parseable-severity --nocolor | ansible-lint-junit -o ansible-lint.xml
    ```
3. or run `ansible-lint` on your playbook(s) and redirect output to file
    ```shell
    # less verbose
    ansible-lint -p --nocolor your_fancy_playbook.yml > ansible-lint.txt

    # more verbose
    ansible-lint --parseable-severity --nocolor your_fancy_playbook.yml > ansible-lint.txt
    ```
    and run `ansible-lint-junit` and pass generated file to it
    ```shell
    # less verbose
    ansible-lint-junit ansible-lint.txt -o ansible-lint.xml

    # more verbose
    ansible-lint-junit ansible-lint.txt -o ansible-lint.xml
    ```

### Output
* if there are any lint errors, full JUnit XML will be created
* if there are no errors, empty JUnit XML will be created, this is for i.e. [Bamboo](https://www.atlassian.com/software/bamboo) JUnit parser plugin compatibility.
It will break build if XML is missing or incorrect, and there is really no way of generating XML with *"PASSED"* tests in case of linter.
