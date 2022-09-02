# stocks-api

### installation
1.1 run: `cp .env.template .env.dev` \
1.2. Fill .env.dev with configs \
2. run: `docker-compose build` \
3. run: `docker-compose up -d` \
4. run: `docker-compose exec stocks_api python manage.py migrate`

### API endpoints

BASE_URL: http://0.0.0.0:8000

- `/news/stock/{stock}` \
description: to retrieve company news by ticket. Example: "/news/stock/TSLA" \
query_parameters:
  - date_from [optional]: filter news by date. Format: "%Y-%m-%d". example: "2022-09-01".
  - date_to [optional]: filter news by date. Format: "%Y-%m-%d". example: "2022-09-01".
  - page_size [optional]: to paginate response. Format: int. example: 5.
  - page [optional]: to choose page number from paginated response. !!! has no effect if no page_size !!!.
