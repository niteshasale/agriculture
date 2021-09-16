from django.urls import path
from .import views
urlpatterns = [
	path('',views.home,name="home"),
	path('predict',views.predict,name="predict"),
	path('statistics',views.statistics,name="statistics"),
	path('selectlabel',views.selectlabel,name="selectlabel"),
	path('average',views.average,name="average"),
	path('selectaverage',views.selectaverage,name="selectaverage"),
	path('climat',views.climat,name="climat"),
	path('above',views.above,name="above"),
	path('season',views.season,name="season"),
]