from django.contrib import admin
from django.urls import path, include
import funccrud.urls
import funccrud.views
# import classcrud.urls
# import classcrud.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', funccrud.views.welcome, name="welcome"),
    path('funccrud/', include(funccrud.urls)),
    path('signup/', funccrud.views.signup, name='signup'),
    path('login/', funccrud.views.login, name='login'),
    path('logout/', funccrud.views.logout, name='logout'),
    # path('classcrud/', include(classcrud.urls)),
]
