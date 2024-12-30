from abc import ABC, abstractmethod

class DocumentProcessor(ABC):
    def process(self, file_path):
        self.read_document(file_path)
        self.process_document()
        self.save_document()

    @abstractmethod
    def read_document(self, file_path):
        pass

    @abstractmethod
    def process_document(self):
        pass

    @abstractmethod
    def save_document(self):
        pass

class WordProcessor(DocumentProcessor):
    def __init__(self):
        self.content = ""
        self.metadata = {}

    def read_document(self, file_path):
        print(f"Reading Word document from {file_path}")
        self.content = "Sample content from the Word document."
        self.metadata = {"title": "Sample Word", "author": "Author Name"}

    def process_document(self):
        print("Processing Word document")
        print(f"Content: {self.content}")
        print(f"Metadata: {self.metadata}")

    def save_document(self):
        print("Saving Word document")
        print(f"Document saved with title: {self.metadata['title']}")
        print(f"Final Content: {self.content}")

class PDFProcessor(DocumentProcessor):
    def __init__(self):
        self.content = ""
        self.metadata = {}

    def read_document(self, file_path):
        print(f"Reading PDF document from {file_path}")
        self.content = "Sample content from the PDF document."
        self.metadata = {"title": "Sample PDF", "author": "Author Name"}

    def process_document(self):
        print("Processing PDF document")
        print(f"Content: {self.content}")
        print(f"Metadata: {self.metadata}")

    def save_document(self):
        print("Saving PDF document")
        print(f"Document saved with title: {self.metadata['title']}")
        print(f"Final Content: {self.content}")

class ExcelProcessor(DocumentProcessor):
    def __init__(self):
        self.content = ""
        self.metadata = {}

    def read_document(self, file_path):
        print(f"Reading Excel document from {file_path}")
        self.content = "Sample content from the Excel document."
        self.metadata = {"title": "Sample Excel", "author": "Author Name"}

    def process_document(self):
        print("Processing Excel document")
        print(f"Content: {self.content}")
        print(f"Metadata: {self.metadata}")

    def save_document(self):
        print("Saving Excel document")
        print(f"Document saved with title: {self.metadata['title']}")
        print(f"Final Content: {self.content}")
def main():
    processors = [
        WordProcessor(),
        PDFProcessor(),
        ExcelProcessor()
    ]
    file_paths = ["word_document.docx", "pdf_document.pdf", "excel_document.xlsx"]
    
    for i, processor in enumerate(processors):
        print(f"\nProcessing {file_paths[i]}:")
        processor.process(file_paths[i])

if __name__ == "__main__":
    main()