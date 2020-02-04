Contribution guidelines
=======================

Thank you for considering contributing to the `RIDE project`_.

RIDE is a development environment for `Robot Framework`_ test cases.

These guidelines provide instructions explaining how to submit issues and contribute
code or documentation to the `RIDE project`_.  Other great ways to contribute include
answering questions and participating in discussion on `robotframework-users`_ lists,
relevant `Slack`_ channels (especially #ride and #ride-dev) and other forums as well
as spreading the word about RIDE and Robot Framework one way or another.

These guidelines expect readers to have a basic knowledge about open source
as well as why and how to contribute to open source projects. If you are
totally new to these topics, it may be a good idea to look at the generic
`Open Source Guides`_ first.

.. contents::
   :depth: 2
   :local:


Submitting issues
-----------------

Bugs and enhancements are tracked using the `issue tracker`_.
If you are unsure if something is a bug or feature worth
implementing, you can first ask on `robotframework-users`_ list or #ride `Slack`_ channel. These and
other similar forums, not the issue tracker, are also places where to ask
general questions.

Before submitting a new issue, it is always a good idea to check is the
same bug or enhancement already reported. If it is, please add your
comments to the existing issue instead of creating a new one.

Reporting bugs
~~~~~~~~~~~~~~

Explain the bug you have encountered so that others can understand it
and preferably also reproduce it.

Key things to have in good bug report for RIDE include:

-  Python and wxPython version information.
-  RIDE and Robot Framework version.
-  Operating system.
-  Steps to reproduce the problem. With more complex problems it is
   often a good idea to create a "Short, Self-Contained, Correct Example"
   `(SSCCE)`_.
-  Possible error message and traceback.

  Note: all information in the issue tracker is public. Do not
  include any confidential or commercially sensitive information.

Enhancement requests
~~~~~~~~~~~~~~~~~~~~

Describe the new feature and use cases for it in as much detail as
possible by creating an issue using the `issue tracker`_.
Especially with larger enhancements, be prepared to
contribute the code in the form of a `Pull Request`_ as explained below or to
pay someone to do this work. Consider also would it be better to implement this
functionality as a separate project outside of RIDE.




Code contributions
------------------

If you have fixed a bug or implemented an enhancement, you can
contribute your changes via a GitHub `Pull Request`_. This is not
restricted to code. On the contrary, fixes and enhancements to
documentation\_ and tests\_ alone are also very valuable.

Choosing something to work on
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often you already have a bug or an enhancement you want to work on in
your mind, but you can also look at the `issue tracker`_ to find bugs and
enhancements submitted by others. The issues vary significantly in complexity
and difficulty, so you can try to find something that matches your skill
level and knowledge.  There are two specific labels to look for when looking for
something to contribute:

`good first issue`_
   These issues typically do not require any knowledge of Robot Framework
   internals and are generally easy to implement or fix. Thus these issues
   are especially good for new contributors.

`help_wanted`_
   These issues require external help to get implemented or fixed.

.. _good first issue: https://github.com/robotframework/RIDE/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22
.. _help_wanted: https://github.com/robotframework/RIDE/issues?q=is%3Aopen+is%3Aissue+label%3A%22help_wanted%22

Pull requests
~~~~~~~~~~~~~

On GitHub a `Pull Request`_ is the main mechanism to contribute code. They
are easy to use both for the contributor and for person accepting the
contribution, and with more complex contributions it is easy also for
others to join the discussion. Preconditions for creating a pull
requests are having a `GitHub`_ account, installing `Git`_ and forking the
`RIDE project`_.

GitHub has good articles explaining how to `set up Git`_, `fork a repository`_
and `use pull requests`_ and we do not go through them in more detail.
We do, however, recommend to create dedicated topic/feature branches for pull requests
instead of creating them based on the master branch. This is especially
important if you plan to work on multiple pull requests at the same time.

This project requires that pull request contains linear history of commits and
we do not allow that pull request contains merge commits or other noise. This helps
the review process and makes the maintenance easier for the project administrators.
Generally it is recommended to do `git pull --rebase`  instead of the `git pull --merge`
when there is need pull changes from upstream.

https://wiki.wxpython.org/How%20to%20Learn%20wxPython

Python Coding Style
~~~~~~~~~~~~~~~~~~~

In general, your Python code should be PEP-8/Flake8 compliant.  We will soon be implementing CI that will check compliance in this area so please save yourself refactoring effort and aim for full compliance.

`Reminder of PEP8 coding conventions <http://books.agiliq.com/projects/essential-python-tools/en/latest/linters.html>`_:

* Spaces are the preferred indentation method.
* Use 4 spaces per indentation level.
* In line with PEP8, 79 characters are preferred under most circumstances.  wxPython has some particularly long variable names however you should limit all lines to an absolute maximum of 90 characters to reduce horizontal scrolloing on side-by-side diffs.
* Separate top-level function and class definitions with two blank lines.
* Method definitions inside a class are surrounded by a single blank line.
* Imports should "one per line" and grouped as follows:

  * Standard Library imports
  * Related third party imports
  * Local app/library specific imports.

Different types of contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All contributors should familarise themselves with the existing wiki documentation:

https://github.com/robotframework/RIDE/wiki

User/Tester:

1. We welcome bug reports and enhancement requests by creating Issues but please
search the Issue history first to ensure you are not creating duplicates.
Your idea may have already been considered/rejected or they may already
be an open status Issue for a bug.

Developer:

1. Good understanding of `Git`_ and how to make contributions with a GitHub `Pull Request`_
2. Basic understanding of Python but perhaps beyond beginner level.  You are welcome to learn on this project.
3. Good understandting of wxPython






Finalizing pull requests
------------------------

Once you have code, documentation and tests ready, it is time to
finalize the pull request.

Acknowledgments
~~~~~~~~~~~~~~~

If you have done any non-trivial change and would like to be credited,
remind us to add `acknowledge` tag to the issue. This way we will add
your name to the release notes, when next release is made.

Resolving conflicts
~~~~~~~~~~~~~~~~~~~

Conflicts can occur if there are new changes to the master that touch
the same code as your changes. In that case you should
`sync your fork`_ and `resolve conflicts`_ to allow for an easy merge.




.. _Downloads: https://pypi.python.org/pypi/robotframework-ride
.. _Wiki: https://github.com/robotframework/RIDE/wiki

.. _BUILD: https://github.com/robotframework/RIDE/blob/master/BUILD.rest

.. _release notes: https://github.com/robotframework/RIDE/blob/master/doc/releasenotes/ride-1.7.4.1.rst




.. _RIDE project: https://github.com/robotframework/RIDE
.. _Robot Framework: https://github.com/robotframework/robotframework
.. _issue tracker: https://github.com/robotframework/RIDE/issues
.. _robotframework-users: https://groups.google.com/forum/#!forum/robotframework-users
.. _Open Source Guides: https://opensource.guide/
.. _Slack signup page: https://robotframework-slack-invite.herokuapp.com/
.. _Pull Request: https://help.github.com/articles/github-glossary/#pull-request
.. _Slack: https://robotframework-slack-invite.herokuapp.com
.. _Git: https://git-scm.com
.. _GitHub: https://github.com/
.. _(SSCCE): http://sscce.org

