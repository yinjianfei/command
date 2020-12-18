# kafka

## kafka cmd

> bin/kafka-configs.sh --zookeeper zookeeper-headless:2181 --entity-type topics --entity-name new_subject --describe
> bin/kafka-topics.sh --list --zookeeper zookeeper-headless:2181

## kafka pt

./kafka-producer-perf-test.sh --producer-props bootstrap.servers=127.0.0.1:9092 --num-records 18000000 --record-size 5000 --throughput 20000 --topic test


./kafka-consumer-perf-test.sh --broker-list localhost:9092 --topic test --fetch-size 1048576 --messages 18000000 --threads 1


 kafka-console-consumer.sh --bootstrap-server node1:9092 --from-beginning --topic new_subject


+# list kafka topics, double check
+topics=`kubectl exec -n middlewares kafka-0 -- /opt/bitnami/kafka/bin/kafka-topics.sh --list --zookeeper zookeeper-0.zookeeper-headless.middlewares.svc.cluster.local:2181`
+for topic in $topic_list;
+do
+if [[ "NO" == `echo "${topics[@]}" |grep -wq "$topic" && echo "YES" || echo "NO"` ]];then
+    echo "create kafka topic error $topic"
+    exit 1
+fi
+done
