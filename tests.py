import pytest

from main import BooksCollector

@pytest.fixture(autouse=True)
def collector():  # фикстура, которая создаёт объект
    collector = BooksCollector()
    return collector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name',['Я','Гордость и предубеждение и зомби','Гордость и предубеждение и зомби и зомби'])
    def test_add_new_book_add_one_book_valid_number_of_characters(self,collector,name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_set_comedy_to_existing_book(self,collector,genre):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', genre)
        assert collector.books_genre['Гордость и предубеждение и зомби'] == genre

    def test_set_book_genre_set_comedy_to_nonexisting_book(self,collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        assert 'Гордость и предубеждение и зомби' not in collector.books_genre.keys()

    def test_get_book_genre_get_genre_to_existing_book(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Аватар')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        collector.set_book_genre('Аватар', 'Фантастика')
        assert collector.get_book_genre('Аватар') == 'Фантастика'

    def test_get_books_with_specific_genre_get_fantastic_two_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Аватар')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        collector.set_book_genre('Аватар', 'Фантастика')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Аватар','Гарри Поттер']

    def test_get_books_genre_get_empty(self,collector):
        assert collector.books_genre == {}

    def test_get_books_for_children_get_two_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Аватар')
        collector.add_new_book('Астрал')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        collector.set_book_genre('Аватар', 'Фантастика')
        collector.set_book_genre('Астрал', 'Ужасы')
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби', 'Аватар']

    def test_add_book_in_favorites_get_existing_book(self,collector):
        collector.add_new_book('Аватар')
        collector.add_book_in_favorites('Аватар')
        collector.add_book_in_favorites('Аватар')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_existing_book_in_favorites(self,collector):
        collector.add_new_book('Аватар')
        collector.add_book_in_favorites('Аватар')
        collector.delete_book_from_favorites('Аватар')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_get_two_book(self,collector):
        collector.add_new_book('Аватар')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Аватар')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.favorites == ['Аватар', 'Гарри Поттер']

