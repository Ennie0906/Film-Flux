# Generated by Django 4.2.7 on 2023-12-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("films", "0002_rename_ingredients_films_review_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="films",
            name="film_type",
            field=models.CharField(
                choices=[
                    ("action", "Action"),
                    ("comedy", "Comedy"),
                    ("thriller", "Thriller"),
                    ("horror", "Horror"),
                    ("adventure", "Adventure"),
                    ("thriller", "Thriller"),
                    ("anime", "Anime"),
                    ("war", "War"),
                    ("drama", "Drama"),
                    ("romance", "Romance"),
                    ("family", "Family"),
                    ("documentary", "Documentary"),
                    ("science fiction", "Science Fiction"),
                    ("war", "War"),
                    ("western", "Western"),
                    ("tv show", "TV Show"),
                ],
                default="comedy",
                max_length=50,
            ),
        ),
    ]
