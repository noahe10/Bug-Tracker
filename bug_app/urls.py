from django.urls import path
from .views import appList, appDetail, appCreate, appUpdate, appDelete, login

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('list/', appList.as_view(), name='appList'),
    path('detail/<int:pk>', appDetail.as_view(), name='appDetail'),
    path('create/', appCreate.as_view(), name='appCreate'),
    path('update/<int:pk>/', appUpdate.as_view(), name='appUpdate'),
    path('delete/<int:pk>/', appDelete.as_view(), name='appDelete'),
]