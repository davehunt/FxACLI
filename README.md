# FxACLI

A simple command line tool for creating and disposing of test accounts for
[Firefox Accounts](https://developer.mozilla.org/en-US/docs/Mozilla/Tech/Firefox_Accounts).

## Target environment

By default all accounts will be created on the stage environment. You can use
the `--env` command line option to target `production` or `stable`.

## Installation

```
$ pipenv sync
```

## Creating a verified test account

```
$ pipenv run fxacli create
Account created!
 - 🌐  https://api-accounts.stage.mozaws.net/v1
 - 📧  test-72a888a3f6@restmail.net
 - 🔑  IvOhSLzI
Account verified! 🎉
```

## Destroying a test account

```
$ pipenv run fxacli destroy test-72a888a3f6@restmail.net IvOhSLzI
Account destroyed! 💥
```
