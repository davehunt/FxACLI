# FxACLI

A simple command line tool for creating and disposing of test accounts for
[Firefox Accounts](https://developer.mozilla.org/en-US/docs/Mozilla/Tech/Firefox_Accounts).

## Installation

```
$ pipenv sync
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
