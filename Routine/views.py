from django.shortcuts import render , redirect
from .forms import UserForm , RoutineForm , LoginForm
# Create your views here.
from .models import User , Routine

#view for register user 
def register(request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        
        if user.is_valid():

            user.save()
            return redirect('routine:login')
    else:
        user_form = UserForm()
        context = {
            'user_form':user_form
        }
        return render(request,'routine/register.html',context)


#view for login user    
def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'],password=request.POST['password'])
        if user:
            request.session['user_id'] = user[0].id
            return redirect('routine:index')
        else:
            return render(request,'routine/login.html')

    else:
        form = LoginForm()
        context = {
            'form': form
            }
        return render(request,'routine/login.html', context)

#view for addming routine for each user using UserForm
def add_routine(request):
    if request.method == 'POST':
        routine = RoutineForm(request.POST)
        if routine.is_valid():
            routine.save()
        
            return render(request,'routine/index.html')
    else:
        return render(request,'routine/add_routine.html')

#view for deleting routine of user by id
def delete_routine(request,id):
    
    Routine.objects.filter(id=id).delete()
    return redirect('routine:index')
    

#index view for user to see oewn routines through session 
def index(request):
    if(request.session.get('user_id')):
        if request.method == 'POST':
            routine = RoutineForm(request.POST)
            if routine.is_valid():
                routine.save()
                context = {
                    'message': "Routine added"
                }
                return redirect('routine:index')

        routines = Routine.objects.filter(user = request.session['user_id']).order_by('time')
        user = User.objects.get(id=request.session['user_id'])
        form = RoutineForm()	
        context = {

                    'routines':routines,
                    'form' : form,
                    'user': user,
                }
        
        return render(request,'routine/index.html',context)
    else:
        return redirect('routine:login')


#logout function delete session user_id
def logout(request):
    request.session.flush()
    return redirect('routine:login')

