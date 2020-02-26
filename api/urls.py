from django.urls import path

from api.views import PageList, PageDetail

urlpatterns = [
    path('pages/', PageList.as_view(), name='pages_list'),
    path('pages/<int:pk>', PageDetail.as_view(), name='pages_detail')
]