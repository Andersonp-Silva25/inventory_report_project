import os
import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __file_extension(path):
        extension = os.path.splitext(path)
        return extension[1]

    def __csv_file_reader(path):
        with open(path, encoding="utf-8") as file:
            return list(
                csv.DictReader(file, delimiter=",", quotechar='"')
            )

    def __json_file_reader(path):
        with open(path, encoding="utf-8") as file:
            return json.load(file)

    def __file_reader(path):
        extension = Inventory.__file_extension(path)
        if extension == '.csv':
            return Inventory.__csv_file_reader(path)
        elif extension == '.json':
            return Inventory.__json_file_reader(path)

    def import_data(path, type):
        if type == 'simples':
            return SimpleReport.generate(Inventory.__file_reader(path))
        elif type == 'completo':
            return CompleteReport.generate(Inventory.__file_reader(path))
