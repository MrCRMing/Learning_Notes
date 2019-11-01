from django.db import models


# Create your models here.

class Cat(models.Model):
    class Meta:
        db_table = "catInfo"
        ordering = ('created_at',)

    BLACK = 'BLK'
    WHITE = 'WHE'
    GREY = 'GRY'
    BROWN = "BRW"
    RED = "RED"
    COLORS = (
        (BLACK, 'black'),
        (WHITE, 'white'),
        (GREY, 'grey'),
        (BROWN, 'brown'),
        (RED, 'red')
    )

    HAPPY = "HAY"
    GRUMPY = "GRY"
    BAD = "BAD"
    MOODS = (
        (HAPPY, "happy"),
        (GRUMPY, "grumpy"),
        (BAD, "bad"),
    )

    owner = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=50, blank=True)
    colors = models.CharField(max_length=3, choices=COLORS, default=BLACK)
    age = models.IntegerField(blank=True)
    photo = models.URLField(blank=True)
    toy = models.CharField(max_length=50, blank=True)
    mood = models.CharField(max_length=3, choices=MOODS, default=HAPPY)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s -- %s -- %d' % (self.name, self.owner, self.age)
