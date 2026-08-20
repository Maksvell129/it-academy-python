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

