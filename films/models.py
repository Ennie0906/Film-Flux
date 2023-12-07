from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField

# Create your models here.


# Film Types
FILM_TYPES = [
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
]



class Films(models.Model):

    """A model to leave reviews"""

    user = models.ForeignKey(
        User, related_name="film_reviewer", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    review = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="films/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    film_type = models.CharField(max_length=50, choices=FILM_TYPES, default="comedy")
    rating = models.IntegerField()
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)
