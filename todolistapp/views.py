# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from .serializers import AddTaskSerializer, EditTaskSerializer, TodoSerializer
from .forms import AddtaskForm
from .models import Todo


class IndexView(APIView):
    """
    List all the todolist, and paginate the result.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request):
        todo_lists = Todo.objects.filter(flag=0)
        paginator = Paginator(todo_lists, 5)
        page = request.GET.get("todo_page")

        try:
            todo_lists = paginator.page(page)
        except PageNotAnInteger:
            todo_lists = paginator.page(1)
        except EmptyPage:
            todo_lists = paginator.page(paginator.num_pages)

        finish_lists = Todo.objects.filter(flag=1)
        paginator = Paginator(finish_lists, 5)
        page = request.GET.get("finish_page")   

        try:
            finish_lists = paginator.page(page)
        except PageNotAnInteger:
            finish_lists = paginator.page(1)
        except EmptyPage:
            finish_lists = paginator.page(paginator.num_pages)
        return Response(
            {
                "todo_lists": todo_lists,
                "finish_lists": finish_lists
            }
        )


class SortByPrioView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"
    
    def get(self, request):
        todo_lists = Todo.objects.filter(flag=0).order_by("-priority")
        paginator = Paginator(todo_lists, 5)
        page = request.GET.get("todo_page")

        try:
            todo_lists = paginator.page(page)
        except PageNotAnInteger:
            todo_lists = paginator.page(1)
        except EmptyPage:
            todo_lists = paginator.page(paginator.num_pages)

        finish_lists = Todo.objects.filter(flag=1)
        paginator = Paginator(finish_lists, 5)
        page = request.GET.get("finish_page")   

        try:
            finish_lists = paginator.page(page)
        except PageNotAnInteger:
            finish_lists = paginator.page(1)
        except EmptyPage:
            finish_lists = paginator.page(paginator.num_pages)
        return Response(
            {
                "todo_lists": todo_lists,
                "finish_lists": finish_lists
            }
        )


class SortByExpireView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"
    
    def get(self, request):
        todo_lists = Todo.objects.filter(flag=0).order_by("-expire_time")
        paginator = Paginator(todo_lists, 5)
        page = request.GET.get("todo_page")

        try:
            todo_lists = paginator.page(page)
        except PageNotAnInteger:
            todo_lists = paginator.page(1)
        except EmptyPage:
            todo_lists = paginator.page(paginator.num_pages)

        finish_lists = Todo.objects.filter(flag=1)
        paginator = Paginator(finish_lists, 5)
        page = request.GET.get("finish_page")   

        try:
            finish_lists = paginator.page(page)
        except PageNotAnInteger:
            finish_lists = paginator.page(1)
        except EmptyPage:
            finish_lists = paginator.page(paginator.num_pages)
        return Response(
            {
                "todo_lists": todo_lists,
                "finish_lists": finish_lists
            }
        )


class AddTaskView(APIView):
    """
    Create a new todolist.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "addtask.html"

    def get(self, request):
        serializer = AddTaskSerializer()
	return Response({"serializer": serializer})

    def post(self, request):
        serializer = AddTaskSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            todo_list = Todo(
                todo = data["todo"],
                flag = 0,
                priority = data["priority"]
            )
	    if data["expire_time"]:
                todo_list.expire_time = data["expire_time"]
            todo_list.save()
            return redirect(reverse("index", request=request))
        return Response({"serializer": serializer})


class EditTaskView(APIView):
    """
    Edit the todolist info, change and save the info.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "edittask.html"

    def get(self, request, list_id):
        todo_list = Todo.objects.get(id=list_id)
	serializer = EditTaskSerializer()
	return Response(
            {
                "serializer": serializer,
                "todoinfo": TodoSerializer(todo_list).data
            }
        )

    def post(self, request, list_id):
        todo_list = Todo.objects.get(id=list_id)
        initial_data = {
            "todo": todo_list.todo,
            "priority": todo_list.priority,
            "expire_time": todo_list.expire_time
        }
	serializer = EditTaskSerializer(data=request.data)
	if serializer.is_valid():
            data = serializer.data
            todo_list.todo = data["todo"]
            todo_list.priority = data["priority"]
            todo_list.expire_time = data["expire_time"]
            todo_list.save()
            return redirect(reverse("index", request=request))
        return Response(
            {
                "serializer": serializer,
                "todo_list": TodoSerializer(todo_list).data
            }
        )


def deletetask(request, list_id):
    """
    Delete a target todolist.
    """
    try:
        todo_list = Todo.objects.get(id=list_id)
    except ObjectDoesNotExist:
        return "The todo list is not exists."
    if todo_list:
        todo_list.delete()
        return HttpResponseRedirect(reverse("index"))


def finishtask(request, list_id):
    """
    Put a todolist flag into complete status.
    """
    try:
        todo_list = Todo.objects.get(id=list_id)
    except ObjectDoesNotExist:
        return "The todo list is not exists."
    if todo_list and todo_list.flag == 0:
        todo_list.flag = 1
        todo_list.save()
        return HttpResponseRedirect(reverse("index"))


def backtask(request, list_id):
    """
    Put a todolist flag into undo status.
    """
    try:
        todo_list = Todo.objects.get(id=list_id)
    except ObjectDoesNotExist:
        return "The todo list is not exists."
    if todo_list and todo_list.flag == 1:
        todo_list.flag = 0
        todo_list.save()
        return HttpResponseRedirect(reverse("index"))

