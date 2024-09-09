from django.shortcuts import render

def show_main(request):
    context = {
        'title' : 'GROSA',
        'nama' : 'Arvin Wijayanto',
        'kelas' : 'PBP D',
    }

    return render(request, "main.html", context)
