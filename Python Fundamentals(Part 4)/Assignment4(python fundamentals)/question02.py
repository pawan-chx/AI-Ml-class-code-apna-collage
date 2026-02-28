class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def display_all_reviews(self):
        print(self.reviews)

    def count_reviews(self):
        print(f"Total reviews = {len(self.reviews)}")


book1 = Book("money", "pawan")
print(book1.author)

book1.add_review("kbah dkknadf dvdlfaf")
book1.add_review("kbah dkknadf dvdlfaf auirwke woithwekj gwouthewekkr qtkj4nt")

book1.display_all_reviews()
book1.count_reviews()
