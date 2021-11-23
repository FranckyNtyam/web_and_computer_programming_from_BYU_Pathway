with open("books.txt") as book_of_mormon:
    for chapter in book_of_mormon:
        chapter = chapter.strip()
        print(chapter)