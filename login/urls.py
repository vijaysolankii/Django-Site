from django.contrib import admin
from django.urls import path

from .views import (
    demologinIndex,
    demoProfileCreate,
    demoProfileList,
    CreateProfileView,
    SearchProfileView
)

urlpatterns = [
    path("", demoProfileList, name="profilelist"),
    path("search/<str:para>/", demoProfileList, name="profilesearch"),
    path("<int:custid>/", demologinIndex, name="profiledetails"),
    path("add/", CreateProfileView.as_view(), name="addpage"),
    path("search/", SearchProfileView.as_view(), name="searchpage"),
]