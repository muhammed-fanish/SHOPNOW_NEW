from django.views.static import serve
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include, re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('ckeditor/', include('ckeditor.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    re_path(r'^', include(('web.urls', 'web'), namespace="web")),

    re_path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path('static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_FILE_ROOT}),
    re_path('static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
