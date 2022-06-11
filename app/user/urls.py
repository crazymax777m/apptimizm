from django.urls import path

from rental.views import UserView, UserCarsListView, AddCarView, DeleteCarView

# preventing post requests to users list
user_detail = UserView.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)

urlpatterns = [
    # users list url
    path('', UserView.as_view({'get': 'list'})),
    # user detail url
    path('<int:pk>/', user_detail, name='user_detail'),
    # all user's cars url
    path('<int:pk>/cars/', UserCarsListView.as_view(), name='user_cars_list'),
    # add car to user url
    path('<int:pk>/addcar/<int:car_pk>/', AddCarView.as_view()),
    # delete car from user
    path('<int:pk>/deletecar/<int:car_pk>/', DeleteCarView.as_view()),
]
