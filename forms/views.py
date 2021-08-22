from django.db.models import Q, F, Subquery, OuterRef
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import CategorySerializer, FormFieldSerializer, FormSerializer
from .models import Category, Form, FormField


class TestView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        data = {
            'abcd': 'test'
        }
        return Response(data, status=status.HTTP_200_OK)


class CreateCategoryApiView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        form_id = request.data.get('form_id', None)
        form = None
        if form_id:
            form = get_object_or_404(Form, pk=form_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(form=form)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListCategoriesApiView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()


class UpdateCategoryApiView(generics.UpdateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class DeleteCategoryApiView(generics.DestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()

    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SearchCategoryApiView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        search_term = self.request.query_params.get('search_term')
        return Category.objects.filter(Q(name__icontains=search_term))


class CategoryDetailApiView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()


class CreateFormApiView(generics.CreateAPIView):
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic() 
    # ensures that if fields in a form are in the same position 
    # to not create the form in the first place and return an
    # error message
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UpdateFormApiView(generics.UpdateAPIView):
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Form.objects.all()

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class DeleteFormApiView(generics.DestroyAPIView):
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Form.objects.all()

    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CreateFormFieldApiView(generics.CreateAPIView):
    serializer_class = FormFieldSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        form_id = request.data.get('form_id')
        form = get_object_or_404(Form, pk=form_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(form=form)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateFormFieldApiView(generics.UpdateAPIView):
    serializer_class = FormFieldSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = FormField.objects.all()

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class SearchFormApiView(generics.ListAPIView):
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        search_term = self.request.query_params.get('search_term')
        return Form.objects.filter(Q(name__icontains=search_term))


class ListFormApiView(generics.ListAPIView):
    serializer_class = FormSerializer
    queryset = Form.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ListFieldsByFormApiView(generics.ListAPIView):
    serializer_class = FormFieldSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        form_id = self.kwargs.get('pk', None)
        return FormField.objects.filter(form=form_id)


class ListFormFieldByCategoryApiView(generics.ListAPIView):
    serializer_class = FormFieldSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        category_id = self.kwargs.get('pk', None)
        category = get_object_or_404(Category, pk=category_id)
        # get all the forms attached to this category and it's list of ancestors field
        forms = category.get_ancestors(include_self=True).values('form')

        fields = FormField.objects\
                        .filter(form__in=forms)\
                        .annotate(
                            level=Subquery(Category.objects.filter(id=OuterRef('form')).values('level')))\
                        .order_by('label', '-level')\
                        .distinct('label')

        return FormField.objects.filter(id__in=fields).order_by('position')