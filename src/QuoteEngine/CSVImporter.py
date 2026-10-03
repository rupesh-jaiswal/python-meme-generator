import csv
from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from model import QuoteModel
class CSVImporter(IngestorInterface):
    allowed_extensions=['csv']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """ parse the csv file and return a list of quotes"""
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest extension of {path}')
        quotes=[]
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                quotes.append(QuoteModel(row['body'], row['author']))
        return quotes
    
