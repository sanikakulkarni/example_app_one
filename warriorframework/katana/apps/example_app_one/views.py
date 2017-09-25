# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View


class ExampleAppOneView(View):

    def get(self, request):
        return render(request, 'example_app_one/example_app_one.html', {"data": "Example App One"})