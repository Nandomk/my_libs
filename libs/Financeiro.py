def calcular_valor_futuro(principal, taxa_juros, periodos):
    """
    Calcula o valor futuro usando juros compostos.

    :param principal: Valor inicial investido
    :param taxa_juros: Taxa de juros (em decimal, por exemplo, 0.05 para 5%)
    :param periodos: Número de períodos (anos, meses, etc.)
    :return: Valor futuro após aplicar os juros compostos
    """
    valor_futuro = principal * (1 + taxa_juros) ** periodos
    return valor_futuro



def calcular_valor_presente(valor_futuro, taxa_juros, periodos):
    """
    Calcula o valor presente usando juros compostos.

    :param valor_futuro: Valor futuro desejado
    :param taxa_juros: Taxa de juros (em decimal, por exemplo, 0.05 para 5%)
    :param periodos: Número de períodos (anos, meses, etc.)
    :return: Valor presente necessário para atingir o valor futuro
    """
    valor_presente = valor_futuro / (1 + taxa_juros) ** periodos
    return valor_presente

