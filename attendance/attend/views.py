from django.shortcuts import render,redirect
 

from .models import Student
from .forms import YourTaskForm


def your_view(request):

    if request.method == 'POST':
        form = YourTaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            # Automation logic
            if instance.instructor:
                # If instructor column has a value, add "saranya"
                instance.instructor = f"{instance.instructor}, saranya"
            else:
                # If instructor column is empty, set it to "saranya"
                instance.instructor = "saranya"

            # Save the instance
            instance.save()

            return redirect('index.html')  
    else:
        form = YourTaskForm()

    return render(request, 'index.html', {'form': form})




def index(request):

    data = Student.objects.all()
    return render(request, "index.html",{'data':data})


