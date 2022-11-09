import os
import pytest
import comp630
import boto3
from moto import mock_s3

TEST_BUCKET = "comp630-m1-f22-proftim"
TEST_FILE = "fip1001.moto"

@mock_s3
def test_upload():
    global TEST_BUCKET
    global TEST_FILE

    conn = boto3.client("s3", region_name="us-east-1")

    conn.create_bucket(Bucket=TEST_BUCKET)
    with open(TEST_FILE, "rb") as  f:
        object_name = os.path.basename(f.name)
        comp630.to_the_cloud(f.name, TEST_BUCKET, TEST_FILE)

    assert True
