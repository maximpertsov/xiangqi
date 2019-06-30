from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


class PlayerManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(user__username=username)


class Player(models.Model):
    objects = PlayerManager()

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1500)

    def get_username(self):
        return self.user.username

    def natural_key(self):
        return self.get_username()

    natural_key.dependencies = [User._meta.app_label + '.' + User._meta.model_name]

    def __str__(self):
        return self.get_username()


@receiver(post_save, sender=get_user_model())
def create_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)


@receiver(post_save, sender=get_user_model())
def save_player(sender, instance, **kwargs):
    instance.player.save()