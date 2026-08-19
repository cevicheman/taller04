# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Simulación de base de datos local en memoria
data_list = []

#Cada actividad deberá almacenar, como mínimo, un título, una descripción, un responsable y la fecha de creación. 
# Añadiendo algunos datos de ejemplo para probar el GET
data_list.append({
    "titulo": "Actividad 1",
    "descripcion": "Descripción de la actividad 1",
    "responsable": "Responsable 1",
    "fecha_creacion": "2026-01-01"
})
data_list.append({
    "titulo": "Actividad 2",
    "descripcion": "Descripción de la actividad 2",
    "responsable": "Responsable 2",
    "fecha_creacion": "2026-01-01"
})
data_list.append({
    "titulo": "Actividad 3",
    "descripcion": "Descripción de la actividad 3",
    "responsable": "Responsable 3",
    "fecha_creacion": "2026-01-01"
})

class DemoRestApi(APIView):
    name = "Demo REST API"

    def get(self, request):
        return Response(data_list, status=status.HTTP_200_OK)


    def post(self, request):
      data = request.data

      # Validación mínima
      if 'titulo' not in data or 'responsable' not in data:
         return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

      data_list.append(data)

      return Response({'message': 'Dato guardado exitosamente.', 'data': data}, status=status.HTTP_201_CREATED)
