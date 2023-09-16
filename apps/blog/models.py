from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(_('Post title'), max_length=256)
    photo = models.ImageField(_('Post photo'), upload_to='images/blog/posts/%Y/%m/')
    content = RichTextUploadingField(_('Post content'))

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE, verbose_name=_('Post'))
    full_name = models.CharField(_('Full name'), max_length=256)
    email = models.EmailField(_('Email'), blank=True, null=True)
    comment = RichTextField(_('Comment'))

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return f'{self.full_name}\'s comment on {self.post}'
