# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

MENUS_URL = '/menus'


class MenuFrame(models.Model):

    name = models.CharField(max_length=32)
    ancestor = models.ForeignKey('self', null=True, blank=True)
    url = models.CharField('url', max_length=140, blank=True, editable=False)
    level = models.IntegerField('level', default=0, editable=False)

    def save(self, **kwargs):
        if self.ancestor:
            self.level = self.ancestor.level + 1
            self.url = ''.join([self.ancestor.url, '/', self.name])
        else:
            if not self.pk:
                super(MenuFrame, self).save(**kwargs)
            self.level = 0
            self.url = ''.join([MENUS_URL, '/', self.name])
        super(MenuFrame, self).save(**kwargs)

    def delete(self, using=None, keep_parents=False):
        super(MenuFrame, self).delete()

    def children(self):
        _children = MenuFrame.objects.filter(ancestor=self).order_by('id', )
        for child in _children:
            child.ancestor = self
        return _children

    def has_children(self):
        return self.children().count() > 0

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'menu_frame'
        verbose_name = 'menu_frame'
        verbose_name_plural = 'menu_frames'
