FxACLI
======

A simple command line tool for creating and disposing of test accounts for
`Firefox Accounts`_.

.. image:: https://img.shields.io/badge/license-MPL%202.0-blue.svg
   :target: https://github.com/davehunt/FxACLI/blob/master/LICENSE
   :alt: License
.. image:: https://img.shields.io/pypi/v/FxAClI.svg
   :target: https://pypi.python.org/pypi/FxAClI/
   :alt: PyPI
.. image:: https://img.shields.io/travis/davehunt/FxACLI.svg
   :target: https://travis-ci.org/davehunt/FxACLI/
   :alt: Travis
.. image:: https://img.shields.io/github/issues-raw/davehunt/FxACLI.svg
   :target: https://github.com/davehunt/FxACLI/issues
   :alt: Issues
.. image:: https://api.dependabot.com/badges/status?host=github&repo=davehunt/FxACLI
   :target: https://dependabot.com
   :alt: Updates

Installation
------------

.. code-block:: bash

  $ pip install fxacli

Target environment
------------------

By default all accounts will be created on the stage environment. You can use
the ``--env`` command line option to target ``production`` or ``stable``.

Creating a verified test account
--------------------------------

.. code-block:: bash

  $ fxacli create
  Account created!
   - 🌐  https://api-accounts.stage.mozaws.net/v1
   - 📧  test-72a888a3f6@restmail.net
   - 🔑  IvOhSLzI
  Account verified! 🎉

Destroying test accounts
------------------------

The most recently created account can be destroyed by simply running:

.. code-block:: bash

  $ fxacli destroy
  Account destroyed! 💥
   - 🌐  https://api-accounts.stage.mozaws.net/v1
   - 📧  test-72a888a3f6@restmail.net
   - 🔑  IvOhSLzI

To destroy all accounts created using the tool, pass the ``--all`` flag.

To destroy a specific account, or one not created using this tool, you must
specify ``--email`` and ``--password`` options.

Resources
---------

- `Release Notes`_
- `Issue Tracker`_
- Code_

.. _Firefox Accounts: https://developer.mozilla.org/en-US/docs/Mozilla/Tech/Firefox_Accounts
.. _Release Notes:  http://github.com/davehunt/FxACLI/blob/master/CHANGES.rst
.. _Issue Tracker: http://github.com/davehunt/FxACLI/issues
.. _Code: http://github.com/davehunt/FxACLI
