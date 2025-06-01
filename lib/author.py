# lib/author.py
class Author:
    all = []  # Class variable to hold all authors
    def __init__(self, name):
        self.name = name
        self._articles = []
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after instantiation")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        from article import Article
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({magazine.category for magazine in self.magazines()})