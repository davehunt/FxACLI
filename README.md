# FxACLI

A simple command line tool for creating and disposing of test accounts for
[Firefox Accounts](https://developer.mozilla.org/en-US/docs/Mozilla/Tech/Firefox_Accounts).

[![license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/davehunt/FxACLI/blob/master/LICENSE.txt)
[![travis](https://img.shields.io/travis/davehunt/FxACLI.svg?label=travis)](http://travis-ci.org/davehunt/FxACLI/)
[![updates](https://pyup.io/repos/github/davehunt/FxACLI/shield.svg)](https://pyup.io/repos/github/davehunt/FxACLI/)
[![Python 3](https://pyup.io/repos/github/davehunt/FxACLI/python-3-shield.svg)](https://pyup.io/repos/github/davehunt/FxACLI/)

## Installation

```
$ pipenv install
```

## Target environment

By default all accounts will be created on the stage environment. You can use
the `--env` command line option to target `production` or `stable`.

## Creating a verified test account

```
$ pipenv run fxacli create
Account created!
 - 🌐  https://api-accounts.stage.mozaws.net/v1
 - 📧  test-72a888a3f6@restmail.net
 - 🔑  IvOhSLzI
Account verified! 🎉
```

## Destroying test accounts

The most recently created account can be destroyed by simply running:

```
$ pipenv run fxacli destroy
Account destroyed! 💥
- 🌐  https://api-accounts.stage.mozaws.net/v1
- 📧  test-72a888a3f6@restmail.net
- 🔑  IvOhSLzI
```

To destroy a specific account, or one not created using this tool, you must
specify `--email` and `--password` options.
