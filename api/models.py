from django.db import models
from django.contrib.auth.models import User


# For Managing User Profile Picture
class UserProfilePhoto(models.Model):
    sno = models.AutoField(primary_key=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="profilePhotos")
    user = models.ForeignKey(User,on_delete=models.CASCADE) # associated with an user


#For Managing Video Data
class VideoData(models.Model):
    sno = models.AutoField(primary_key=True)
    video_title = models.TextField(max_length=1000)
    video_desc = models.TextField(max_length=5000)
    video_likes = models.IntegerField(default=0)
    video_views = models.IntegerField(default=0)
    video_file = models.FileField(upload_to="videoFiles",null=False)
    notes_file = models.FileField(upload_to="notesFiles",null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) # associated with an user
    # upload_date 




   