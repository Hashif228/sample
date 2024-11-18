from django.contrib import admin
from django.urls import path
from .import views
from .views import Cre,Det,Del

urlpatterns = [
    
    path('index/',views.index,name='index'),
    path('course/',views.course,name='course'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('knowus/',views.knowus,name='know'),
    path('hea/',views.hea,name='hea'),
    path('placement/',views.placement,name='placement'),
    path('login/',views.login,name='login'),
    path('courses/',views.courses,name='courses'),
    path('python/',views.python,name='python'),
    path('java/',views.java,name='java'),
    path('flutter/',views.flutter,name='flutter'),
    path('php/',views.php,name='php'),
    path('rhcsa/',views.rhcsa,name='rhcsa'),
    path('rhce/',views.rhce,name='rhce'),
    path('networking/',views.networking,name='networking'),
    path('microsoftbi/',views.microsoftbi,name='microsoftbi'),
    path('mern/',views.mern,name='mern'),
    path('mean/',views.mean,name='mean'),
    path('ionic/',views.ionic,name='ionic'),
    path('digitalmarketing/',views.digitalmarketing,name='digitalmarketing'),
    path('devops/',views.devops,name='devops'),
    path('datascience/',views.datascience,name='datascience'),
    path('dataanalytics/',views.dataanalytics,name='dataanalytics'),
    path('ccna/',views.ccna,name='ccna'),
    path('azure/',views.azure,name='azure'),
    path('aws/',views.aws,name='aws'),
    path('asp/',views.asp,name='asp'),
    path('softwaretesting/',views.softwaretesting,name='softwaretesting'),
    path('uiux/',views.uiux,name='uiux'),
    path('webdesign/',views.webdesign,name='webdesign'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('password/',views.password,name='password'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('dashboard/course',views.dashboardcourse,name='dashboardcourse'),
    path('logout',views.logout,name='logout'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('det/<int:pk>/',Det.as_view(),name='det'),
    path('cre/',Cre.as_view(),name='cre'),
    path('del/<int:pk>',Del.as_view(),name='Del'),













]
