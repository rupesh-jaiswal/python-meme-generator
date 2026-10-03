from typing import List
import subprocess
from QuoteEngine.IngestorInterface import IngestorInterface
from model import QuoteModel
class PDFImporter(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """ parse the pdf file and return a list of quotes"""
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest extension of {path}')

        subprocess.call(['pdftotext', '-layout', path, 'output.txt'])
        with open('output.txt', 'r') as f:
            quotes = [line.strip().split(' - ') for line in f if line.strip()]
            f.close()
        # @TODO Implement the parse method to extract quotes from a PDF file
        # You can use libraries like PyPDF2 or pdfminer.six to read PDF files
        # For now, we'll return an empty list as a placeholder
        print(f"Extracted quotes from PDF: {quotes}")
        return [QuoteModel(body.strip(), author.strip()) for body, author in quotes if body and author]
    