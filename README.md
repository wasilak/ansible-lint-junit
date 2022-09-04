[![Build Status](https://travis-ci.org/wasilak/ansible-lint-junit.svg?branch=master)](https://travis-ci.org/wasilak/ansible-lint-junit)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/wasilak/ansible-lint-junit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/wasilak/ansible-lint-junit/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/wasilak/ansible-lint-junit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/wasilak/ansible-lint-junit/context:python)
[![Maintainability](https://api.codeclimate.com/v1/badges/e50acaa43b7a5f762904/maintainability)](https://codeclimate.com/github/wasilak/ansible-lint-junit/maintainability)

Ansible-lint-junit
---

The [ansible-lint](https://github.com/willthames/ansible-lint) to JUnit converter.

### Installation

via pip:

```shell
pip install ansible-lint-junit
```

### Updating

via pip:

```shell
pip install ansible-lint-junit --upgrade
```

### Usage:

- You can run `ansible-lint` on your playbook(s) and redirect output to pipe
  ```shell
  ansible-lint playbook.yml -p --nocolor | ansible-lint-junit -o ansible-lint.xml
  ```
- You can use a temporary file to store the output of `ansible-lint`.
  After that run `ansible-lint-junit` and pass generated file to it
  ```shell
  ansible-lint -p --nocolor your_fancy_playbook.yml > ansible-lint.txt
  ansible-lint-junit ansible-lint.txt -o ansible-lint.xml
  ```

### Output

- If there are any lint errors, full JUnit XML will be created.
- If there are no errors, empty JUnit XML will be created, this is for
  i.e. [Bamboo](https://www.atlassian.com/software/bamboo) JUnit parser plugin compatibility.\
  It will break build if XML is missing or incorrect, and there is really no way of generating XML with *"PASSED"* tests
  in case of linter.

### License

The ansible-lint-junit project is distributed under the [MIT] license.