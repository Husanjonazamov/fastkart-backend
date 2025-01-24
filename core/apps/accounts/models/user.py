from django.contrib.auth import models as auth_models
from django.db import models

from ..choices import RoleChoice
from ..managers import UserManager


class User(auth_models.AbstractUser):
    phone = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    validated_at = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=10)
    profile_image = models.ForeignKey(
        "content.ImageModel", on_delete=models.SET_NULL, null=True, blank=True
    )
    system_reserve = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_users",
    )
    email_verified_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    orders_count = models.IntegerField(default=0)
    store = models.ForeignKey(
        "product.StoreModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )
    wallet = models.OneToOneField(
        "core.WalletsModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="consumer",
    )
    vendor_wallet = models.OneToOneField(
        "core.WalletsModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vendors",
    )
    role = models.ForeignKey(
        "Role", on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )

    USERNAME_FIELD = "phone"
    objects = UserManager()

    def __str__(self):
        return self.phone




class Role(models.Model):
    name = models.CharField(max_length=255)
    guard_name = models.CharField(max_length=255)
    system_reserve = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pivot = models.ForeignKey(
        "Pivot", on_delete=models.SET_NULL, null=True, blank=True, related_name="roles"
    )

    def __str__(self):
        return self.name


class Pivot(models.Model):
    model = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="pivots"
    )
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True, related_name="pivots"
    )
    model_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.model_type} - {self.role.name}"
