from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    @staticmethod
    def generate(productList):
        companies = [product["nome_da_empresa"] for product in productList]
        quantity_company = Counter(companies).most_common()

        response = (
            f"{SimpleReport.generate(productList)}\n"
            f"Produtos estocados por empresa:\n"
        )

        for company, quantity in quantity_company:
            response += f"- {company}: {quantity}\n"

        return response
