# Generated by Django 4.1 on 2023-07-31 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_authors_alter_article_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='articles.author'),
        ),
    ]
