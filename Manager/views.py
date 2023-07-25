from django.shortcuts import render, redirect
from .forms import ManagerForm
from .models import Manager

# Add Blog

def create_member(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('search/')
            except:
                pass
    else:
        form = ManagerForm()
    return render(request, 'create.html', {'form':form})

# retrieve blog

def retrieve_member(request):
    members = Manager.objects.all()
    return render(request,'search.html',{'members':members} )

# Update Blog

def update_member(request,pk):
    members = Manager.objects.get(id=pk)
    form = ManagerForm(instance=members)

    if request.method == 'POST':
        form = ManagerForm(request.POST, instance=members)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'blogs': members,
        'form': form,
    }
    return render(request,'update.html',context)

# Delete Blog

def delete_member(request, pk):
    blogs = Manager.objects.get(id=pk)

    if request.method == 'POST':
        blogs.delete()
        return redirect('/search')

    context = {
        'blogs': blogs,
    }
    return render(request, 'remove.html', context)
