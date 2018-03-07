## Drone counters with history

Drone counters permit to get the history of drone deployments and to expose counters of deployments.

### Legacy

Use the MySQL drone database

#### Get total number of deployments

> curl http://localhost:5000/counters/total

#### Get total number of deployments for a specific repo and branches

> curl -H "Content-type: application/json" -X POST http://localhost:5000/counters/repo -d '{"repo":"CLOUD/console-server", "branch_regex":"develop"}'

### New

Use an internal MongoDB collection to be isolate from the MySQL drone database

#### New deployment

> curl -H "Content-type: application/json" -X POST http://localhost:5000/drone/history -d '{ "owner" : "CLOUD", "name" : "console-server", "branch" : "develop", "author_email" : "cloud@yp.ca", "build_created" : 1495552425, "commit" : "042efe90cc65b6d9bcdd500c0d6798e10fbf7fc5", "build_number" : 90}'

#### Get total number of deployments

> curl http://localhost:5000/drone/counters/total

#### Get total numer of deployments for a specific repo and branch

`release` and `all` are special identifiers which permit respectively to get `all release/*` branches and `all` branches <br>

> curl http://localhost:5000/drone/counters/for/CLOUD/console-server/all <br>
> curl http://localhost:5000/drone/counters/for/CLOUD/console-server/master <br>
> curl http://localhost:5000/drone/counters/for/CLOUD/console-server/develop <br>
> curl http://localhost:5000/drone/counters/for/CLOUD/console-server/release <br>
> curl http://localhost:5000/drone/counters/for/CLOUD/console-server/release/0.1 <br>

