from django.urls import path,include
from . import views
app_name="blog"
urlpatterns = [
    path("",views.home,name="all_blogs"),
       path("<int:blog_id>",views.detail, name="detail"),
    path("<int:blog_id>/<int:ha_id>",views.detail),

]