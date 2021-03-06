from Config.models import Config
from News.models import Keyword
from base.decorator import require_login, require_post, require_json, require_params, Error, error_response
from base.response import response


@require_post
@require_json
@require_params(['kw', 'count', 'web_count'])
@require_login
def add_keyword(request):
    """
    添加关键字
    """
    kw = request.POST['kw']
    count = request.POST['count']
    web_count = request.POST['web_count']
    Keyword.create(kw, count, web_count)
    return response()


@require_post
@require_json
@require_params(['kw', 'count', 'web_count', 'id'])
@require_login
def update_keyword(request):
    """
    更新关键字
    """
    k_id = request.POST['id']
    kw = request.POST['kw']
    count = request.POST['count']
    web_count = request.POST['web_count']
    try:
        o = Keyword.objects.get(pk=k_id)
    except:
        return error_response(Error.NOT_FOUND_KEYWORD)
    o.kw = kw
    o.count = count
    o.web_count = web_count
    o.save()
    return response()


@require_post
@require_json
@require_params(['id'])
@require_login
def delete_keyword(request):
    """
    删除关键字
    """
    k_id = request.POST['id']
    try:
        o = Keyword.objects.get(pk=k_id)
    except:
        return error_response(Error.NOT_FOUND_KEYWORD)
    o.delete()
    return response()


@require_post
@require_json
@require_params(['lasting'])
@require_login
def update_lasting(request):
    """
    更新持续时长
    """
    lasting = request.POST['lasting']
    o = Config.objects.get(key='lasting')
    o.value = lasting
    o.save()
    return response()


@require_post
@require_json
@require_params(['interval'])
@require_login
def update_interval(request):
    """
    更新分析间隔
    """
    interval = request.POST['interval']
    o = Config.objects.get(key='interval')
    o.value = interval
    o.save()
    return response()
