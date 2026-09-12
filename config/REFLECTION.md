Failure output: 

Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_book_name (catalog.tests.BookModelTest.test_book_name)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\jesus\cidm3312\book-catalog\catalog\tests.py", line 19, in test_book_name
    self.assertContains(response, book_title)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
AssertionError: False is not true : Couldn't find 'The Dog Story' in the following response
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>Book Catalog</title>\n</head>\n<body>\n    <nav>\n        <ul>\n            <li><a href="/">Book List</a></li>\n            <li><a href="/publishers/">Publishers</a></li>\n            <li><a href="/reviews/">Reviews</a></li>\n        </ul>\n    </nav>\n    <hr>\n    \n\n<h1>Books</h1>\n<ul>\n    \n</ul>\n\n\n</body>\n</html>'

----------------------------------------------------------------------
Ran 1 test in 0.038s

FAILED (failures=1)
Destroying test database for alias 'default'...

Current Output Now: 

Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.055s

OK
Destroying test database for alias 'default'...

The failure output informed me that the line test_book_name failed and was unable to find my book titled “The Dog Story”.

Question 1. 

The model that has a foreign key that I chose is the Book class. As mentioned in the instructions, we were told that "A publisher publishes many books. Each book belongs to one publisher". This lets us know that the publisher will have the primiary key as it is indenpendt from books, but books are dependent on if the publisher actually publishes them. I arranged books to have the foreign key to reflect that it is dependent on publisher. If we reverse this, publishers would become dependent on books, which isn't logically right since publishers publish the books. This would also make it to where a publisher record can only be tied to one book, which would conflict data if a publisher has published multiple books.

Question 2. The field I chose was a models.DateField() to show the date when a book was published. I chose this type over the other fields as I foudn it fitting to show that books are truly dependet on a publisher, showing that once a publisher publishes the book, there is an associated date with it. I also chose it since it stores a number data rather than string text. If stored as a CharField, I would lose the data validation of how the date is formated. DateFiled enforces a specfic date format that doesn't allow any type of string value. Using CharField would allow for any type of text, even if it wasn't an actual date.
