from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SupersSerializer
from .models import Supers

@api_view(['GET','Post'])
def supers_list(request):

    if request.method == 'GET':
      supers = Supers.objects.all()
      serializer = SupersSerializer(supers, many=True)
      return Response(serializer.data)


    elif request.method == 'POST':
       serializer = SupersSerializer(data=request.data)
       if serializer.is_valid() == True:
          serializer.save()
          return Response(serializer.data, status=201)
       else:
         return Response(serializer.errors, status =400)
