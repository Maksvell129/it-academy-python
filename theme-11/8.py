from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write(self):
        pass


class TxtWriter(Writer):
    def write(self):
        print("Записать в тектовый файл")


class CsvWriter(Writer):
    def write(self):
        print("Записать в csv файл")


class ExcelWriter(Writer):
    def write(self):
        print("Записать в Excel файл")



class Reader(ABC):
    @abstractmethod
    def read(self):
        pass


class TxtReader(Reader):
    def read(self):
        pass


class CsvReader(Reader):
    def read(self):
        pass


class ExcelReader(Reader):
    def read(self):
        pass


class PdfReader(Reader):
    def read(self):
        pass
