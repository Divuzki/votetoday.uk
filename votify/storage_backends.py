from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class CachedS3BotoStorage(S3Boto3Storage):
    """
    S3BotoStorage backend which also saves a hashed copies of the files it saves.
    """
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    custom_domain = settings.STATIC_URL


class StaticStorage(S3Boto3Storage):
    location = settings.STATIC_LOCATION
    default_acl = 'public-read'
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    custom_domain = settings.AWS_S3_CUSTOM_DOMAIN
