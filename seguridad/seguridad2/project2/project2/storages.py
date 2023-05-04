from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


#class MediaStore(S3Boto3Storage):
 #   location = 'media'
  #  file_overwrite = False


class MediaStore(S3Boto3Storage):
    location = 'media'
    default_acl = 'private'
    file_overwrite = False
    AWS_STORAGE_BUCKET_NAME = 'cloudseguridad'
    custom_domain = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    encrypt_key = True
    kms_key_id = getattr(settings, 'MEDIASTORE_ENCRYPTION_KEY_ID', None)
    kms_key_region = getattr(settings, 'MEDIASTORE_ENCRYPTION_KEY_REGION', None)
