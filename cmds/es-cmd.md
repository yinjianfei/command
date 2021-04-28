
curl -XGET 'http://elasticsearch-es-es-master-0.elasticsearch-es-es-master.middlewares.svc.cluster.local:9200/subject_repo*/_count'
curl -XGET 'http://10.40.46.25:19201/subject_repo*/_count'
kubectl port-forward --address=0.0.0.0 elasticsearch-es-es-master-0 19201:9200 -n middlewares
kubectl port-forward --address=0.0.0.0 mongo-0 27017:27017 -n middlewares
kubectl port-forward --address=0.0.0.0 id-service-8574b96854-tpcrp 25014:27017 -n middlewares
kubectl port-forward --address=0.0.0.0 txwl-business-77948bf65-frvh2 8080:8080 -n fp
server.connection-timeout=5000
curl '10.98.15.227:9200/_cat/indices'
curl -X GET "10.98.15.227:9200/subject_repo_5fffcfffd9fd96000136fff5_2001040_2021-01-16/_settings?pretty"

curl -XGET '10.102.111.227:9200/subject_repo*/_count'
 curl -XGET '10.104.203.209:9200/repository/external/1?pretty'

 curl -X GET "10.98.15.227:9200/repository/_search?pretty" -H 'Content-Type: application/json' -d'{
  "query": {
   
  }
}'
curl -X GET "10.98.15.227:19201/repository/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match_all": {}
    }
}
'
curl -X GET "10.98.15.227:9200/subject_repo_*/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match_all": {}
    }
}
'
curl -X GET "10.104.203.209:9200/feature_5fdc78b2e8507500010f027f_2001040_2020-12-18/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match_all": {}
    }
}
'


