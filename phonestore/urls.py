from django.urls import path

from phonestore import views
from phonestore.views import AdDetailedView

urlpatterns = [
    path('ad/<int:pk>', AdDetailedView.as_view(), name='ad-view'),
]
