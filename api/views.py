from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions
from .models import Genre, Book, Comment
from .serializers import GenreSerializer, BookSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        janrlar = Genre.objects.all()
        return janrlar

    def get_serializer_class(self):
        return GenreSerializer

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    lookup_url = 'id'

    def get_queryset(self):
        janrlar = Genre.objects.all()
        return janrlar

    def get_serializer_class(self):
        return GenreSerializer

class BookListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        kitoblar = Book.objects.all()
        return kitoblar

    def get_serializer_class(self):
        return BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    lookup_url = 'id'

    def get_queryset(self):
        kitoblar = Book.objects.all()
        return kitoblar

    def get_serializer_class(self):
        return BookSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        kommentlar = Comment.objects.all()
        return kommentlar

    def get_serializer_class(self):
        return CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    lookup_url = 'id'

    def get_queryset(self):
        kommentlar = Comment.objects.all()
        return kommentlar

    def get_serializer_class(self):
        return CommentSerializer
