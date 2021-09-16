from django.shortcuts import render
import joblib
# Create your views here.
import pandas as pd
data = pd.read_csv('agriculture.csv')
model = joblib.load('agricultural production optimization engine.pkl')
def home(request):
	return render(request,'predict/home.html',{'name':'shubhangi'})


def predict(request):
	value = {}
	if request.method == "POST":
		nitrogen = request.POST.get('nitrogen')
		phosphorus = request.POST.get('phosphorus')
		potassium = request.POST.get('potassium')
		temperature = request.POST.get('temperature')
		humidity = request.POST.get('humidity')
		ph = request.POST.get('ph')
		rainfall = request.POST.get('rainfall')
		output = model.predict([[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]])[0]
		value['output']=output
	return render(request,'predict/predict.html',value)

def statistics(request):
	
	df = data['label'].value_counts().index
	
	return render(request,'predict/statistics.html',{'df':df})

def selectlabel(request):
	value = {}
	if request.method == "POST":
		label = request.POST.get('label')
		x = data[data['label']==label]
		n_min = x['N'].min()
		p_min = x['P'].min()
		k_min = x['K'].min()
		t_min = x['temperature'].min()
		h_min = x['humidity'].min()
		ph_min = x['ph'].min()
		rain_min = x['rainfall'].min()

		minimum = [n_min,p_min,k_min,t_min,h_min,ph_min,rain_min]

		n_mean = x['N'].mean()
		p_mean = x['P'].mean()
		k_mean = x['K'].mean()
		t_mean = x['temperature'].mean()
		h_mean = x['humidity'].mean()
		ph_mean = x['ph'].mean()
		rain_mean = x['rainfall'].mean()

		average = [n_mean,p_mean,k_mean,t_mean,h_mean,ph_mean,rain_mean]

		n_max = x['N'].max()
		p_max = x['P'].max()
		k_max = x['K'].max()
		t_max = x['temperature'].max()
		h_max = x['humidity'].max()
		ph_max = x['ph'].max()
		rain_max = x['rainfall'].max()

		maximum = [n_max,p_max,k_max,t_max,h_max,ph_max,rain_max]
		value['minimum']=minimum
		value['average']=average
		value['maximum']=maximum
		
	return render(request,'predict/statistics_show.html',value)

def average(request):
	
	df = data.iloc[0:1,:-1]
	label = data['label'].value_counts().index
	return render(request,'predict/average.html',{'df':df,'label':label})

def selectaverage(request):
	result = []
	if request.method == "POST":
		avg = request.POST.get('avg')
		labels = data['label'].value_counts().index
		for label in labels:
			result.append(data[data['label']==label][avg].mean())
	return render(request,'predict/average_show.html',{'result':result})


def climat(request):
	df = data.iloc[0:1,:-1]
	label = data['label'].value_counts().index
	return render(request,'predict/climat.html',{'df':df,'label':label})

def above(request):
	if request.method == "POST":
		condition = request.POST.get('condition')
		above = [data[data[condition]>data[condition].mean()]['label'].unique()]
		below = [data[data[condition]<data[condition].mean()]['label'].unique()]

	return render(request,'predict/above.html',{'above':above,'below':below})	

def season(request):
	summer = data[(data['temperature']>30) & (data['humidity']>50)]['label'].unique()
	winter = data[(data['temperature']<29) & (data['humidity']>30)]['label'].unique()
	rainy = data[(data['rainfall']>200) & (data['humidity']>30)]['label'].unique()
	return render(request,'predict/season.html',{'summer':summer,'winter':winter,'rainy':rainy})