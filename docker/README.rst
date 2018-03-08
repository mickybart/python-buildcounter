Docker
------

This part can be extracted to a new project to manage your own Uptime Server deployment
with custom Config and secrets management.

Create an image
^^^^^^^^^^^^^^^

.. code:: bash
    
    export VERSION=1
    export UPTIME_ENV=dev
    docker build -t buildcounter:$VERSION --build-arg UPTIME_ENV=$UPTIME_ENV .

secret.json
^^^^^^^^^^^

Check the README.rst on the root of the project.
