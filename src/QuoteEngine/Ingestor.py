

from QuoteEngine.CSVImporter import CSVImporter
from QuoteEngine.DocxImporter import DocxImporter
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.PDFImporter import PDFImporter
from QuoteEngine.TextImporter import TextImporter


class Ingestor(IngestorInterface):
    """ a simple Ingestor class to parse different file types and extract quotes"""
    allowed_extensions = ['txt', 'docx', 'csv', 'pdf']
    ingestors = [TextImporter, DocxImporter, CSVImporter, PDFImporter]
    @classmethod
    def parse(cls, path:str):
        """parse the file and return a list of quotes"""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f'Cannot ingest extension of {path}')