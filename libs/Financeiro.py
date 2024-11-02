import math


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

def calcular_taxa_juros(valor_presente, valor_futuro, periodos):
        """
        Calcula a taxa de juros compostos.

        :param valor_presente: Valor presente ou inicial
        :param valor_futuro: Valor futuro desejado
        :param periodos: Número de períodos (anos, meses, etc.)
        :return: Taxa de juros (em decimal)
        """
        taxa_juros = (valor_futuro / valor_presente) ** (1 / periodos) - 1
        return taxa_juros


def calcular_periodos(valor_presente, valor_futuro, taxa_juros):
            """
            Calcula o número de períodos necessários para atingir um valor futuro com juros compostos.

            :param valor_presente: Valor presente ou inicial
            :param valor_futuro: Valor futuro desejado
            :param taxa_juros: Taxa de juros (em decimal, por exemplo, 0.05 para 5%)
            :return: Número de períodos necessários
            """
            periodos = math.log(valor_futuro / valor_presente) / math.log(1 + taxa_juros)
            return periodos