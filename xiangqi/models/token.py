from django.db import models
from django.utils import timezone

from xiangqi.lib import jwt
from xiangqi.models import User

DEFAULT_TOKEN_LIFE = 3600


class TokenManager(models.Manager):
    def create(self, user, **kwargs):
        created_on = timezone.now()
        expires_on = created_on + timezone.timedelta(seconds=DEFAULT_TOKEN_LIFE)
        payload = {'sub': user.username, 'exp': int(expires_on.timestamp())}
        token_string = jwt.encode(payload).decode()
        kwargs.update(string=token_string, created_on=created_on, expires_on=expires_on)
        return super().create(**kwargs)

    def bulk_create(self, *args, **kwargs):
        raise NotImplementedError('Bulk token creation not allowed')

    def save(self, *args, **kwargs):
        raise NotImplementedError('Token editing not allowed')


class Token(models.Model):
    objects = TokenManager()

    string = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField()
    expires_on = models.DateTimeField()

    # TODO: add to user manager (requires users proxy class)
    def get_user(self):
        user_info = jwt.decode(self.string)
        return User.objects.get(username=user_info['sub'])
