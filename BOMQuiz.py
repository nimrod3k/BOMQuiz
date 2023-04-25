from sws.random_verse import get_random_verse, pretty_print_verse
import ldscriptures as lds

OT = 1
NT = 2
BOM = 3
DAC = 4
POGP = 5

BOM_BOOKS = {
    1:'1 Nephi',
    2:'2 Nephi',
    3:'Jacob',
    4:'Enos',
    5:'Jarom',
    6:'Omni',
    7:'Words of Mormon',
    8:'Mosiah',
    9:'Alma',
    10:'Helaman',
    11:'3 Nephi',
    12:'4 Nephi',
    13:'Mormon',
    14:'Ether',
    15:'Moroni'
    }
BOM_OFFSET = 66
verse = get_random_verse(filter_book=BOM)
print(verse['scripture_text'])
print(BOM_BOOKS)
print('\nGuess the book: ')
book_guess = int(input())
print('\nGuess the chapter: ')
chapter_guess = int(input())
print('\nGuess the verse: ')
verse_guess = int(input())
points = 0
if book_guess == (verse['book_id'] - BOM_OFFSET):
    print(f'{BOM_BOOKS[int(book_guess)]} was correct + 5 points')
    chapter_offset = verse['chapter_number'] - chapter_guess
    points += 5
    if chapter_offset == 0:
        print('Chapter was correct')
    else:
        print(f'You were {abs(chapter_offset)} chapters away!  Guessed: {chapter_guess}   Actual Chapter: {verse["chapter_number"]}')

else:
    print(f'{BOM_BOOKS[book_guess]} was incorrect, it was {verse["book_title"]}')


# scripture = lds.get('2 Nephi 28:30')


