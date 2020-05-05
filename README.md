# Logging pipeline

## Network diagram
<p align="center">
  <img src=".img/network_diagram.png">
</p>

## .env
The Docker images are pinned to the following version below. If you want a different version please update `.env`
```
CONFLUENT_VERSION=5.5.0
LOGSTASH_VERSION=7.6.2
ROOT_LOGLEVEL=ERROR
SPLUNK_VERSION=splunk:8.0-debian
```

## Generate TLS certificates
### NGINX
1. `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout conf/nginx/ssl/nginx.key -out conf/nginx/ssl/nginx.crt`
1. `openssl dhparam -out conf/nginx/ssl/dhparam.pem 2048`

### Logstash
1. `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout conf/logstash/ssl/logstash.key -out conf/logstash/ssl/logstash.crt`

## Build pipeline and spin up stack
1. `docker-compose build`
1. `docker-compose up -d`

## Create Kafka Splunk connector
1. `virtualenv -p python3 venv`
1. `source venv/bin/activate`
1. `pip3 install -r requirements.txt`
1. `mv conf/python/config.yml.example conf/python/config.yml`
1. open `conf/python/config.yml`
  1. Splunk
    1. Set `external_url` to a URL that can be used to reach Splunk externally
    1. Set `username` to an admin user for Splunk
    1. Set `password` to a password for an admin user
    1. Set `index_name` to the name, you want the index to have in Splunk
  1. Kafka
    1. Set `connect_extenral_url` to a URL that can be used to reach Kafka Connect externally
    1. Set `topics` to a list of Kafka topics you want to be consumed and ingested into the index specified above
1. `python3 splunk-kafka-connector.py --all`


## References
* []()