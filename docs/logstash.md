# Logstash
Logstash is the frontend to the logging for ingest logs from client. Logstash was picked because there is a plethora of plugins, documentation, and support for this tool.

## Generate OpenSSL cert
1. `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout Docker/logstash/certs/logstash.key -out Docker/logstash/certs/logstash.crt`

## Spin up logstash
1. `docker-compose -f docker-compose-logstash.yml build`
1. `docker-compose -f docker-compose-logstash.yml up -d`

## References
* [Configuration Management Settings in Logstash](https://www.elastic.co/guide/en/logstash/current/configuring-centralized-pipelines.html#configuration-management-settings)
* [Repositories for APT and YUM](https://www.elastic.co/guide/en/beats/filebeat/current/setup-repositories.html)
* [Setting up SSL for Filebeat and Logstash](https://documentation.wazuh.com/2.1/installation-guide/optional-configurations/elastic_ssl.html)
* [Kafka Input Configuration in Logstash](https://facingissuesonit.com/2017/05/06/integrate-logstash-with-kafka/)
* [How to remove fields in logstash/es](https://discuss.elastic.co/t/how-to-remove-fields-in-logstash-es/77039/2)
* []()
* []()
* []()
* []()
