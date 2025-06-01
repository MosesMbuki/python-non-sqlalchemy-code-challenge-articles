from author import Author
from magazine import Magazine

class Article:
    all = [] 
    
    def __init__(self, author, magazine, title):        
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable")
        
    @property
    def author(self):
        return self._author
        
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author")
        self._author = author
        
    @property
    def magazine(self):
        return self._magazine
        
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = magazine