=========
Using Git
=========

Making changes
--------------

If you want to add a new feature, branch off the ``develop`` branch, and when you
want to fix a bug, branch off ``main`` instead.

To create a new feature branch that tracks the upstream development branch::

    git checkout develop -b your-awesome-feature-name upstream/develop

Make your changes, the add and commit your created, modified or deleted files::

    git add my-file-or-directory
    git commit -m "An explanatory commit message"
	
During the commit, your code will be linted and formatted using ``ruff``. Please see the guide to :ref:`code-style` for more details.

Keeping your branch up to date
------------------------------

If you are adding a new feature, please update your local  ``develop`` branch and then rebase your feature branch onto it.
If you are fixing a bug, please update your local ``main`` branch and then rebase your bug-fix branch onto it.

To update the ``develop`` branch, switch to it and pull changes from the upstream branch::

    git checkout develop
    git pull upstream develop --tags

Now switch back to your feature branch and rebase it on top of the up-to-date ``develop``::

    git checkout your-awesome-feature-name
    git rebase develop

Sharing your changes
--------------------

Update your remote branch::

    git push -u origin your-awesome-feature-name

You can then make a `pull request
<https://docs.github.com/en/get-started/quickstart/contributing-to-projects#making-a-pull-request>`_
on Github to the ``develop`` branch for new features and ``main`` branch for bug fixes.