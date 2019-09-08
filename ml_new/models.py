from django.db import models

# Create your models here.

class plot_img(models.Model):
    image=models.ImageField(upload_to='plot_img',blank=True,null=True)