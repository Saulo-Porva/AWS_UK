import boto3
import json
from fake_web_events import Simulation


client = boto3.client(
    aws_access_key_id="AKIAXWISTEIKUDR76SUC",
    aws_secret_access_key="+9GWreJJMRDUUxErKqT27f5n01AMOxMEo44cuM1r"
)

#client = boto3.client('firehose')


def put_record(event):
    data = json.dumps(event) + "\n"
    response = client.put_record(
        DeliveryStreamName='kinesis-firehose-bootcamp',
        Record={"Data": data}
    )
    print(event)
    return response


simulation = Simulation(user_pool_size=100, sessions_per_day=10000)
events = simulation.run(duration_seconds=300)

for event in events:
    put_record(event)

