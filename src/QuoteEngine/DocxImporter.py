from QuoteEngine.IngestorInterface import IngestorInterface
import docx
from typing import List
from model import QuoteModel
class DocxImporter(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """parse the docx file and return a list of quotes"""
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest extension of {path}')
        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                [body, author] = para.text.split('-')
                quotes.append(QuoteModel(body.strip(), author.strip()))
        return quotes