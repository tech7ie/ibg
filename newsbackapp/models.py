from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ForeignKey('Images', related_name='news_items', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}\n{self.text}"
    
class Images(models.Model):
    news = models.ForeignKey(News, related_name='images', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/')