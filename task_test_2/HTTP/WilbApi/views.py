from rest_framework import generics

from .tasks import get_article, get_file
from .serializers import *
from .services import *
import base64


class ProductArticleView(generics.ListCreateAPIView):
    queryset = ProductArticle.objects.all()
    serializer_class = ProductArticleSerializer

    def post(self, request, *args, **kwargs):
        article = request.data.get('article')
        get_article.s(artic=article).apply_async(countdown=3)
        return self.create(request,)


class ExcelFileView(generics.ListCreateAPIView):
    queryset = ExcelArticle.objects.all()
    serializer_class = ProductExcelSerializer

    def post(self, request, *args, **kwargs):
        excel64 = request.data.get('excel_base64')
        get_file.s(excel_base64=excel64).apply_async(countdown=2)
        return self.create(request, *args, **kwargs)


with open("WilbApi/articles.xlsx", 'rb') as file:
    excel_raw_bytes = file.read()
    excel_base64 = base64.b64encode(excel_raw_bytes).decode('utf-8')
    asyncio.get_event_loop().run_until_complete(art_excel(excel_base64))
