from django.db import models

class MoviePetition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class PetitionVote(models.Model):
    petition = models.ForeignKey(MoviePetition, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vote for {self.petition.title}"