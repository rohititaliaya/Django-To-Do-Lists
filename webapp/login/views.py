from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.sessions.models import Session
from .forms import*
from .models import*

# Create your views here.
def index(request):
	x = ulogin()
	# del request.session['user']
	most = UserData.objects.all()
	#HOw to get form data
	if request.method == "POST" :
		form = ulogin(request.POST)
		if form.is_valid():
			username = form.cleaned_data['Unm']
			password = form.cleaned_data['pwd']
			bool_unm = UserData.objects.filter(Q(pk=username)).exists() 
			if bool_unm == 1 :
				get_unm = UserData.objects.get(Email=username)
				tpass=get_unm.password
			if bool_unm == 1 and tpass==password :
				 context={'unm':username}
				 request.session['user'] = username 
				 messages.success(request, f"Your Welcome {username}")
				 return redirect('loggedin')
			else:
				 messages.error(request, f"Invelid Username and Password !!!")
				 return redirect('login')
		else:
			messages.error(request, f"Invelid Username and Password !!!")
			return redirect('login')	

	context = {'login':x}
	return render(request,'login.html',context)

def loggedin(request):	
	if request.session.has_key('user'):
		form = TaskForm()
		y=request.session.get('user')
		taskd=	Taskdet.objects.filter(user=y)
		usd=UserData.objects.get(Email=y)
		if request.method=="POST":
			form=TaskForm(request.POST)
			if form.is_valid():
				ins=form.save(commit=False)
				# ins.title=form.cleaned_data['title']
				ins.user=usd
				ins.save()
				messages.error(request, f"Task Added !!")
				return redirect('loggedin')
			else:
				messages.error(request, f"error")
				return redirect('loggedin')
		context={'form':form,'A':taskd}
		return render(request,'loggedin.html',context)
	return redirect('login')

def register(request):
	m = reg()
	form = ulogin()

	if request.method == "POST":
		form = reg(request.POST)
		if form.is_valid():
			form.save()
		return  redirect('/register')
	else:
		HttpResponse("somthing")

	context = {'frm':m,'login':form}
	return render(request,'Register.html',context)

def updateTask(request,pk):
	t = Taskdet.objects.get(id=pk)
	
	form = TaskForm(instance=t)

	if request.method == 'POST' :
		form = TaskForm(request.POST,instance=t)
		if form.is_valid():
			form.save()
			return  redirect('loggedin')
	
	context = {'form':form}
	return render(request,'update_tasks.html',context)

def deleteTask(request,pk):
		item = Taskdet.objects.get(id=pk)

		if request.method == "POST" :
			item.delete()
			return  redirect('loggedin')
				
		context={'item' :item}
		return render(request,'delete.html',context)

def logout(request):
	try:
		del request.session['user']
	except KeyError:
		pass
	return render(request,'login.html')