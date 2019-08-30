from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	major = models.CharField('Major', max_length=255)
	grad_year = models.CharField('Graduation Year', max_length=255)
	classes = models.CharField('Class for Partner', max_length=255)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
	resume = models.FileField(upload_to='resumes', blank=True)
	portfolio_site = models.URLField(blank=True)

def __str__(self):
  return self.user.username