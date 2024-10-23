from rest_framework import generics
from .models import Filer
from rest_framework.response import Response
from .serializers import FileSerializer

class UploadFile(generics.GenericAPIView):
    serializer_class = FileSerializer
    queryset = Filer.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)