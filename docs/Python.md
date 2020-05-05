# Python connector script

1. `venv -p python3 venv`
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

## Entire setup
1. `python3 splunk-kafka-connector.py --all`

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
* [Optional arguments in a function [closed]](https://codereview.stackexchange.com/questions/148153/optional-arguments-in-a-function)
* [Github issue - consumer group not being deleted on deletion of a connector](https://github.com/confluentinc/kafka-connect-elasticsearch/issues/267)
* [Edit an HTTP Event Collector token using cURL](https://docs.splunk.com/Documentation/Splunk/8.0.3/Data/HTTPEventCollectortokenmanagement)
* []()
* []()
* []()