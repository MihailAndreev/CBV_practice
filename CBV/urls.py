from django.urls import path

from CBV_practice.CBV.views import MyView, MyTemplateView, MyDetailsView, MyListView, MyCreateView, MyUpdateView, \
    MyDeleteView

urlpatterns = (
    path('', MyView.as_view(), name='MyView'),
    path('template_view/', MyTemplateView.as_view(), name='My template view'),
    path('details_view/<int:pk>/', MyDetailsView.as_view(), name='My details view'),
    path('list_view/', MyListView.as_view(), name='My list view'),
    path('create_car/', MyCreateView.as_view(), name='My create view'),
    path('update_car/<int:pk>/', MyUpdateView.as_view(), name='My update view'),
    path('delete_car/<int:pk>/', MyDeleteView.as_view(), name='My delete view'),
)
