
import frappe
import boto3
from frappe_s3_attachment.controller import S3Operations

def debug():
    try:
        doc = frappe.get_doc('S3 File Attachment', 'S3 File Attachment')
        print(f"Region in Doc: {doc.region_name}")
        print(f"Bucket: {doc.bucket_name}")
        
        s3_ops = S3Operations()
        print(f"Boto3 Client Region: {s3_ops.S3_CLIENT.meta.region_name}")
        print(f"Boto3 Client Endpoint: {s3_ops.S3_CLIENT.meta.endpoint_url}")
        
        url = s3_ops.get_url('test_key', 'test.jpg')
        print(f"Generated URL: {url}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    frappe.connect()
    debug()
