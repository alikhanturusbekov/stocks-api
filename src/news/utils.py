from django.core.paginator import Paginator


def paginate(data, get_params) -> dict:
    page = get_params['page'] if 'page' in get_params else 1
    paginator = Paginator(data, get_params['page_size'])

    page = paginator.get_page(page)
    return {
        'page': page.number,
        'page_size': get_params['page_size'],
        'total_pages': paginator.num_pages,
        'data': page.object_list,
    }
