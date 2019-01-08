import boto3
import json

__author__ = "Venkata.Sai.Kateppalli<venkatasai.k@codejukers.in>"
__version__ = "1.0"

def list_buckets():
    s3=boto3.resource('s3')
    buckets = []
    for idx, bucket in enumerate(s3.buckets.all()):
        buckets.append({
            'id': idx + 1,
            'name': bucket._name
        })
    return json.dumps(buckets)