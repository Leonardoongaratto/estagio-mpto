import json

from django.http.response import HttpResponse
from django.db import transaction

from .models import State
from .serialization import StateSerializer


def state_list(request):
    query = State.objects.all()
    response = HttpResponse()
    response.status_code = 501


    if query.exists():
        response = HttpResponse(
            content_type ='application/json',
            content=json.dumps([
                StateSerializer.serialize(state) for state in query
            ])
        )
    else:
        response.status_code = 404
    
    return response

def state_creat(request):
    response = None

    try:
        with transaction.atomic():
            data = json.loads(request.body)
            state = StateSerializer.deserialize(data)
            state.save()

            response = HttpResponse(
                content=json.dumps(
                    StateSerializer.serialize(state)
            ),
            status=201
        )
                
    except Exception as e:
        response = HttpResponse(
            content=json.dumps({
                'message': str(e)
            }),
            status=400
        )

    return response


def state_index(request):
    response = None

    if request.method == 'GET':
        response = state_list(request)

    elif request.method == 'POST':
        response = state_creat(request)

    return response
