from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Brand(TimeStampedModel):
    title = models.CharField(_('Brand title'), max_length=128)
    description = models.TextField(_('Brand description'))
    logo = models.ImageField(_('Brand logo'), upload_to='images/brands/%Y/%m/')

    is_new = models.BooleanField(_('New status'), default=True)
    is_popular = models.BooleanField(_('Popular status'), default=False)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.title


class Category(TimeStampedModel):
    title = models.CharField(_('Category title'), max_length=128)
    description = RichTextField(_('Description'), blank=True, null=True)
    icon = models.ImageField(_('Category icon'), upload_to='images/store/categories/icons')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Collection(TimeStampedModel):
    title = models.CharField(_('Collection title'), max_length=256)
    description = RichTextField(_('Description'), blank=True, null=True)
    photo = models.ImageField(_('Collection photo'), upload_to='images/collections/%Y/%m/')

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')

    def __str__(self):
        return self.title


class SkinType(models.Model):
    title = models.CharField(_('Skin type title'), max_length=128)

    class Meta:
        verbose_name = _('Skin type')
        verbose_name_plural = _('Skin types')

    def __str__(self):
        return self.title


class Product(TimeStampedModel):
    vendor_code = models.PositiveIntegerField(_('Vendor code'), unique=True)

    brand = models.ForeignKey('store.Brand', related_name='products', on_delete=models.PROTECT, verbose_name=_('Brand'))
    category = models.ForeignKey('store.Category', related_name='products', on_delete=models.PROTECT, verbose_name=_('Category'))
    collections = models.ManyToManyField('store.Collection', related_name='products', blank=True, verbose_name=_('Collections'))

    title = models.CharField(_('Product title'), max_length=256)
    description = RichTextField(_('Product description'))
    application = RichTextField(_('Application'))
    ingredients = models.TextField(_('Ingredients'))
    skin_types = models.ManyToManyField('store.SkinType', related_name='products', blank=True, verbose_name=_('Suitable skin types'))

    price = models.PositiveIntegerField(_('Product price'))
    discount = models.PositiveIntegerField(_('Discount'), default=0, validators=[MaxValueValidator(100)])
    rating = models.DecimalField(_('Product rating'), max_digits=2, decimal_places=1, default=0, blank=True, null=True)

    purchase_count = models.PositiveIntegerField(_('Purchase count'), default=0)
    views = models.PositiveIntegerField(_('Views count'), default=0)

    is_new = models.BooleanField(_('New status'), default=True)
    is_hit = models.BooleanField(_('Hit status'), default=False)
    is_bestseller = models.BooleanField(_('Bestseller status'), default=False)
    is_tiktok = models.BooleanField(_('TikTok product status'), default=False)
    is_miniature = models.BooleanField(_('Miniature status'), default=False)

    popularity = models.DecimalField(_('Popularity'), max_digits=24, decimal_places=2, default=0)

    is_available = models.BooleanField(_('Available status'), default=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        indexes = [
            models.Index(fields=['title'])
        ]

    def delete(self, *args, **kwargs):
        for photo in self.photos.all():
            photo.delete()
        super(self, Product).delete(*args, **kwargs)

    def __str__(self):
        return self.title


class Photo(models.Model):
    product = models.ForeignKey('store.Product', related_name='photos', on_delete=models.PROTECT, verbose_name=_('Product'))
    photo = models.ImageField(_('Photo'), upload_to='images/store/products/%Y/%m/')
    ordinal_number = models.PositiveIntegerField(_('Ordinal number'), blank=True, null=True)

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
        unique_together = ['product', 'ordinal_number']
        ordering = ['ordinal_number']

    def __str__(self):
        return f'{self.product.title} - {self.pk}'


class Video(models.Model):
    product = models.ForeignKey('store.Product', related_name='videos', on_delete=models.PROTECT, verbose_name=_('Product'))
    video = models.FileField(_('Video'), upload_to='videos/store/products/%Y/%m/')
    ordinal_number = models.PositiveIntegerField(_('Ordinal number'), blank=True, null=True)

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
        unique_together = ['product', 'ordinal_number']
        ordering = ['ordinal_number']

    def __str__(self):
        return f'{self.product.title} - {self.pk}'


class Review(TimeStampedModel):
    user = models.ForeignKey('accounts.User', related_name='reviews', on_delete=models.SET_NULL, null=True, verbose_name=_('Reviewer user'))
    product = models.ForeignKey('store.Product', related_name='reviews', on_delete=models.CASCADE, verbose_name=_('Reviewed product'))
    rating = models.PositiveIntegerField(_('Rating'), validators=[MaxValueValidator(5, message=_('Max rating is 5'))])
    review = models.CharField(_('Review'), max_length=512, blank=True, null=True)

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        unique_together = ['user', 'product']

    def __str__(self):
        return f'Review by {self.user} on {self.product}'
