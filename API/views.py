import base64
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from API.models import *
from rest_framework.renderers import JSONRenderer

from API.serializers import StudentSerializer
import numpy as np
import matplotlib.pyplot as plt
# Create your views here.

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk
from io import BytesIO





# Create your views here.
def homepage(request):
    equations = Equation.objects.all()
    context = {'equations': equations}
    return render(request, 'index.html', context)



def fetch_graph(request):
    equation_id = request.GET.get('equation_id')
    equation = Equation.objects.get(id=equation_id)

    x_min = equation.x_min
    x_max = equation.x_max
    x = np.linspace(x_min, x_max, 400)

    def f(x):
        try:
            return eval(equation.expression)
        except Exception as e:
            return None

    y = f(x)

    if y is not None:
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f'f(x) = {equation.expression}', color='blue')
        plt.title('Graph of f(x)')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.legend()

        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)

        image_base64 = base64.b64encode(buffer.read()).decode()

        # Return the graph HTML as JSON response
        graph_html = f'<img src="data:image/png;base64,{image_base64}" alt="Graph">'
        return JsonResponse({'graph_html': graph_html})
    else:
        return JsonResponse({'error': 'Failed to generate graph.'})
     

