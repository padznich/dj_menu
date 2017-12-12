# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from tree.models import MenuFrame


register = template.Library()


def show_frames(context, path):

    root_menus = MenuFrame.objects.filter(level=0)
    main_frame = dict((menu, None) for menu in root_menus)
    context['main_frame'] = main_frame
    return context


register.inclusion_tag('menu.html', takes_context=True)(show_frames)
