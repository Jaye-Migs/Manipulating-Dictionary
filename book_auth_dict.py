books = [
    {'book': 'To Kill a Mockingbird',
     'author': 'Harper Lee'},
    {'book': '1984',
     'author': 'George Orwell'},
    {'book': 'The Great Gatsby',
     'author': 'F. Scott Fitzgerald'},
    {'book': 'Moby Dick',
     'author': 'Herman Melville'},
    {'book': 'Pride and Prejudice',
     'author': 'Austen'},
    {'book': 'The Catcher in the Rye',
     'author': 'J.D. Salinger'},
    {'book': 'Brave New World',
     'author': 'Aldous Huxley'},
    {'book': 'The Grapes of Wrath',
     'author': 'John Steinbeck'},
    {'book': 'The Hobbit',
     'author': 'J.R.R. Tolkien'},
    {'book': 'Fahrenheit 451',
     'author': 'Ray Bradbury'},
    {'book': 'War and Peace',
     'author': 'Leo Tolstoy'},
    {'book': 'The Alchemist',
     'author': 'Paulo Coelho'}
]

print (books)

print (books[8])

books[4]['author'] = 'Jane Austen'
print (books)

books.pop(2)

print (books[-1])