"""MyPortfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from ZiriPortfolio.models import MyPortfolio
from django.conf.urls.static import static
from django.conf import settings

# Serializers define the API representation.
class MyPortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyPortfolio
        fields = ('title', 'description', 'image', 'url', 'date')

# ViewSets define the view behavior.
class MyPortfolioViewSet(viewsets.ModelViewSet):
    queryset = MyPortfolio.objects.all()
    serializer_class = MyPortfolioSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'portfolio', MyPortfolioViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^work/', include('ZiriPortfolio.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)