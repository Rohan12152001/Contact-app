from django.urls import path,URLPattern
from . import views
from django.conf import settings
from django.conf.urls.static import static 
# from .views import *

app_name='contactapp'


urlpatterns=[
    path('',views.homepage,name='homepage'),
    # path('contact_list',views.contact_list,name='contact_list'),
    path('contact_list/<int:pk>/',views.contact_detail.as_view(),name='contact_detail'),
    path('contact_list/',views.contact_list,name='contact_list'),
    path('update/<int:pk>/',views.contact_edit,name='update'), ### Doubt ##
    path('delete/<int:pk>/',views.contact_delete,name='delete'),
    #path('<pk>/',views.contact_detail.as_view(),name='contact_detail'),
    path('create/',views.contact_new,name='create'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 



