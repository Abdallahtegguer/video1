from django.db import models
from django.utils import timezone
import boto3
import os 



#def user_directory_path(instance, filename):
  #  key = kms.generate_data_key(KeyId=AWS_KMS_KEY_ID, KeySpec='AES_256')
  #  encrypted_filename = key['CiphertextBlob'] + filename.encode()
  #  return 'posts/{0}/{1}'.format(instance.id, encrypted_filename)

import uuid

def user_directory_path(instance, filename):
    filename, ext = os.path.splitext(filename)
    return 'posts/{0}/{1}.encrypted'.format(uuid.uuid4(), filename)



    
class Post(models.Model):
    title= models.CharField(max_length=250)
    image= models.ImageField(upload_to=user_directory_path)
    image_caption= models.CharField(max_length=100, default='photo by demo')
    publish= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Create your models here.
