from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from book.views import SignUpView, SignInView, UserUpdateView, AddBooksView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-user/', (SignUpView.as_view())),
    path('login/', (SignInView.as_view())),
    path('update-details/', (UserUpdateView.as_view())),
    path('add-books/', (AddBooksView.as_view())),
]
