from django.db import models


# Create your models here.
class author(models.Model):
    author_name = models.CharField(max_length= 150) # name of author

    def __str__(self):
        return self.author_name

class authorInfo(models.Model):
    author_name = models.ForeignKey(author, on_delete= models.CASCADE)
    author_bio = models.CharField(max_length=1000)  # description of author
    author_linkedIn = models.CharField(max_length=1000)  # link to linkedIn
    author_facebook = models.CharField(max_length=1000)  # link to facebook

    def __str__(self):
        return self.author_bio
