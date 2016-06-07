from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()

router.register(r'user', views.UserViewSet)

urlpatterns = router.urls
