# monogo cmd

## backup restore
kubectl exec -it mongo-0 bash -n middlewares
mongodump --host 127.0.0.1 --port 27017 --username admin --password admin --authenticationDatabase admin --archive=/tmp/policy --db=resource-manager

10.105.221.131
kubectl cp middlewares/mongo-0:/tmp/policy ./policy
//进入容器
kubectl exec -it mongo-0 bash -n middlewares
//dump resource-manager
mongodump --host 127.0.0.1 --port 27017 --username admin --password admin --authenticationDatabase admin --archive=/tmp/resource  --db=resource-manager
//退出容器，新建一个文件，再把dump 文件copy到宿主机
kubectl cp middlewares/mongo-0:/tmp/resource ./resource
//scp到另外一台机器

//copy到容器内
kubectl cp dump middlewares/mongo-0:/tmp
//进入容器
kubectl exec -it mongo-0 bash -n middlewares
mongorestore --host 127.0.0.1 --port 27017 --username admin --password admin --authenticationDatabase admin  --archive=/tmp/dump
mongorestore  --archive=/tmp/dump


kubectl exec -it mongo-0 bash -n middlewares
mongo -u amdin -p admin
use resource-manager
db.camera.find({"attrs.name":"duiqi"})


## mongodb array contains
db.inventory.find( { tags: "red" } )

##  contains 字符串
db.camera.find({"attrs._group_path" : {$regex : ".*:2_group:*"}})



kubectl exec -it mongo-0 bash -n middlewares
mongo -u amdin -p admin
use resource-manager
db.getCollection('policy').find({"attrs.action": /^528/})




kubectl exec -it mongo-0 bash -n middlewares
mongo -u amdin -p admin
use resource-manager
db.camera_group.find()
use face_platform
db.history_track_retrieval_query.find().count()
db.history_track_retrieval_query.getIndexes()


db.getCollection('policy').find({"$and":[{"meta.type":"camera"},{"meta.resourceFilter.#or":{"$size":1}}]})
db.getCollection('policy').find({"$and":[{"meta.type":"camera"}]}).count()
db.getCollection('policy').find({"$and":[{"meta.type":"camera"},{"meta.groupAndResource.resources":{"$exists": true,"$not": {"$size":0}}}]})
db.user.updateOne({"meta.name":"admin"},{"$set":{"meta.password":"0192023a7bbd73250516f069df18b500"}})


db.history_track_retrieval_query.find({ "finished": false, "id": { "$gte": 0 } })
db.history_track_retrieval_query.ensureIndex({user_id : 1, query_time: 1})
db.history_track_retrieval_query.ensureIndex({finished: 1, id: 1})
db.history_track_retrieval_query.find({"id":142130})
db.camera.find({"meta.source.type":3}).count()

db.camera.find({"meta.source.type":2}).count()
db.camera.find({"meta.source":null}).count()

db.camera.count()
db.camera.find({"meta.source.type":2}).count()


db.camera.update({"meta.source":null},{"$set":{"meta.source":{"type":3}}})
db.camera.updateMany({},{"$set":{"meta.source.type":2}}})


db.getCollection('policy').find({"$and":[{"meta.userFilter.#eq.id":"1"},{"meta.type":"role"}]}]})


db.getCollection('policy').find({"$and":[{"meta.type":"camera"},{"meta.userFilter.#eq.id":"2"}]}).count()

db.getCollection('policy').update({"$and":[{"meta.resourceFilter.#or.0":{"#preMatch":{"_group_path":"8_group:"}}},{"meta.resourceFilter.#or.1":{"#preMatch":{"_group_path":"0_group:1_group:"}}},{"meta.type":"role"}]})



db.getCollection('policy').find({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["2_group","0_group"]}]}).count()

db.getCollection('policy').find({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["0_group","2_group"]}]}).count()

db.getCollection('policy').find({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["0_group"]}]}).count()



db.policy.updateMany({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["0_group"]}]},{"meta.groupAndResource.groups":["1_group"]})

db.getCollection('policy').find({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["2_group","0_group"]}]},{"meta.groupAndResource.groups":["2_group","1_group"]})



db.policy.updateMany({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["0_group","1_group"]}]},{"$set":{"meta.groupAndResource.groups":["1_group"]}})

db.policy.updateMany({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["2_group","0_group","1_group"]}]},{"$set":{"meta.groupAndResource.groups":["2_group","1_group"]}})

db.policy.updateMany({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["2_group","1_group"]}]},{"$set":{"meta.groupAndResource.groups":["1_group"]}})


db.getCollection('policy').find({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["2_group","0_group","1_group"]}]}).count()
db.getCollection('policy').find({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["0_group","1_group"]}]}).count()



db.getCollection('policy').find({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["2_group","1_group"]}]}).count()
db.getCollection('policy').find({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":["1_group"]}]}).count()
db.getCollection('policy').find({"$and":[{"meta.userFilter.#eq.id":"2"},{"meta.type":"camera"},{"meta.groupAndResource.groups":"2_group"}]}).count()

db.camera_group.deleteOne({"_id":"2_group"})

db.camera.find({"attrs._group_path" : {$regex : ".*0_group:1_group*"}})
1605974400

kubectl exec -it mongo-0 bash -n middlewares
mongo -u amdin -p admin
use face_platform
db.user_manager.find({"timestamp":{"$lt":1605974400}}).count()
db.user_manager.deleteMany({"timestamp":{"$lt":1605974400}})


db.getCollection('policy').find({"$and":[{"meta.type":"camera"},
        {
            "meta.resourceFilter.#or": {
                "#preMatch": {
                    "_group_path": "0_group:"
                }
            }
        }]}).count()


db.getCollection('policy').updateMany({"$and":[{"meta.type":"camera"},
        {
            "meta.resourceFilter.#or": [{
                "#preMatch": {
                    "_group_path": "0_group:"
                }
            }]
        }]},{"$set":{
            "meta.resourceFilter.#or": [{
                "#preMatch": {
                    "_group_path": "0_group:1_group:"
                }
            }]
        }})
db.getCollection('policy').updateMany({"$and":[{"meta.type":"camera"},
        {
            "meta.resourceFilter.#or.0": [{
                "#preMatch": {
                    "_group_path": "0_group:"
                }
            }]
        }]},{"$set":{
            "meta.resourceFilter.#or.0": [{
                "#preMatch": {
                    "_group_path": "0_group:1_group:"
                }
            }]
        }})


db.getCollection('policy').updateMany({"$and":[{"meta.type":"camera"},
        {
            "meta.resourceFilter.#or.10": {
                "#preMatch": {
                    "_group_path": "0_group:"
                }
            }
        }]},{"$set":{
            "meta.resourceFilter.#or.10": {
                "#preMatch": {
                    "_group_path": "0_group:1_group:"
                }
            }
        }})






0 1  5 10






db.getCollection('policy').find({
    "$and": [
        {
            "meta.userFilter.#eq.id": "1"
        },
        {
            "meta.resourceFilter.#or":{"$size":2}
        },
        {
            "meta.resourceFilter.#or.0": {
                "#preMatch": {
                    "_group_path": "8_group:"
                }
            }
        },
        {
            "meta.resourceFilter.#or.1": {
                "#preMatch": {
                    "_group_path": "7_group:2_group:"
                }
            }
        },
        {
            "meta.type": "role"
        }
    ]
})
db.getCollection('policy').updateMany({"$and":[{"meta.userFilter.#eq.id":"1"},{"meta.resourceFilter.#or":{"$size":2}},{"meta.resourceFilter.#or.0":{"#preMatch":{"_group_path":"8_group:"}}},{"meta.resourceFilter.#or.1":{"#preMatch":{"_group_path":"7_group:2_group:"}}},{"meta.type":"role"}]},{
    "$set":{"meta.resourceFilter.#or": [{"#preMatch":{"_group_path":"8_group:"}},{"#preMatch":{"_group_path":"7_group:"}}]}
})

db.getCollection('policy').update({"_id" : "5e91d3270654b0626484e708"},{
    "$set":{"meta.resourceFilter.#or": [{"#preMatch":{"_group_path":"8_group:"}},{"#preMatch":{"_group_path":"7_group:"}}]}
})


kubectl exec -it mongo-0 bash -n middlewares
mongo -u amdin -p admin
use face_platform
db.user_manager.find({"$and":[{"user_id":4},{"topic":"login"}]})


db.getCollection('camera').updateMany({"attrs.group_id":"0_group"},{"$set":{"attrs._group_path":"0_group:1_group:" + this._id+":","attrs.group_id":"1_group"}})



//停止fp 防止更新过程中出现其他update操作

kubectl exec -it mongo-0 bash -n middlewares
mongo -u amdin -p admin

//dump camera
mongodump --host 127.0.0.1 --port 27017 --username admin --password admin --authenticationDatabase admin --archive=/tmp/cameras --db=resource-manager --collection=camera

use resource-manager
//查看设备， 这些设备看起来都是很早之前创建的设备， id比较老
db.getCollection('camera').find({"attrs.group_id":"0_group"})
//2001 条
db.getCollection('camera').find({"attrs.group_id":"0_group"}).count()
//更新设备信息
db.getCollection('camera').updateMany({"attrs.group_id":"0_group"},{"$set":{"attrs._group_path":"0_group:1_group:" + this._id+":","attrs.group_id":"1_group"}})




## policy 错误修复
db.getCollection('policy').updateMany({"$and":[{"meta.type":"camera"},{"meta.userFilter.#eq.id":"2"}]},{"$set":{"meta.resourceFilter":[{"#preMatch" : { "_group_path" : "0_group:1_group:" } }]}})

db.getCollection('policy').updateMany({"$and":[{"meta.type":"camera"},{"meta.userFilter.#eq.id":"2"}]},{"$set":{"meta.groupAndResource.resources":[]}})

db.getCollection('policy').find({"$and":[{"meta.type":"camera"},{"meta.userFilter.#eq.id":"2"}]}).count()


db.getCollection('camera').find({"attrs._group_path": /^0_group:1_group:3_group:27_group:/})
db.camera.updateMany({"attrs._group_path": /^0_group:1_group:3_group:27_group:/},{"$set":{"meta.administrative_division.custom_region_id":NumberInt(27)}})