from django.db import models

class Hotel(models.Model):
    TYPE_CHOICES = [
        ('5-star', '5-Star'),
        ('4-star', '4-Star'),
        ('3-star', '3-Star'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    overview = models.TextField()
    location = models.CharField(max_length=255)
    photos = models.JSONField()
    

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    room_type = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - {self.hotel.name}"
