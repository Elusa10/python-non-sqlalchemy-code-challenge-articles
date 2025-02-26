class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        magazine.add_article(self) 
        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]
        pass

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))
        pass

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article
        pass

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))

class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  # Calls the setter method
        self.category = category  # Calls the setter method
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and value.strip():
            self._category = value
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        pass

    def add_article(self, article):
        self._articles.append(article)


    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if self.articles:
            return [article.title for article in self._articles] if self._articles else []
            

    def contributing_authors(self):
        author_counts = {}
        
        for article in self.articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        
        return contributing_authors if contributing_authors else None
        