from django.db import models


class Car_category(models.Model):
    NAME_MAX_LEN = 15
    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    def __str__(self):
        return self.name



class WRC_Car(models.Model):
    TITLE_MAX_LEN = 24

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    description = models.TextField()

    rally_class = models.ForeignKey(
        Car_category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
