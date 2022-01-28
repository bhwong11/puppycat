from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Vacation, Activities
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import VacationSerializer, ActivitiesSerializer


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


@api_view(['GET'])
def getVacations(request):
    vacations = Vacation.objects.all()
    serializer = VacationSerializer(vacations, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def vacationsDetail(request, pk):
    vacation = Vacation.objects.get(vacation_id=pk)
    serializer = VacationSerializer(vacation, many=False)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def createVacations(request):
    print('REQUEST DATA', request.data)
    serializer = VacationSerializer(data=request.data)
    if serializer.is_valid():
        print('CREATE!!!')
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateVacations(request, pk):
    vacation = Vacation.objects.get(vacation_id=pk)
    serializer = VacationSerializer(instance=vacation, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print('Not Valid')
    for key, value in serializer.data.items():
        setattr(vacation, key, value)
        vacation.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteVacations(request, pk):
    vacation = Vacation.objects.get(vacation_id=pk)
    vacation.delete()
    return Response('item successfully deleeted')


@api_view(['GET'])
def getActivities(request):
    activities = Activities.objects.all()
    serializer = ActivitiesSerializer(activities, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def activitiesDetail(request, pk):
    activity = Activities.objects.get(id=pk)
    serializer = ActivitiesSerializer(activity, many=False)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def createActivities(request):
    activity = Activities.objects.create(
        name=request.data["name"], description=request.data["description"], vacation=Vacation.objects.get(vacation_id=request.data["vacation"]))
    serializer = ActivitiesSerializer(
        instance=activity, data={**request.data, "vacation": activity.vacation})
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateActivities(request, pk):
    activity = Activities.objects.get(id=pk)
    activity.vacation = Vacation.objects.get(
        vacation_id=request.data["vacation"])
    serializer = ActivitiesSerializer(
        instance=activity, data={**request.data, "vacation": activity.vacation})
    if serializer.is_valid():
        serializer.save()
    else:
        print('Not Valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteActivities(request, pk):
    vacation = Vacation.objects.get(vacation_id=pk)
    vacation.delete()
    return Response('item successfully deleeted')
