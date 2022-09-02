import datetime
from http.client import HTTPException

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .constants import ErrorMessage
from .serializers import CompanyNewsSerializer
from .models import CompanyNews
from .utils import paginate


@api_view(['GET'])
def get_company_news(request, stock) -> Response:
    get_params = request.query_params

    company_news = CompanyNews.objects.filter(stock=stock)
    if 'date_from' in get_params:
        date_from = datetime.datetime.strptime(get_params['date_from'], "%Y-%m-%d")
        company_news = company_news.filter(published_at__gte=date_from)
    if 'date_to' in get_params:
        date_to = datetime.datetime.strptime(get_params['date_to'], "%Y-%m-%d")
        date_to = date_to + datetime.timedelta(hours=24)
        company_news = company_news.filter(published_at__lt=date_to)

    news_data = CompanyNewsSerializer(company_news, many=True).data
    if 'page_size' in get_params:
        try:
            news_data = paginate(news_data, get_params)
        except:
            raise HTTPException(ErrorMessage.INVALID_PAGINATION)

    return Response(news_data)
