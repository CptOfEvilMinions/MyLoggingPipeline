# Splunk docs

## Build logstash
1. `docker run --rm -it -e SPLUNK_PASSWORD=changeme splunk/splunk:8.0.3-debian create-defaults > conf/splunk/default.yml`
1. `docker-compose -f docker-compose.yml build splunk`

## References
* [Splunk NGINX](https://dev.splunk.com/enterprise/docs/dataapps/httpeventcollector/confignginxloadhttp)
* [Configuring Nginx Load Balancer For The HTTP Event Collector](https://www.splunk.com/en_us/blog/tips-and-tricks/configuring-nginx-load-balancer-for-the-http-event-collector.html)
* [Set up and use HTTP Event Collector in Splunk Web](https://docs.splunk.com/Documentation/Splunk/8.0.3/Data/UsetheHTTPEventCollector)
* [docker-splunk - examples](https://splunk.github.io/docker-splunk/EXAMPLES.html#create-standalone-from-cli)
* [Github - dennybritz/docker-splunk](https://github.com/dennybritz/docker-splunk/tree/master/enterprise)
* [Unable to connect Splunk HEC using https](https://answers.splunk.com/answers/773770/unable-to-connect-splunk-hec-using-https.html)
* [Github - splunk/kafka-connect-splunk - Configuration schema structure ](https://github.com/splunk/kafka-connect-splunk)
* [CREATE A SECURE ADMINISTRATOR PASSWORD IN DOCKER FOR SPLUNK 7.1.0](https://www.outcoldsolutions.com/blog/2018-04-25-docker-splunk-7-1-0/)
* [Configuration file directories](https://docs.splunk.com/Documentation/Splunk/8.0.3/Admin/Configurationfiledirectories)