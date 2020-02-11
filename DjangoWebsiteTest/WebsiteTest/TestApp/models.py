from django.db import models


# Create your models here.
class Comment(models.Model):
    author = models.TextField()
    body = models.TextField()
    postDate = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    class Meta:
        # Sort comments chronologically
        ordering = ['-postDate']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)

