import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def read(path):
        with open(path, encoding="utf-8") as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(file_reader)

    def import_data(path, type):
        if type == 'simples':
            return SimpleReport.generate(Inventory.read(path))
        elif type == 'completo':
            return CompleteReport.generate(Inventory.read(path))
