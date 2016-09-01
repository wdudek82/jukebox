from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Soundcode(models.Model):
    symbol = models.CharField(max_length=1, unique=True)
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Soundcode'
        verbose_name_plural = 'Soundcodes'
        ordering = ('title',)


class Song(models.Model):
    TEMPO_LIST = (
        ('SS', 'ad lib-60'),
        ('SM', '61-81'),
        ('SF', '82-89'),

        ('MS', '90-97'),
        ('MM', '98-106'),
        ('MF', '107-118'),

        ('FS', '119-124'),
        ('FM', '125-130'),
        ('FF', '131-inf.'),
    )

    MOOD = ((num, num) for num in range(1,6))
    ENERGY = ((num, num) for num in range(1,6))

    song_id = models.CharField(max_length=15, unique=True)
    # cover = models.CharField(max_length=15) # same as song_id :?
    artist_1 = models.ForeignKey('playlist.Artist', related_name='artist1')
    artist_2 = models.ForeignKey('playlist.Artist', related_name='artist2', blank=True)
    title = models.CharField(max_length=50)
    soundcode = models.ManyToManyField(Soundcode)
    mood = models.IntegerField(choices=MOOD, default=1)
    energy = models.IntegerField(choices=ENERGY, default=1)
    tempo = models.CharField(max_length=2, choices=TEMPO_LIST, default='SS')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.song_id
