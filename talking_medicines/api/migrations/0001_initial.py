# Generated by Django 4.1 on 2023-05-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("author", models.CharField(max_length=255)),
                (
                    "author_flair_text",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "author_flair_text_color",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                ("body", models.TextField()),
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("permalink", models.CharField(max_length=255)),
                ("score", models.IntegerField()),
                ("subreddit", models.CharField(max_length=255)),
            ],
        ),
    ]
