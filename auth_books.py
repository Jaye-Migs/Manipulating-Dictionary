author = [
    {'author': 'J.K. Rowling',
     'book': 'Harry Potter and the Sorcerer\'s Stone'
    },
    {'author': 'George Orwell',
     'book': '1984'
    },
    {'author': 'J.R.R. Tolkien',
     'book': 'The Lord of the Rings'
    },
    {'author': 'Harper Lee',
     'book': 'To Kill a Mockingbird'
    },
    {'author': 'F. Scott Fitzgerald',
     'book': 'The Great Gatsby'
    },
    {'author': 'Jane Austen',
     'book': 'Pride and Prejudice'
    },
    {'author': 'Mark Twain',
     'book': 'The Adventures of Huckleberry Finn'
    },
    {'author': 'Herman Melville',
     'book': 'Moby-Dick'
    }
]

print (author)

print ('5th author\'s famous book is: ', author[4]['book'])

author[6]['book'] = 'A Connecticut Yankee in King Arthur\'s Court'
print (author)

author.pop(5)

print ('Last author is: ', author[-1])