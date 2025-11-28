from django.shortcuts import render

def inicio(request):
    # Asegúrate de que el nombre de la plantilla sea exacto
    return render(request, 'mi_app/index.html')