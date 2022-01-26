from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Vacation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import VacationSerializer


# Create your views here.
class Home(View):
    def get(self, request):
        return JsonResponse({'foo': 'bar'})


class About(View):
    def get(self, request):
        return JsonResponse(['foo', 'bar', 'another one'], safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class Vacactions(View):
    def get(self, request):
        all_vactions = list(Vacation.objects.values())
        return JsonResponse(all_vactions, safe=False)

    def post(self, request, **kwargs):
        new_vacation = request.POST.get('hello')
        print(new_vacation)
        return JsonResponse(['something'], safe=False)


class VacationViewSet(viewsets.ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
