from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.views import serve

urlpatterns = [
    path('', views.loogin, name='loogin'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('club/<int:pk>/delete/', views.delete_club, name='delete_club'),
    path('search/', views.search, name= 'search'),
    path('leadshome/', views.leadshome, name='leadshome'),
    path('usershome/', views.usershome, name= 'usershome'),
    path('home/', views.home, name='home'),
    path('club-info/<str:pk>', views.clubinfo, name='club-info'),
    path('createpost/', views.createpost, name='createpost'),
    path('upcomingevent/', views.create_upcoming_event, name='upcomingevent'),
    path('registers/', views.create_register, name='registers'),
    path('addclubleadss/', views.create_addclubleads, name='addclubleads'),
    path('addclub/', views.addclub, name='addclub'),
    path('clubs/', views.ClubListView.as_view(), name='club_list'),
    path('addclubleads_detail/', views.addclubleads_detail.as_view(), name='addclubleads_detail'),
    path('addregister/', views.addregister.as_view(), name='addregister'),
    path('club_detail/', views.club_detail.as_view(), name='club_detail'),
    path('event_detail', views.event_detail.as_view(), name='event_detail'),
    path('club/<int:pk>/update/', views.update_club, name='update_club'),
    path('static/<path:path>/', serve, {'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)