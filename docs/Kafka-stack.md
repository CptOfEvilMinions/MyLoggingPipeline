
##  Create Kafka connector
```
curl http://connect:8083/connectors -X POST -H "Content-Type: application/json" -d'{
"name": "splunk-zeek1",
"config": {
  "connector.class": "com.splunk.kafka.connect.SplunkSinkConnector",
  "tasks.max": "10",
  "topics": "zeek_conn",
  "splunk.hec.uri":"https://splunk:8088",
  "splunk.hec.token": "<token>",
  "splunk.hec.ack.enabled" : "true",
  "splunk.hec.raw" : "false",
  "splunk.hec.track.data" : "true",
  "splunk.hec.ssl.validate.certs": "false"
 }
}
```

## References
* [cjmatta/README.md - kafka stack](https://gist.github.com/cjmatta/a716fa26bb1ed22dd7f8d66f2b87d1cd)
* [Configuring Docker Logging](https://docs.confluent.io/3.1.1/cp-docker-images/docs/operations/logging.html)
* [Github - Failed to deserialize data for topic to Avro: #1190](https://github.com/confluentinc/schema-registry/issues/1190)
* [Understand how ARG and FROM interact](https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact)
* [Difference between 'image' and 'build' within docker compose](https://stackoverflow.com/questions/34316047/difference-between-image-and-build-within-docker-compose)
* [Docker ARG, ENV and .env - a Complete Guide](https://vsupalov.com/docker-arg-env-variable-guide/#the-dot-env-file-env)
* [Kafka Broker doesn't find cluster id and creates new one after docker restart](https://stackoverflow.com/questions/59592518/kafka-broker-doesnt-find-cluster-id-and-creates-new-one-after-docker-restart)
* []()
* []()
* []()
* []()