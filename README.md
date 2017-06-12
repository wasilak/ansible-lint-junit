[ansible-lint](https://github.com/willthames/ansible-lint) to JUnit converter
---

### Installation
via pip;
```shell
pip install ansible-lint-junit
```
### Updating
via pip;
```shell
pip install ansible-lint-junit --upgrade
```

### Usage:
1. run `ansible-lint` on your playbook(s) with parameter `-p` (it is required) and redirect output to file
  ```shell
  ansible-lint -p your_fancy_playbook.yml > ansible-lint.txt
  ```
2. run `ansible-lint-junit` and pass generated file to it
  ```shell
  ansible-lint-junit ansible-lint.txt -o ansible-lint.xml
  ```

### Output
* if there are any lint errors, full JUnit XML will be created
* if there are no errors, empty JUnit XML will be created, this is for i.e. [Bamboo](https://www.atlassian.com/software/bamboo) JUnit parser plugin compatibility.
It will break build if XML is missing or incorrect, and there is really no way of generating XML with *"PASSED"* tests in case of linter.
