from django.shortcuts import render,redirect
from django.db.models import ProtectedError
from .forms import EmployeeForm,PositionForm
from .models import Employee,Position
# Create your views here.
def employee_list(request,flag=0):
    if flag > 0:
        mes = True
    else:
        mes = False
    print("=========================--------------",request)
    context = {'employee_list':Employee.objects.all().order_by('id'),'position_list':Position.objects.all(),'message':mes}
    return render(request,"employee_register/employee_list.html",context)

def employee_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"employee_register/register_form.html",{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')


def position_form(request,id=0):
    print("=========================================================================",id)
    if request.method == "GET":
        if id==0:
            form = PositionForm()
        else:
            position = Position.objects.get(pk=id)
            form = PositionForm(instance=position)
        return render(request,"employee_register/position_form.html",{'form':form})
    else:
        print("=============================================================else")
        if id==0:
            form = PositionForm(request.POST)
        else:
            position = Position.objects.get(pk=id)
            form = PositionForm(request.POST,instance=position)
        print("==============================",form)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def position_delete(request,id):
    position = Position.objects.get(pk=id)
    try:
        position.delete()
    except ProtectedError:
        print(ProtectedError)
        print("========================================================Cannot delete")
    return redirect('/employee/list')
