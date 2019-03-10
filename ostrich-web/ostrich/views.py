# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse, HttpResponse

from .models import Light, Status, Camera, Density

def getLightStatus(request,qrcode):
	light = Light.objects.get(lightid=qrcode)
	if not light:
		return JsonResponse({'error':"Sorry not found"})

	return JsonResponse({'foo':light.title})

def getCameraDensity(request	):
	return JsonResponse({'foo':'bar'})