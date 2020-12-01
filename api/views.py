from django.http import JsonResponse
from rest_framework.decorators import api_view
from scripts.count_class import count_class
from scripts.count_comment import count_comment
from scripts.count_file_and_folder import count_file_and_folder
from scripts.count_library import count_library
from scripts.count_line_of_code import count_line_of_code
from scripts.count_method import count_method
from scripts.count_testing import count_testing


@api_view(["GET"])
def counter_class(request, author, repository):
    counter = count_class(author + '/' + repository)
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_comment(request, author, repository):
    counter = count_comment(author + '/' + repository)
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_file_and_folder(request, author, repository):
    counter = count_file_and_folder(author + '/' + repository)
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_library(request, author, repository):
    counter = count_library(author + '/' + repository)
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_line_of_code(request, author, repository):
    counter = count_line_of_code(author + '/' + repository)
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_method(request, author, repository):
    counter = count_method(author + '/' + repository)
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_testing(request, author, repository):
    counter = count_testing(author + '/' + repository)
    return JsonResponse(counter, safe=False)
