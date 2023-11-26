# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 14:41:03 2023

@author: wwolf
"""

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.index, name='hello_world'),
]