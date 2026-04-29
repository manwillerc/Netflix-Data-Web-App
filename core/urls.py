from django.urls import path
from . import views
from .views import ViewerListView, ViewerDetailView, AccountListView, AccountDetailView, BehaviorDetailView, ViewerAccountDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about'),
    path('analytics/', views.analytics, name="analytics"),
    path('user_list/', views.user_list, name='user_list'),
    path('account_list/', views.account_list, name='account_list'),
    path('behavior_list/', views.behavior_list, name='behavior_list'),
    path('viewers/', ViewerListView.as_view(), name="viewer_list"),
    path('viewer/<int:pk>', ViewerDetailView.as_view(), name="viewer_details"),
    path('accounts/', AccountListView.as_view(), name="account_list"),
    path('account/<int:pk>', AccountDetailView.as_view(), name="account_details"),
    path('behavior/<int:pk>', BehaviorDetailView.as_view(), name = "behavior_details"),
    path('add_account/', views.create_account, name='add_account'),
    path('account/<int:pk>/edit/', views.edit_account, name="edit_account"),
    path('account/<int:pk>/confirm_delete', views.delete_account, name="confirm_delete_account"),
    path('add_viewer/', views.create_viewer, name='add_viewer'),
    path('viewer/<int:pk>/edit/', views.edit_viewer, name="edit_viewer"),
    path('viewer/<int:pk>/confirm_delete', views.delete_viewer, name="confirm_delete_viewer"),
    path('prediction_tool/', views.predict_churn, name="prediction_form"),
    path('viewer/<int:pk>/account/<int:pk2>', ViewerAccountDetailView.as_view(), name="viewer_account_details")
    
]