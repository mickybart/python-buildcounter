Build Counter
=============

Build Counters for statistics purpose (DevOps)

`Code documentation (sphinx) <https://mickybart.github.io/python-buildcounter/>`__

Docker
------

The docker folder provides everything to create an image of a Build Counter service.

buidlcounter module
-------------------

Installation
^^^^^^^^^^^^

This package is available for Python 3.5+.

Install the development version from github:

.. code:: bash

    pip3 install git+https://github.com/mickybart/python-buildcounter.git

Prerequisite
^^^^^^^^^^^^

Examples in this README are using the secret.json file to inject Mongo credentials.
Of course you can use any other solution provided by your infrastructure.

.. code:: python
    
    # Secrets structure
    #
    secrets = {
        "mongo" : {
            "uri": "",
            "db": "",
            "timeoutms": 5000,
            "collection" : ""
        }
    }

Quick start
^^^^^^^^^^^

.. code:: python

    from buildcounter.config import Config
    from buildcounter.app import App
    
    secrets = Config.load_json("secret.json")
    
    config = Config(secrets["mongo"])
    
    App(config).run()

Custom Config
^^^^^^^^^^^^^

The class Config is the main way to customize the build counter.

Please read the Code documentation for more details.

.. code:: python

    from buildcounter.config import Config
    from buildcounter.app import App
    
    secrets = Config.load_json("secret.json")
    
    class CustomConfig(Config):
        pass

    config = CustomConfig(ecrets["mongo"])
    
    App(config).run()

Error Types
-----------


Internal Notes
--------------

`Code documentation (sphinx) <https://mickybart.github.io/python-buildcounter/>`__

Bugs or Issues
--------------

Please report bugs, issues or feature requests to `Github
Issues <https://github.com/mickybart/python-buildcounter/issues>`__
