class QuoteModel():
    """ A simple QuoteModel to encapsulate a body and an author """
    def __init__(self, body:str, author:str):
        self.body=body
        self.author=author

    def __str__(self):
        return f"{self.body} - {self.author}"
