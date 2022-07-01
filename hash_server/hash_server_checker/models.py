from django.db import models
import hashlib
from django.dispatch import receiver
from django.db.models.signals import pre_save
class save_data(models.Model): #save word with its hashes
    
    word = models.CharField(max_length=16)
    md5_hash = models.CharField(max_length=32,null=True,blank=True)
    sha256_hash = models.CharField(max_length=64,null=True,blank=True)
    sha224_hash = models.CharField(max_length=120,null=True,blank=True)


    def __str__(self):
        return self.word

@receiver(pre_save, sender=save_data)
def _pre_save_receiver(sender,instance, **kwargs):
    word = instance.word
    word = word.encode()
    instance.md5_hash = hashlib.md5(word).hexdigest()
    instance.sha256_hash = hashlib.sha256(word).hexdigest()
    instance.sha224_hash = hashlib.sha224(word).hexdigest()

