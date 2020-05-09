# Confluent Kafka docs

##  Create Kafka connector
```
curl http[s]://<Kafka Connect IP addr/FQDN>:8083/connectors -X POST -H "Content-Type: application/json" -d'{
  "name": "<Name of Kafka Connector consumer for Splunk>",
    "config": {
     "connector.class": "com.splunk.kafka.connect.SplunkSinkConnector",
     "tasks.max": "10",
     "topics": "<List of Kafka topics seperated by commas: zeek_conn, zeek_dns, zeek_sll, etc>",
     # Specifying "splunk" as the hostname because Kafka Connect and Splunk share a Docker network so they can communicate by Docker container name
     "splunk.hec.uri":"https://splunk:8088",
     "splunk.hec.token": "<Splunk HEC token>",
     "splunk.hec.ack.enabled : "true",
     "splunk.hec.raw" : "false",
     "splunk.hec.track.data" : "true",
     # The Splunk Docker container generates self-signed certs for HEC endpoints
     "splunk.hec.ssl.validate.certs": "false"
    }
}'
```

## Build logstash
1. `docker-compose build connect`

## References
* [cjmatta/README.md - kafka stack](https://gist.github.com/cjmatta/a716fa26bb1ed22dd7f8d66f2b87d1cd)
* [Configuring Docker Logging](https://docs.confluent.io/3.1.1/cp-docker-images/docs/operations/logging.html)
* [Github - Failed to deserialize data for topic to Avro: #1190](https://github.com/confluentinc/schema-registry/issues/1190)
* [Understand how ARG and FROM interact](https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact)
* [Difference between 'image' and 'build' within docker compose](https://stackoverflow.com/questions/34316047/difference-between-image-and-build-within-docker-compose)
* [Docker ARG, ENV and .env - a Complete Guide](https://vsupalov.com/docker-arg-env-variable-guide/#the-dot-env-file-env)
* [Kafka Broker doesn't find cluster id and creates new one after docker restart](https://stackoverflow.com/questions/59592518/kafka-broker-doesnt-find-cluster-id-and-creates-new-one-after-docker-restart)
* [doccker-compse - EXTRA_HOSTS](https://docs.docker.com/compose/compose-file/compose-file-v2/)
* [Support host.docker.internal in dockerd on Linux #40007](https://github.com/moby/moby/pull/40007)