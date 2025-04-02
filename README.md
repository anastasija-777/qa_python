# qa_python
### Реализованные тесты

### **1. Добавление новых книг:**

* Тест test_add_new_book_add_two_books() проверяет успешное добавление двух книг.
* Тест test_add_new_book_add_one_book_valid_number_of_characters() проверяет успешное добавление книги с валидным количеством символов в названии (от 1 до 40 символов).

### 2. Установка жанра книги

* Тест test_set_book_genre_set_comedy_to_existing_book() проверяет установку жанра из списка self.genre для существующей книги в словаре self.books_genre.
* Тест test_set_book_genre_set_comedy_to_nonexisting_book() проверяет отсутствие установки жанра для несуществующей книги в словаре self.books_genre.

### 3. Получение жанра книги:

* Тест test_get_book_genre_get_genre_to_existing_book() проверяет получение жанра для существующей книги в словаре self.books_genre.

### 4. Фильтрация книг по жанру:

* Тест test_get_books_with_specific_genre_get_fantastic_two_books() проверяет фильтрацию книг по жанру "Фантастика".

### 5. Книги для детей:

* Тест test_get_books_for_children_get_two_books() проверяет фильтрацию книг, подходящих для детей.

### 6.Избранные книги:

* Тест test_add_book_in_favorites_get_existing_book() проверяет добавление существующей книги в избранное.
* Тест test_delete_book_from_favorites_delete_existing_book_in_favorites() проверяет удаление книги из избранного.
* Тест test_get_list_of_favorites_books_get_two_book() проверяет получение списка избранных книг.
