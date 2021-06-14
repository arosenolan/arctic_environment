"""tools_for_curiousity_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('t4c/', include('t4c.urls')),
    path('admin/', admin.site.urls),
]

### # This is for later ...  BT
#### Use static() to add url mapping to serve static files during development (only)
###from django.conf import settings
###from django.conf.urls.static import static
###
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
