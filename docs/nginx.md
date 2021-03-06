# NGINX
Logstash is the frontend to the logging for ingest logs from client. Logstash was picked because there is a plethora of plugins, documentation, and support for this tool.

## Generate OpenSSL cert
1. `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout conf/nginx/ssl/nginx.key -out conf/nginx/ssl/nginx.crt`

## Generate DHparam
1. `openssl dhparam -out conf/nginx/ssl/dhparam.pem 2048`

## Build logstash
1. `docker-compose build nginx`

## References
* [plentz/nginx.conf](https://gist.github.com/plentz/6737338)
* [nginx as reverse proxy with upstream SSL](https://serverfault.com/questions/341023/nginx-as-reverse-proxy-with-upstream-ssl)
* []()
* []()
* []()
* []()
* []()