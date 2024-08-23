from django.core.management.base import BaseCommand
from faker import Faker
from libraryApp.factories import AuthorFactory, BookFactory
from libraryApp.models import Book, Author
import time
import factory


class Command(BaseCommand):
    help = 'populate database with dummy data using django-faker'

    def handle(self, *args, **kwargs):
        faker = Faker()
        start = time.perf_counter()

        authors = Author.objects.all()[:3]
        # authors = AuthorFactory.stub_batch(10)
        for _ in range(1):
            BookFactory.create(author=authors)

        end = time.perf_counter()
        print("total time takes: ", end-start)
        self.stdout.write(self.style.SUCCESS("Successfully populated dummy data in Database"))
