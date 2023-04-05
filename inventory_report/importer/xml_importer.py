from inventory_report.importer.importer import Importer
import xmltodict
import os


class XmlImporter(Importer):

    def file_extension(path):
        extension = os.path.splitext(path)
        if extension[1] == ".xml":
            return True

    def import_data(path):
        if XmlImporter.file_extension(path):
            with open(path, encoding="utf-8") as file:
                return xmltodict.parse(file.read())["dataset"]["record"]

        raise ValueError("Arquivo inválido")
