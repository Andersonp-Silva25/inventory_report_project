from inventory_report.inventory.product import Product


def test_cria_produto():
    response = (
        "O produto Spironolactone fabricado em 2021-07-17 por REMEDYREPACK "
        "com validade até 2023-11-18 precisa ser armazenado instrucao 7."
    )

    product = Product(
        7,
        "Spironolactone",
        "REMEDYREPACK",
        "2021-07-17",
        "2023-11-18",
        "SM28 B981 5118 903W JY0C 5KVO 3QD",
        "instrucao 7",
    )

    assert str(product) == response
