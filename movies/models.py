from django.db import models

class movies(models.Model):
    Movie_Icon = models.ImageField(upload_to='images/')
    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    Movie_File = models.FileField(upload_to='videos/')
    Client = models.CharField(max_length=50)
    Project_Manager = models.CharField(max_length=50)
    Creation_Date = models.DateField(auto_now_add=True)
    Modified_Date = models.DateField(auto_now=True)

    def __str__(self):
        return self.Name
