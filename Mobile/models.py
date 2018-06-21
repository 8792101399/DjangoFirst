from django.db import models

# Create your models here.




class Post(models.Model):
    name = models.CharField(max_length = 400)
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()

    def __str__(self):
        return self.name +"   "  + self.title

class Bill_Database(models.Model):
    Name = models.CharField(max_length = 400)
    Address  = models.CharField(max_length = 400)
    Mobile   = models.CharField(max_length = 200)
    Model = models.CharField(max_length=400)
    Price = models.CharField(max_length=400)
    Discount = models.CharField(max_length=200)
    Gst = models.CharField(max_length=400)

    def __str__(self):
        return self.Name + "     " + self.Mobile + "   " + self.Price



