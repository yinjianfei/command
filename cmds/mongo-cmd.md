# monogo cmd

## backup restore

mongodump --host=127.0.0.1 --port=27017 -u admin -p admin --archive=/tmp/dump -d resource-manager

mongorestore --archive=/tmp/dump
db.getCollection('policy').find({"$and":[{"meta.type":"camera"},{"meta.resourceFilter.#or":{"$size":1}}]})
db.getCollection('policy').find({"$and":[{"meta.type":"camera"}]}).count()
db.getCollection('policy').find({"$and":[{"meta.type":"camera"},{"meta.groupAndResource.resources":{"$exists": true,"$not": {"$size":0}}}]})
