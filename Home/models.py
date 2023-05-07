from django.db import models

# Create your models here.

class File(models.Model):
    file= models.FileField(upload_to="files")


class Form(models.Model):
      name = models.CharField(max_length=122)
      email = models.CharField(max_length=122)
      phone = models.CharField(max_length=12)
      education = models.CharField(max_length=122)
      experience = models.CharField(max_length=122)
      skills = models.CharField(max_length=122)

      def __str__(self):
        return self.name
