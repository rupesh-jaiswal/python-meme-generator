from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from model import QuoteModel

class TextImporter(IngestorInterface):
    """A simple TextImporter to parse text files and extract quotes"""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """parse the txt file and return a list of quotes"""
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest extension of {path}')
        quotes = []
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    [body, author] = line.split('-')
                    quotes.append(QuoteModel(body.strip(), author.strip()))
        return quotes
