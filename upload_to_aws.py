import boto3

import config


def create_s3_client() -> boto3.client:
    """_summary_

    Returns:
        boto3.client: _description_
    """
    # AWS config variables
    AWS_ACCESS_KEY_ID = config.aws_access_key_id
    AWS_SECRET_ACCESS_KEY = config.aws_secret_access_key
    REGION_NAME = config.region_name


    # Create a S3 cliet with the config crendentials
    s3 = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=REGION_NAME)
    return s3


def upload_file_to_s3(s3: boto3.client) -> None:
    """_summary_

    Args:
        s3 (boto3.client): _description_
    """
    # Upload file to S3 bucket
    file_name = config.filename
    bucket_name = config.bucket_name
    object_name = f"{config.object_name}/{file_name}"
    s3.upload_file(file_name, bucket_name, object_name)


def run_upload_to_s3():
    s3 = create_s3_client()
    upload_file_to_s3(s3)


if __name__ == "__main__":
    run_upload_to_s3()