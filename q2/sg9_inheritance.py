class Publication: # Parent Class
    def __init__(self, title, author): # Initiates the attributes
        self.__TITLE, self.__AUTHOR = title, author

    @property # Getter Method
    def title(self):
        return self.__TITLE
        
    @title.setter # Setter Method
    def title(self, title):
        self.__TITLE = title

    @property # Getter Method
    def author(self):   
        return self.__AUTHOR

    @author.setter # Setter Method
    def author(self, author):
        self.__AUTHOR = author

    def display_info(self): # A Display Function
        print(f'Title: {self.__TITLE}\nAuthor: {self.__AUTHOR}')

class Book(Publication): # Child Class
    def __init__(self, number_of_pages, title, author): # Initiates the attributes
        super().__init__(title, author) # Calls the parent class constructor
        self.__PAGE_COUNT = number_of_pages

    @property # Getter Method
    def page_count(self):
        return self.__PAGE_COUNT

    @page_count.setter # Setter Method
    def page_count(self, number_of_pages):
        if number_of_pages < 0: # Constraint
            raise ValueError('The page count must be positive.') # Stops the program 
        self.__PAGE_COUNT = number_of_pages

class Magazine(Publication): # Child Class
    def __init__(self, issue_number, title, author): # Initiates the attributes
        super().__init__(title, author) # Calls the parent class constructor
        self.__ISSUE_NUM = issue_number

    @property # Getter Method
    def issue_number(self):
        return self.__ISSUE_NUM

    @issue_number.setter # Setter Method
    def issue_number(self, issue_number):
        if issue_number < 0: # Constraint
            raise ValueError('The issue number must be positive.') # Stops the program
        self.__ISSUE_NUM = issue_number

# Testing

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book(310, "The Hobbit", "J.R.R. Tolkein")
mag1 = Magazine(202, "National Geographic", "Various Authors")

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
print(book1.page_count)
book1.page_count = 100
book1.display_info()
print(book1.page_count)

print("\nMagazine Information:")
mag1.display_info()
print(mag1.issue_number)