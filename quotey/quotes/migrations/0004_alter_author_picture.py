# Generated by Django 4.1.5 on 2023-01-20 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_author_grad_year_author_picture_quote_quoted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(default='./static/quotes/pp.png', upload_to=''),
        ),
    ]
