from django.shortcuts import render,redirect
from .models import Drive
from .forms import DriveForm
# Create your views here.
def drives(request):
    alldrives = Drive.objects.all()
    return render(request, 'all-drives.html', {'alldrives': alldrives})
    
def drive(request, pk):
    drive = Drive.objects.get(drive_id=pk)
    return render(request, 'single-drive.html', {'drive': drive})    



def createDrive(request):
    if request.method == 'POST':
        form = DriveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all-drives')  # Redirect to a success page or any other URL
    else:
        form = DriveForm()
    return render(request, 'create_drive.html', {'form': form})

# views.py
from django.shortcuts import render, redirect, get_object_or_404


def updateDrive(request, pk):
    drive = get_object_or_404(Drive, drive_id=pk)
    form = DriveForm(instance=drive)
    if request.method == 'POST':
        form = DriveForm(request.POST, request.FILES, instance=drive)
        if form.is_valid():
            form.save()
            return redirect('all-drives')  # Redirect to any appropriate URL
    context = {'form': form}
    return render(request, 'create_drive.html', context)

def delete_drive(request, pk):
    drive = get_object_or_404(Drive, drive_id=pk)
    if request.method == 'POST':
        drive.delete()
        return redirect('all-drives')  # Redirect to any appropriate URL
    return render(request, 'delete_drive.html', {'drive': drive})