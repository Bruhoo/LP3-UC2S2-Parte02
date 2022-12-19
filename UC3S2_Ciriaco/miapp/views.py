from django.shortcuts import render, HttpResponse

# Create your views here.

layout="""
    <h1>Lenguaje de Programacion III-S2-EC3</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
    </ul>
    <hr/>
"""
def index(request):
    mensaje="""
        <h3>Ciriaco Esquivel Omar Antonio</h2>
        <h3>Cachay Huertas Jose Fernando</h3>
        <h3>Delgado Tuanama Willy Francis</h3>
    """
    return HttpResponse(layout + mensaje)