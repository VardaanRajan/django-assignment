from django.shortcuts import render, get_object_or_404, redirect
from .models import ChaiVarity  # Import your model
from .forms import ChaiForm    # Import your form

def all_chai(request):
    # Get all chai objects
    chais = ChaiVarity.objects.all()
    
    # Handle form submission
    if request.method == 'POST':
        form = ChaiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_chai')
    else:
        form = ChaiForm()
    
    context = {
        'chais': chais,
        'form': form,
    }
    return render(request, 'chai/all_chai.html', context)

def chai_detail(request, id):
    # Get single chai object or 404 if not found
    chai = get_object_or_404(ChaiVarity, id=id)
    context = {
        'chai': chai
    }
    return render(request, 'chai/chai_detail.html', context)