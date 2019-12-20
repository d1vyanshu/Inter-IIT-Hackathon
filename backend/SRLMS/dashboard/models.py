from django.db import models
from authentication.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_posts')
    image = models.ImageField(upload_to='images', default=None, null=False)
    description = models.TextField()
    date_posted = models.DateField(auto_now_add = True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    upvoters = models.ManyToManyField(User, related_name='upvoted_posts')
    downvoters = models.ManyToManyField(User, related_name='downvoted_posts')
    is_resolved = models.BooleanField(default=False)
    x_coordinate = models.FloatField(null=False, blank=False)
    y_coordinate = models.FloatField(null=False, blank=False)


    def __str__(self):
        return '{} Post'.format(self.author)
