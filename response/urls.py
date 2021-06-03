from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/threads/<abbrev>', views.ListThread.as_view()),
    path('api/board/', views.ListBoard.as_view()),
    path('api/replies/<id>', views.ListReplies.as_view()),
    path('api/thread/post', views.CreateThreadView.as_view())

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
