from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('thrall.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('bag/', include('bag.urls')),
    path('blog/', include('blog.urls')),
    path('products/', include('products.url'))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)