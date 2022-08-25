from django.db import models


class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    content = models.TextField()
    cover = models.ImageField(upload_to='upload')
    user = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)


    class Meta:
        unique_together = ['article']
        ordering = ['created']

    def __str__(self):
        return '%s' % (self.content)
