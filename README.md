[ansible-lint](https://github.com/willthames/ansible-lint) to JUnit converter
---

### Usage:
1. download and install (i.e. via pip) [ansible-lint](https://github.com/willthames/ansible-lint)
2. run `ansible-lint` on your playbook(s) with parameter `-p` (it is required) and redirect output to file
  ```shell
  ansible-lint -p your_fancy_playbook.yml > ansible-lint.txt
  ```
3. run `ansible-lint-junit` and pass generated file to it
  ```shell
  ansible-lint-junit ansible-lint.txt -o ansible-lint.xml
  ```
