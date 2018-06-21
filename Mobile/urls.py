from django.conf.urls import url
from . import views

app_name = 'Mobile'

urlpatterns = [
    # home
    url(r'^home/$', views.homepage, name='homepage'),
    url(r'homepage/$', views.mobilehomepage, name='mobilehomepage'),
    url(r'^signup/$',views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^bills/$', views.bills_view, name="bills"),
    url(r'^bill_generate', views.bill_generate_view , name= 'bill_generate'),
    url(r'^additem/$', views.additem_view, name="additem"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name="activate"),
    url(r'^generatepdf/$', views.generatepdf_View, name = 'generatepdf'),

]
