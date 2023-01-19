from django.db import models

# A model for authors
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# A model for quotes
# Quotes are linked to authors
class Quote(models.Model):
    quote_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField(verbose_name="date published")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote_text
