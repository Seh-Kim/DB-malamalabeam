from django.db import models
from user.models import CustomUser

# Create your models here.

class Store(models.Model): 
    store_id = models.CharField(max_length=20, primary_key=True)
    store_name = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20)
    rating = models.FloatField(max_length=20)
    image = models.ImageField(upload_to="review/", blank=True, null=True)
    phone_num = models.CharField(max_length=20)

class Bookmark(models.Model): 
    bookmark_id = models.CharField(max_length=20, primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)

class Review(models.Model): 
    review_id = models.CharField(max_length=20, primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    content = models.CharField(max_length=500, null=False)
    rating = models.FloatField(max_length=20, null=False)
    image = models.ImageField(upload_to="review/", blank=True, null=True)
    review_date = models.DateTimeField()
    class Meta:
        ordering = ['review_date']
        
class Comment(models.Model): 
    comment_id = models.CharField(max_length=20, primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=500, null=False)
    comment_date = models.DateTimeField()
    class Meta:
        ordering = ['comment_date']