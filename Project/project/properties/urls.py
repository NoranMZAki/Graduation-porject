from django.urls import path


from .import views
urlpatterns = [
    path('details/<int:pk>', views.HouseDetails.as_view()),
    path('houses/', views.HouseView.as_view()),
    path('details/', views.Details.as_view(), name='details'),
    path('filter/', views.Filter.as_view(), name='filter'),
    path('filter2/', views.Filter2.as_view(), name='filter2'),
    path('filter3/', views.Filter3.as_view(), name='filter3'),
    path('sell/', views.Sell12.as_view(), name='sell'),
    # path('sell3/', views.Sell3.as_view(), name='sell3'),
    path('sell4/', views.Sell4.as_view(), name='sell4'),
    path('thankyou/', views.ThankYou.as_view(), name='thankyou'),
    path('result/', views.Prediction, name='Prediction'),
    path('index/', views.Result.as_view(), name='index'),
    path('allhouses/', views.PropView, name='allhouses'),
    path('<int:id>/', views.detail_view, name='detail'),
    path('sell3/', views.sell3, name='sell3'),
    # path('success', views.success, name='success'),

]
