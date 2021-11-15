from django.shortcuts import render
from django.views.generic import ListView


class SnackListView(ListView):
    template_name = "snack_list.html"
