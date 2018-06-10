from django.db import models

# Create your models here.
class mainInfo(models.Model):
    author = models.CharField(max_length= 150) # name of author
    author_bio = models.CharField(max_length= 1000) # description of author
    author_linkedIn =  models.CharField(max_length= 1000) # link to linkedIn
    author_facebook = models.CharField(max_length=1000)  # link to facebook

    def __str__(self):
        return (self.author, self.author_bio)

