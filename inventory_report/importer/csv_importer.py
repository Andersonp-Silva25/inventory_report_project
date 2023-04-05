from inventory_report.importer.importer import Importer
import csv
import os


class CsvImporter(Importer):

    def file_extension(path):
        extension = os.path.splitext(path)
        if extension[1] == ".csv":
            return True

    def import_data(path):
        if CsvImporter.file_extension(path):
            with open(path, encoding="utf-8") as file:
                return list(
                    csv.DictReader(file, delimiter=",", quotechar='"')
                )

        raise ValueError("Arquivo inválido")
