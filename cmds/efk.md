[参考](https://zhuanlan.zhihu.com/p/147799204)

docker run -itd --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.7.1


docker run --link 6323d447914b:elasticsearch -p 5601:5601 -d  --name kibana7.7.1 kibana:7.7.1 

docker run -d  -v /home/jianfei.yin/compose/elk/filebeat.docker.yml:/usr/share/filebeat/filebeat.yml -v //home/jianfei.yin/workspace/ficus2/product/face_platform/txwl/log/:/apps/txwl/logs/ --link 6323d447914b:elasticsearch --link 2c0c805805ab:kibana --name filebeat  elastic/filebeat:7.7.1



## install efk 7.10.2
### pull images
docker pull docker.elastic.co/beats/filebeat:7.10.2
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.10.2
docker pull docker.elastic.co/kibana/kibana:7.10.2

### install es
docker run -itd --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.2

### install kibana
使用es的containerID

增加告警能力， xpack.encryptedSavedObjects.encryptionKey=111111111122222222223333333333444


docker run --link 9db74caf660b:elasticsearch -p 5601:5601 -d  --name kibana docker.elastic.co/kibana/kibana:7.10.2


### install filebeat
docker run -d  -v /home/jianfei.yin/compose/elk/filebeat.docker.yml:/usr/share/filebeat/filebeat.yml -v //home/jianfei.yin/workspace/ficus2/product/face_platform/txwl/log/:/apps/txwl/logs/ --link 9db74caf660b:elasticsearch --link 66d13ef6044c:kibana --name filebeat  docker.elastic.co/beats/filebeat:7.10.2

```
filebeat.inputs:
- type: log
  enabled: true
  ##配置你要收集的日志目录，可以配置多个目录
  paths:
    - /apps/txwl/logs/*.log

  ##配置多行日志合并规则，已时间为准，一个时间发生的日志为一个事件      
  multiline.pattern: '^\d{4}-\d{2}-\d{2}'
  multiline.negate: true
  multiline.match: after

## 设置kibana的地址，开始filebeat的可视化  
setup.kibana.host: "http://kibana:5601"
setup.dashboards.enabled: true
#-------------------------- Elasticsearch output ---------
output.elasticsearch:
    hosts: ["http://elasticsearch:9200"]
    index: "txwl-%{+yyyy.MM.dd}"

setup.template.name: "txwl"
setup.template.pattern: "txwl-*"
json.keys_under_root: false
json.overwrite_keys: true
##设置解析json格式日志的规则
processors:
- decode_json_fields:
     fields: ['message']
     target: ''
     overwrite_keys: true

```