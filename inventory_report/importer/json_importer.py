from inventory_report.importer.importer import Importer
import json
import os


class JsonImporter(Importer):

    def file_extension(path):
        extension = os.path.splitext(path)
        if extension[1] == ".json":
            return True

    def import_data(path):
        if JsonImporter.file_extension(path):
            with open(path, encoding="utf-8") as file:
                return json.load(file)

        raise ValueError("Arquivo inválido")
