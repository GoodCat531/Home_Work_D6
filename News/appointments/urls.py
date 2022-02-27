from django.urls import path

from .views import AppointmentView, AppointView

urlpatterns = [

    path('', AppointmentView.as_view(), name='make_appointment'),
    path('appoint/', AppointView.as_view(), name='test'),

]
