from django.conf import settings
from django.db import models
from django.utils import timezone

# `models.Model`` means that the Post is a Django Model, so Django knows 
# that it should be saved in the database.
class Post(models.Model):

    # https://docs.djangoproject.com/en/5.1/ref/models/fields/#field-types

    # models.ForeignKey – this is a link to another model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # models.CharField – this is how you define text with a limited number of 
    # characters.
    title = models.CharField(max_length=200)

    # models.TextField – this is for long text without a limit.
    text = models.TextField()

    # models.DateTimeField – this is a date and time.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title