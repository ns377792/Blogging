from django.db import models

# Create your models here.
class shorturl(models.Model):
    original_url = models.URLField(blank=False)
    short_query = models.CharField(blank=False, max_length=16)
    visits = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.short_query+" - "+str(self.visits)