# Splunk docs

## Build Splunk
1. `docker-compose build splunk`

## Splunk running on host
1. `sudo sed -r -i 's/SPLUNK_BINDIP=(\b[0-9]{1,3}\.){3}[0-9]{1,3}\b/SPLUNK_BINDIP=127.0.0.1/g' /opt/splunk/etc/splunk-launch.conf`
    1. Forces Splunk to listen on 127.0.0.1
1. `sudo systemctl restart splunk && sudo systemctl status splunk`
1. `sudo apt-get update -y && sudo apt-get install nginx curl -y`
1. `curl https://raw.githubusercontent.com/CptOfEvilMinions/MyLoggingPipeline/master/conf/nginx/nginx.conf --output /etc/nginx/nginx.conf`
1. `curl https://raw.githubusercontent.com/CptOfEvilMinions/MyLoggingPipeline/master/conf/nginx/splunk_host_web.conf --output /etc/nginx/conf.d/splunk_web.conf`
1. `curl https://raw.githubusercontent.com/CptOfEvilMinions/MyLoggingPipeline/master/conf/nginx/splunk_host_hec_input.conf --output /etc/nginx/conf.d/splunk_hec.conf`
1. `curl https://raw.githubusercontent.com/CptOfEvilMinions/MyLoggingPipeline/master/conf/nginx/splunk_host_api.conf --output /etc/nginx/conf.d/splunk_api.conf`
1. `sed -i 's/192.168.34.80/<IP addr of host>/g' /etc/nginx/conf.d/splunk_*.conf`
1. `sudo systemctl restart nginx && sudo systemctl status nginx`
1. Instead of using `docker-compose ...` you need to use `docker-compose -f docker-compose-no-splunk.yml ...`

## Helpful commands
1. `docker run --rm -it -e SPLUNK_PASSWORD=changeme splunk/splunk:8.0.3-debian create-defaults > conf/splunk/default.yml`
1. `docker network create -d bridge --subnet 192.168.34.0/24 --gateway 192.168.34.1 splunk-bridge-net`

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
* [How To Install Splunk 8.0 On Ubuntu In Just 5 Minutes](https://www.bitsioinc.com/tutorials/install-splunk-ubuntu/)
* [Splunk Enterprise does not start due to unusable filesystem](https://docs.splunk.com/Documentation/Splunk/8.0.3/Troubleshooting/FSLockingIssues)
* [Download Splunk Enterprise 8.0.3 for Linux](https://www.splunk.com/en_us/download/splunk-enterprise/thank-you-enterprise.html)
* [Docker Tip #35: Connect to a Database Running on Your Docker Host](https://nickjanetakis.com/blog/docker-tip-35-connect-to-a-database-running-on-your-docker-host)
* [Access host from a docker container](https://dev.to/bufferings/access-host-from-a-docker-container-4099)
* [Accessing a Localhost Service from Inside a Docker Container](https://serverfault.com/questions/982118/accessing-a-localhost-service-from-inside-a-docker-container)
* [Configuring Nginx With Splunk, REST API &amp; SDK Compatibility](https://www.splunk.com/en_us/blog/tips-and-tricks/configuring-nginx-with-splunk-rest-api-sdk-compatibility.html)
* [Docker Compose Networking](https://runnable.com/docker/docker-compose-networking)
* [Running Splunk In Docker](http://development.wombatsecurity.com/development/2018/08/31/running-splunk-in-docker/)
* [Dockerizing Splunk at Scale 2:](https://static.rainfocus.com/splunk/splunkconf18/sess/1521146368312001VwQc/finalPDF/FN1089_DockerizingSplunkatScale_Final_1538666172485001Loc0.pdf)
* [Splunk Source Connector for Confluent Platform](https://docs.confluent.io/current/connect/kafka-connect-splunk/splunk-source/index.html)