from django.db import models

class User(models.Model):
    TTL_SUPERUSER = (
        (0, 'No'),
        (1, 'Yes'),
    )

    TTL_ACTIVE = (
        (0, 'Inactive'),
        (1, 'Active'),
    )

    TTL_SIGNED = (
        (0, 'No'),
        (1, 'Yes'),
    )
    id = models.AutoField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_superuser = models.SmallIntegerField(choices=TTL_SUPERUSER, default=0)
    is_active = models.SmallIntegerField(choices=TTL_ACTIVE, default=0)
    contract_signed  = models.SmallIntegerField(choices=TTL_SIGNED, default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_at = models.DateTimeField(auto_now=True, editable=False)
