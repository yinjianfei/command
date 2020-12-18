
curl '10.105.178.234:9200/_cat/indices'


curl GET '10.105.178.234:9200/repository/_search'
 curl -XGET '10.105.178.234:9200/repository/external/1?pretty'

 curl -X GET "10.105.178.234:9200/repository/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
   
  }
}
'
curl -X GET "10.105.178.234:9200/repository/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match_all": {}
    }
}
'
curl -X GET "10.105.178.234:9200/subject_repo_5fdc78b2e8507500010f027f_2001040_2020-12-18/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match_all": {}
    }
}
'
curl -X GET "10.105.178.234:9200/feature_5fdc78b2e8507500010f027f_2001040_2020-12-18/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match_all": {}
    }
}
'
