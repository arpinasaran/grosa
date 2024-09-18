from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductEntryForm
from main.models import ProductEntry

def show_main(request):
    product_entries = ProductEntry.objects.all()

    context = {
        'title' : 'GROSA',
        'name' : 'Arvin Wijayanto',
        'npm' : '2306259780',
        'class' : 'PBP D',
        'product_entries' : product_entries,
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
