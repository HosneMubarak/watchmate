from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('watchlist_app.urls')),
    path('account/', include('user_app.urls')),
    
    #django default basic auth url
    # path('api-auth/', include('rest_framework.urls')),
]
