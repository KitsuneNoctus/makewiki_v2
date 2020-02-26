# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# from wiki.models import Page
# from api.serializers import PageSerializer

# class PageList(APIView):
#     def get(self, request):
#         pages = Page.objects.all()[:20]
#         data = PageSerializer(pages, many=True).data
#         return Response(data)

# class PageDetail(APIView):
#     def get(self, request, pk):
#         page = get_object_or_404(Page, pk=pk)
#         data = PageSerializer([age]).data
#         return Response(data)

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from wiki.models import Page
from api.serializers import PageSerializer


class PageList(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetail(RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer