from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    

    context ={'projects': projects}
    return render(request, 'project.html',  context)



def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    reviews = projectobj.review_set.all()
    context = {'project': projectobj, 'tags':tags, 'reviews': reviews }
    return render(request, 'second-project.html', context) 


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'project-form.html',  context)



def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')




    context={'form':form}
    return render(request, 'project-form.html',  context)



def deleteProject(request, pk):
     project = Project.objects.get(id=pk)

     if request.method == 'POST':
         project.delete()
         return redirect('projects')
 
     return render(request, 'delete.html',  {'object':project}  )