import factory
from .models import Author, Book
from factory import fuzzy

class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    author_name = factory.Faker('name')
    city = factory.Faker('city')

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    book_name = factory.Faker('sentence', nb_words=4)
    launchdate = factory.Faker('date_this_decade')
    
    # Add related authors after book creation
    @factory.post_generation
    def author(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # A list of authors was passed in, use it
            for author in extracted:
                self.author.add(author)
        else:
            # Create 1-3 authors by default
            self.author.add(*AuthorFactory.create_batch(fuzzy.FuzzyInteger(1, 3).fuzz()))
