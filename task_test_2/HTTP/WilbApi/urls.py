from django.urls import path

from .views import *

urlpatterns = [
    path('article/', ProductArticleView.as_view()),
    path('loading/excel/', ExcelFileView.as_view()),
]
