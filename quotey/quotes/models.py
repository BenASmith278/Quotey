from django.db import models
import django.utils.timezone as tz

# A model for authors
class Author(models.Model):
    name = models.CharField(max_length=50)  # name
    grad_year = models.IntegerField("class", default=26)  # class
    picture = models.ImageField(default='./static/quotes/pp.png')  # picture

    def __str__(self):
        return self.name

# A model for quotes
# Quotes are linked to authors
class Quote(models.Model):
    quote_text = models.CharField(max_length=250)  # text
    pub_date = models.DateTimeField("date published", default=tz.now)  # date published
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # author
    quoted = models.DateTimeField("date quoted", null=True)  # date created

    def __str__(self):
        return self.quote_text
