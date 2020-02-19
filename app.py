from config import app
from config import ACCESS_KEY,SECRET_KEY
import routes
import boto3

s3 = boto3.client(
"s3",
aws_access_key_id=ACCESS_KEY,
aws_secret_access_key=SECRET_KEY
)
bucket_resource = s3

if __name__ == "__main__":
    app.run(debug=True)