#-*- coding:utf-8 -*-

from django.shortcuts import redirect, get_object_or_404

from banner_rotator.models import Banner


def click(request, banner_id, place_slug):
    banner = get_object_or_404(Banner, pk=banner_id)
    banner.click(request, place_slug)

    return redirect(banner.url)
