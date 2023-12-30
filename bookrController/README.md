pip install pipenv
pipenv install

depend: 
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py runserver

/admin login >> name: uruguaj >> password: heslo

- `/api/books/`: List and create books.
- `/api/books/<book_id>/`: Retrieve, update, or delete a specific book.



