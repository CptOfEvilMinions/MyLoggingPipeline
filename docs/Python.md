# Python connector script

1. `pip3 install -U requests`
1. 
```
python3 splunk-kafka-connector.py \
--splunk_connector_name splunk-zeek \
--splunk_hec_uri http://splunk:8088 \
--splunk_hec_token <token> \
--kafka_connect_url http://10.140.100.221:8083/connectors \
--kafak_topics_list zeek_conn
```

## References
* [How to Build Command Line Interfaces in Python With argparse](https://realpython.com/command-line-interfaces-python-argparse/)
* [Python Post JSON using requests library](https://pynative.com/python-post-json-using-requests-library/)