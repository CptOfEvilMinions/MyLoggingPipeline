"""
Author: Ben Bornholm
"""
from datetime import datetime
import argparse
import requests
import json


def create_kafka_splunk_connector(args):
    headers = {
        "Content-Type": "application/json"
    }

    json_data = {
        "name": f"{args.splunk_connector_name}",
        "config": {
            "connector.class": "com.splunk.kafka.connect.SplunkSinkConnector",
            "tasks.max": "10",
            "topics": f"{args.kafak_topics_list}",
            "splunk.hec.uri":f"{args.splunk_hec_uri}",
            "splunk.hec.token": f"{args.splunk_hec_token}",
            "splunk.hec.ack.enabled": "true",
            "splunk.hec.raw": "false",
            "splunk.hec.json.event.enrichment": "org=fin,bu=south-east-us",
            "splunk.hec.track.data": "true"
        }
    }


    r = requests.post(args.kafka_connect_url, headers=headers, json=json.dumps(json_data))

    print (r.json)

    if r.status_code == 200:
        print ( f"[+] - {datetime.now()} - Instantiated connector between Splunk and Kafka for {args.kafak_topics_list}" )

def create_splunk_index():
    pass


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    # Splunk
    my_parser.add_argument('--splunk_connector_name', action='store', type=str, required=True, help='Enter Splunk HEC URI')
    my_parser.add_argument('--splunk_hec_uri', action='store', type=str, required=True, help='Enter Splunk HEC URI')
    my_parser.add_argument('--splunk_hec_token', action='store', type=str, required=True, help='Enter Splunk HEC token')
    
    # Kafka
    my_parser.add_argument('--kafka_connect_url', action='store', type=str, required=True, help='Enter Kafka connect URL')
    my_parser.add_argument('--kafak_topics_list', action='store', type=str, required=True, help='Enter Kafka topics to pull data from in list format [t1,t2,t3]')
    args = my_parser.parse_args()

    create_kafka_splunk_connector(args)