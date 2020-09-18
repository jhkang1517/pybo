# ---------------------------------------- [edit] ---------------------------------------- #
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    ...


def detail(request, question_id):
    ...
# ---------------------------------------------------------------------------------------- #