from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        from PIL import Image
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
        

@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    print('create_profile signal triggered')
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userprofile(sender, instance, **kwargs):
    instance.userprofile.save()