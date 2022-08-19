from django.db import IntegrityError
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from cafes.models import Cafe, CafeComplexity
from cafes.serializers import CafeSerializer, CafeDetailSerializer, CafeComplexitySerializer
from core import exceptions


class CafeViewSet(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            raise exceptions.AlreadyExistInstance

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CafeDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True)
    def flag(self, request, *args, **kwargs):
        obj = self.get_object()
        flags = obj.flags.filter(user=request.user)

        if flags:
            flags.delete()
            return Response({"detail": "삭제"})
        else:
            flags.create(user=request.user, cafe=obj)
            return Response({"detail": "생성"})

    @action(detail=True)
    def like(self, request, *args, **kwargs):
        obj = self.get_object()
        likes = obj.likes.filter(user=request.user)

        if likes:
            likes.delete()
            return Response({"detail": "삭제"})
        else:
            likes.create(user=request.user, cafe=obj)
            return Response({"detail": "생성"})


class CafeComplexityViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    queryset = CafeComplexity.objects.all()
    serializer_class = CafeComplexitySerializer
