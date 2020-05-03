# Python connector script

1. `pip3 install -U requests`
1. 
```
cat > ~/.splunkrc << 'EOF'
# Splunk host (default: localhost)
host=<Splnk IP addr/hostname>
# Splunk admin port (default: 8089)
port=8089
# Splunk username
username=admin
# Splunk password
password=<password>
# Access scheme (default: https)
scheme=http
# Your version of Splunk (default: 5.0)
version=8.0.3
```


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
* [Splunk SDK for Python: Getting Data In](https://www.function1.com/2015/09/splunk-sdk-for-python-getting-data-in)
* [Python String startswith() Method](https://www.tutorialspoint.com/python/string_startswith.htm)
* [Use Python SDK to export data](https://docs.splunk.com/Documentation/Splunk/8.0.3/Search/ExportdatausingSDKs)
* [splunklib.client](https://docs.splunk.com/DocumentationStatic/PythonSDK/1.6.5/client.html#splunklib.client.Indexes.delete)
* [Suppress SSL certificate warnings when ssl_verify=False is set? #240](https://github.com/influxdata/influxdb-python/issues/240)
* [Python Objects and Class](https://www.programiz.com/python-programming/class)
* [Splunk HTTP collector python script](https://ridingintraffic.github.io/blog/splunk-hec-python/)
* [How to get data into Splunk Enterprise using the Splunk Enterprise SDK for Python](https://dev.splunk.com/enterprise/docs/python/sdk-python/howtousesplunkpython/howtogetdatapython/)
* [Splunk docs - Getting Data In](https://docs.splunk.com/Documentation/Splunk/8.0.3/Data/HTTPEventCollectortokenmanagement)
* [Splunk Docs - REST API Tutorials](https://docs.splunk.com/Documentation/Splunk/8.0.3/RESTTUT/RESTandCloud)
* [Configure data collection using your Python code](https://docs.splunk.com/Documentation/AddonBuilder/3.0.1/UserGuide/ConfigureDataCollectionAdvanced)
* [splunk-sdk-python/examples/index.py](https://github.com/splunk/splunk-sdk-python/blob/master/examples/index.py)
* []()
* []()
* []()
* []()
* []()
* []()