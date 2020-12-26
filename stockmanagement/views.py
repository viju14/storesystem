from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockCreateForm,StockSearchForm,StockUpdateForm,IssueForm,ReceiveForm,ReorderLevelForm
import csv
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def homeview(request):
    data='hi welcome to home page'
    title = 'HOME'
    context = {"title": title, "data": data}
    return render(request,'home.html',context)

# @login_required
def list_item(request):
    form=StockSearchForm(request.POST or None)
    header = 'list of item'
    queryset = Stock.objects.all()
    context = {"header": header,
               "queryset": queryset,
               "form": form, }
    if request.method=='POST':
        queryset= Stock.objects.filter(#category__icontains=form['category'].value(),
                                       item_name__icontains=form['item_name'].value())
        if form['export_to_CSV'].value()==True:
            responce=HttpResponse(content_type='text/csv')
            responce['Content-Disposition'] = 'attachment;filename="list of stock.csv"'
            writer =csv.writer(responce)
            writer.writerow(['CATEGORY','ITEM_NAME','Quantity'])
            instance=queryset
            for i in instance:
                writer.writerow([i.category,i.item_name,i.quantity])
            return responce

        context={"header":header,
                 "queryset":queryset,
                 "form":form,}
    return render(request,"list_item.html",context)

# @login_required
def add_item(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully added')
        return redirect('/list')
    context={
        "form":form,
        "title":"add Item"

    }
    return render(request,'add_item.html',context)



def update_item(request,pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)

    if request.method=='POST':
        form = StockUpdateForm(request.POST or None,instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('/list')
    context={
        'form':form,
        'title':'update item'
        }


    return render(request,'add_item.html',context)


def delete_item(request,pk):
    queryset=Stock.objects.get(id=pk)
    if request.method=='POST':
        queryset.delete()
        messages.success(request,'Successfully deleted')
        return redirect('/list')
    return render(request,'delete_item.html')


def details_view(request,pk):
    queryset=Stock.objects.get(id=pk)

    context = {
        'queryset': queryset,
    }
    return render(request,'stock_details.html',context=context)

def issue_item(request,pk):
    queryset = Stock.objects.get(id=pk)
    form = IssueForm(request.POST or None,instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.quantity -= queryset.issue_quantity
        messages.success(request,'ISSUE SCUCCESSFULLY'+ str(instance.quantity)+' '+str(instance.item_name)+"s now left in Store")
        instance.save()
        return redirect('/detail/'+str(instance.id))
    context ={
        'queryset': queryset,
        'form':form,
        'title':'Issue '+str(queryset.item_name)
          }
    return render(request,'add_item.html',context=context)

def receive_item(request,pk):
    queryset = Stock.objects.get(id=pk)
    form = IssueForm(request.POST or None,instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.quantity += queryset.issue_quantity
        messages.success(request,'ISSUE SCUCCESSFULLY,  '+ str(instance.quantity)+' '+ str(instance.item_name)+"s now left in Store")
        instance.save()
        return redirect('/detail/'+str(instance.id))
    context ={
        'queryset': queryset,
        'form':form,
        'title':'Issue'+str(queryset.item_name)
          }
    return render(request,'add_item.html',context=context)



def reorder_level(request,pk):
    queryset = Stock.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, 'Reorder level for '+str(instance.item_name)+' is updated to '+str(instance.reorder_level))
        return redirect('/list')
    context = {
        'instance':queryset,
        'form':form,
        }


    return render(request,'add_item.html',context)
