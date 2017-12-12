# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def show_menus(request, *args, **kwargs):

    path_args = [i for i in request.path.split('/') if i]
    context = {
        'menu_path_list': path_args,
    }

    return render(request, 'base.html', context)
