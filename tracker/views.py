import json

from django.http.response import HttpResponse, HttpResponseNotAllowed
from tracker.models import PackageContainer
from helpers import restfy
from django.http.response import HttpResponse
from .serializers import LogTraceSerializer, StateSerializer, CitySerializer, NaturalPersonSerializer, LegalPersonSerializer, PersonSerializer, PackageContainerSerializer


(
    package_container_index,
    package_container_by_id
) = restfy.make_rest(PackageContainerSerializer)
person_index, person_by_id = restfy.make_rest(
    PersonSerializer,
    allow_create=False,
    allow_update=False,
    allow_delete=False
)
legal_person_index, legal_person_by_id = restfy.make_rest(LegalPersonSerializer)
natural_person_index, natural_person_by_id = restfy.make_rest(NaturalPersonSerializer)
state_index, state_by_id = restfy.make_rest(StateSerializer)
city_index, city_by_id = restfy.make_rest(CitySerializer)



def package_container_log_register(request, unique_identify):
    status = 501
    content = None


    try:
        payload = json.loads(request.body)
        package = PackageContainer.objects.get(unique_identify=unique_identify)
        log_trace = LogTraceSerializer.decode(payload)
        package.logs.add(log_trace, bulk=False)

        status = 201
        content = json.dumps({
            'package': PackageContainerSerializer.encode(package),
            'log_trace': LogTraceSerializer.encode(log_trace)
        })
        
    except PackageContainer.DoesNotExist:
        status = 404 
        content = json.dumps({
            "message": "Pacote não encontrado"
        })
    except Exception as e:
        status = 404
        content = json.dumps({
            "message": str(e)
        })


    return HttpResponse(
        status=status,
        content=content,
        content_type='application/json'
    )



def package_container_log_list(request, unique_identify):
    return HttpResponse(status=501)



def package_container_log_trace(request, unique_identify):
    if request.method == 'GET':
        return package_container_log_list(request, unique_identify)
    elif request.method == 'POST':
        return package_container_log_register(request, unique_identify)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
    
