import os

from dotenv import load_dotenv


load_dotenv()

# Configurar api
api_key = os.getenv("API_KEY")
language = "pt-BR"

filename = "movies_top_rated_tmdb.csv"

# Config AWS crendentials
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region_name = os.getenv("REGION_NAME")

# S3 Bucket
bucket_name = os.getenv("BUCKET_NAME")
object_name = os.getenv("OBJECT_NAME")