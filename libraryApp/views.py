from django.shortcuts import render

from rest_framework import generics
from . import models
from libraryApp import serializers
from rest_framework.response import Response
import datetime
import time
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.conf import  settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
a = cache.keys('*')
print(a)
class BooksList(generics.ListCreateAPIView):
    # queryset = models.Book.objects.all().prefetch_related('author')[:10000]
    
    queryset = cache.get("all_books")
    t = cache.ttl("all_books")
    # cache.delete("all_books")
    print("time-", t)
    if queryset:
        t1 = cache.ttl("all_books") 
        print("all-book from cache : ", t1, queryset, )
    else:
        queryset = models.Book.objects.all()
        print("hit database - ", queryset)
        cache.set("all_books", queryset, timeout=20)
    print("queryset - t", queryset)
    serializer_class = serializers.BookSerializer


class AutherList(generics.ListCreateAPIView):
    # throttle_classes = [UserRateThrottle]
    queryset = models.Author.objects.all()[:1000]
    serializer_class = serializers.AutherSerializer

    def list(self, request):
        # print(request.user)
        queryset = self.get_queryset()
        serializer = serializers.AutherSerializer(queryset, many=True)
        response_body = {
            'data': serializer.data,
            'totalResult': queryset.count(),
            'service': 'ABC',
            'timestamp': datetime.datetime.now().isoformat(),
        }
        return Response(response_body)
