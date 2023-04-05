from datetime import datetime
from collections import Counter


class SimpleReport:

    def __date_validator(productList):
        manufacturing_date = min([
            product["data_de_fabricacao"] for product in productList
        ])

        expiration_date = min([
            product["data_de_validade"] for product in productList
            if product["data_de_validade"] >= datetime.now()
            .strftime('%Y-%m-%d')
        ])

        return [manufacturing_date, expiration_date]

    @staticmethod
    def generate(productList):

        validated_date = SimpleReport.__date_validator(productList)

        company = Counter(
            [product["nome_da_empresa"] for product in productList]
        ).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {validated_date[0]}\n"
            f"Data de validade mais próxima: {validated_date[1]}\n"
            f"Empresa com mais produtos: {company}"
        )
