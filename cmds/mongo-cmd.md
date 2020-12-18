# monogo cmd

## backup restore

mongodump --host=127.0.0.1 --port=27017 -u admin -p admin --archive=/tmp/dump --db=resource-manager

//进入容器
kubectl exec -it mongo-0 bash -n middlewares
//dump resource-manager
mongodump --host 127.0.0.1 --port 27017 --username admin --password admin --authenticationDatabase admin --archive=/tmp/camera --db=resource-manager --collection=camera
//先新建一个文件，再把dump 文件copy到宿主机
kubectl cp middlewares/mongo-0:/tmp/dump ./dump

mongorestore --archive=/tmp/dump


kubectl exec -it mongo-0 bash -n middlewares
mongo -u amdin -p admin
use resource-manager
db.camera.find({"meta.source.type":2})

db.getCollection('policy').find({"$and":[{"meta.type":"camera"},{"meta.resourceFilter.#or":{"$size":1}}]})
db.getCollection('policy').find({"$and":[{"meta.type":"camera"}]}).count()
db.getCollection('policy').find({"$and":[{"meta.type":"camera"},{"meta.groupAndResource.resources":{"$exists": true,"$not": {"$size":0}}}]})
db.user.updateOne({"_id":"2"},{"$set":{"meta.password":"21232f297a57a5a743894a0e4a801fc3"}})

db.camera.find({"meta.source.type":3}).count()

db.camera.find({"meta.source.type":2}).count()
db.camera.find({"meta.source":null}).count()

db.camera.count()
db.camera.find({"meta.source.type":2}).count()


db.camera.update({"meta.source":null},{"$set":{"meta.source":{"type":3}}})
db.camera.updateMany({},{"$set":{"meta.source.type":2}}})