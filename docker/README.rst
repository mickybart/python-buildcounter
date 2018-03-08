Docker
------

This part can be extracted to a new project to manage your own Uptime Server deployment
with custom Config and secrets management.

Create an image
^^^^^^^^^^^^^^^

.. code:: bash
    
    export VERSION=1
    docker build -t buildcounter:$VERSION .

secret.json
^^^^^^^^^^^

Check the README.rst on the root of the project.
