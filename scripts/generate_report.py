import boto3
import json
import argparse
from jinja2 import Environment, FileSystemLoader

def fetch_data_from_s3(bucket, prefix):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    data = []
    for obj in response.get('Contents', []):
        obj_data = s3.get_object(Bucket=bucket, Key=obj['Key'])
        data.append(json.loads(obj_data['Body'].read().decode('utf-8')))
    return data

def generate_report(data, output_file):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')
    rendered = template.render(data=data)
    with open(output_file, 'w') as f:
        f.write(rendered)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Disk Utilization Report")
    parser.add_argument('--bucket', required=True, help='S3 bucket name')
    parser.add_argument('--output', required=True, help='Output HTML file')
    args = parser.parse_args()

    data = fetch_data_from_s3(args.bucket, 'disk_utilization/')
    generate_report(data, args.output)
