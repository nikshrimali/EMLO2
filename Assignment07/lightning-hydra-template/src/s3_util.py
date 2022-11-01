import boto3
import botocore


class S3download:
    def __init__(self, bkt):
        self.bucket = boto3.resource("s3").Bucket(bkt)

    def download_model(self, key, out_file):
        try:
            self.bucket.download_file(key, out_file)

        except botocore.exceptions.ClientError as err:
            if err.response["Error"]["Code"] == "404":
                self.log.info("The object does not exist.")
            else:
                raise


if __name__ == "__main__":
    BUCKET_NAME = "emlo"
    model_name = "model.script.pt"
    destination_file = "/opt/src/model.script.pt"
    s3_connect = S3download(BUCKET_NAME)
    s3_connect.download_model(model_name, destination_file)