submodules-dev
==============

This is a simple python script that just clone or checkout the master version
of each of your submodules.

This can be used in a development environment to:

* Avoid the "detached heads" problems when you work on submodules
* Be sure to have the master version of all dependencies

Usage
-----

Simply run the script from the top-level of your repository :

```
./submodules-dev.py
```

It will clone and/or checkout all the submodules on master
