from django.db.models import Model, CharField, SlugField, ForeignKey, CASCADE, TextField, DateTimeField
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = CharField(max_length=250)
    slug = SlugField(max_length=250, unique_for_date='publish')
    author = ForeignKey(User, on_delete=CASCADE, related_name='blog_post')
    body = TextField()
    publish = DateTimeField(default=timezone.now)
    created = DateTimeField(auto_now_add=True)
    update = DateTimeField(auto_now=True)
    status = CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

