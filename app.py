from api_to_csv import api_to_csv
from upload_to_aws import run_upload_to_s3


# Run the scripts
print("Getting movies from TMDB API...")
api_to_csv()
print("Uploading to S3...")
run_upload_to_s3()
print("Completed.")