from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='static/')
    description=models.TextField()
    url=models.TextField()
    date=models.DateTimeField()
    icon=models.ImageField(upload_to='images/')
    votes_total=models.IntegerField(default=1)
    likes=models.ManyToManyField(User,related_name="likes",blank=True)
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def summery(self):
        return self.description[:200]
    def pub_date(self):
        return self.date.strftime('%b %d %Y')
