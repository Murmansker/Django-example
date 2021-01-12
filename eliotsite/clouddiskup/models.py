from django.db import models

class Uploader(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class File(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    uploader = models.ForeignKey(Uploader, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline