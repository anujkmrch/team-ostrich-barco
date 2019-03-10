# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# class Post(models.Model):
# 	title = models.CharField(max_length=100)
# 	created_date = models.DateTimeField(default=timezone.now)

# class Comment(models.Model):
# 	text = models.CharField(max_length=100)
# 	post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Light(models.Model):
	title = models.CharField(max_length=100)
	lightid = models.CharField(max_length=32,unique=True)
	lattitude = models.FloatField(null=False, blank=False)
	longitude = models.FloatField(null=False, blank=False)
	active = models.BooleanField(default=0) #0=Broken, 1= Working
	operating = models.BooleanField(default=1)
	
	def __str__(self):
		return self.title + " - Active: " + ('Yes' if self.active==True else 'No')

class Status(models.Model):
	light = models.ForeignKey(Light,on_delete=models.CASCADE)
	broken = models.BooleanField(default=0)
	sender = models.BooleanField(default=0)
	status = models.CharField(max_length=100) # R = reg, Y = yellow, G = green, C = clock
	recieved_at	 = models.DateTimeField(default=timezone.now)
	mobile = models.CharField(max_length=15,blank=True,  null=True)

	def __str__(self):
		return self.light.title

class Update(models.Model):
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	text = models.CharField(max_length=255, blank=False,null=False)

class Camera(models.Model):
	lattitude = models.FloatField(null=False, blank=False)
	longitude = models.FloatField(null=False, blank=False)
	maintainence = models.BooleanField(default=0)

class Density(models.Model):
	camera = models.ForeignKey(Camera,on_delete=models.CASCADE)
	data = models.CharField(max_length=100)
