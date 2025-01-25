from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/work-orders/', include('tickets.urls')),  # API routes
]

# Serve generated work order HTML files
if settings.DEBUG:
    urlpatterns += static('/generated_work_orders/', document_root=settings.BASE_DIR / 'generated_work_orders')
