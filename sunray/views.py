from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Project, LargeProject
from django.shortcuts import render
from .models import Project, LargeProject
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def edit_large_project(request, pk):
    large_project = get_object_or_404(LargeProject, pk=pk)
    
    if request.method == 'POST':
        # Handle form submission to edit LargeProject instance
        # Example:
        large_project.title = request.POST['title']
        large_project.kw=request.POST['kw']
        large_project.place= request.POST['place']  # optional field
        large_project.technology= request.POST['technology']
        large_project.saves = request.POST['saves']
        large_project.trees=request.POST['trees']
        large_project.tons=request.POST['tons']
        if 'image' in request.FILES:
            large_project.image = request.FILES['image']
        
        # Update other fields as needed
        large_project.save()
        return redirect('dashboard')  # Redirect to dashboard after edit
    
    return render(request, 'edit_large_project.html', {'large_project': large_project})

@login_required
def delete_large_project(request, pk):
    large_project = get_object_or_404(LargeProject, pk=pk)
    # Implement delete logic
    large_project.delete()
    return redirect('dashboard')  # Redirect to dashboard after delete


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        project.title = request.POST['title']
        project.description = request.POST['description']
        project.project_details = request.POST.get('project_details', '')
        
        if 'image' in request.FILES:
            project.image = request.FILES['image']
        
        project.save()
        return redirect('dashboard')
    
    return render(request, 'edit.html', {'project': project})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    # Implement delete logic here
    project.delete()
    return redirect('dashboard')

def index(request):
    # Retrieve all large projects
    large_projects = LargeProject.objects.all()
    context = {
        'large_projects': large_projects
    }
    return render(request, 'index.html', context)
def large_project_detail(request, pk):
    large_project = get_object_or_404(LargeProject, pk=pk)
    context = {
        'large_project': large_project
    }
    return render(request, 'large_project.html', context)

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


@login_required
def upload_project(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        project_details = request.POST.get('project_details', '')  # optional field
        image = request.FILES['image']

        # Save the project object to the database
        project = Project(title=title, description=description, project_details=project_details, image=image)
        project.save()

        return redirect('project_list')  # Redirect to project list after successful upload

    return render(request, 'upload_project.html')


@login_required
def upload_large_project(request):
    if request.method == 'POST':
        title = request.POST['title']
        kw=request.POST['kw']
        place= request.POST['place']  
        technology= request.POST['technology']
        saves = request.POST['saves']
        image = request.FILES['image']
        trees=request.POST['trees']
        tons=request.POST['tons']
        # Save the large project object to the database
        large_project = LargeProject(title=title, kw=kw, place=place, technology=technology, image=image,saves=saves,trees=trees,tons=tons)
        large_project.save()

        return redirect('dashboard')  # Redirect to index page after successful upload

    return render(request, 'upload_large_project.html')

@login_required
def dashboard(request):
    projects = Project.objects.all()
    large_projects = LargeProject.objects.all()
    
    context = {
        'projects': projects,
        'large_projects': large_projects
    }
    return render(request, 'dashboard.html', context)
