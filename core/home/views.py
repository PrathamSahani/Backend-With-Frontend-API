import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Log

@csrf_exempt
def log_ingestor(request, log_source):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            log = Log.objects.create(
                level=data.get('level', ''),
                log_string=data.get('log_string', ''),
                timestamp=data.get('timestamp', None),
                source=log_source,
                metadata=data.get('metadata', {})
            )
            return JsonResponse({'message': 'Log created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def log_delete(request, log_id):
    if request.method == 'DELETE':
        try:
            log = Log.objects.get(pk=log_id)
            log.delete()
            return JsonResponse({'message': 'Log deleted successfully'}, status=204)
        except Log.DoesNotExist:
            return JsonResponse({'error': 'Log does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)

def log_search(request):
    level = request.GET.get('level', '')
    log_string = request.GET.get('log_string', '')
    timestamp_start = request.GET.get('timestamp_start', '')
    timestamp_end = request.GET.get('timestamp_end', '')
    source = request.GET.get('source', '')

    logs = Log.objects.all()

    # Filtering logs based on form input
    if level:
        logs = logs.filter(level=level)
    if log_string:
        logs = logs.filter(log_string__icontains=log_string)
    if timestamp_start:
        logs = logs.filter(timestamp__gte=timestamp_start)
    if timestamp_end:
        logs = logs.filter(timestamp__lte=timestamp_end)
    if source:
        logs = logs.filter(source=source)

    return render(request, 'search.html', {'logs': logs})
