from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from django.utils.text import slugify
from core.apps.product.models import TagsModel



class BlogModel(AbstractBaseModel):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(unique=True)
    descriptions = models.TextField()
    content = models.TextField()
    meta_title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    is_sticky = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True) 
    created_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    blog_thumbnail = models.ForeignKey(
        'content.ImageModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blog_thumbnails'
        )
    blog_meta_image = models.ForeignKey(
        'content.ImageModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blog_meta_images'
        )
    categories = models.ManyToManyField('product.CategoryModel')
    tags = models.ManyToManyField(TagsModel, related_name='blog')
    
    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Blog"
        verbose_name = _("BlogModel")
        verbose_name_plural = _("BlogModels")
