import sys
import os 

sys.path.append(os.path.abspath('..'))
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

from libs.Financeiro import calcular_valor_futuro, calcular_valor_presente, calcular_taxa_juros, calcular_periodos

# Exemplo de uso
principal = 1000  # Valor inicial
taxa_juros = 0.05  # 5% de juros
periodos = 10  # 10 anos

valor_futuro = calcular_valor_futuro(principal, taxa_juros, periodos)
print(f"O valor futuro após {periodos} períodos é de R${valor_futuro:.2f}")

# Exemplo de uso
valor_futuro_desejado = 2000  # Valor futuro desejado
valor_presente = calcular_valor_presente(valor_futuro_desejado, taxa_juros, periodos)
print(f"O valor presente necessário para atingir R${valor_futuro_desejado:.2f} após {periodos} períodos é de R${valor_presente:.2f}")


 # Exemplo de chamada do método calcular_taxa_juros
valor_presente = 1000  # Valor inicial investido
valor_futuro = 2000    # Valor futuro desejado
periodos = 5           # Número de períodos (anos, meses, etc.)

taxa_juros = calcular_taxa_juros(valor_presente, valor_futuro, periodos)
print(f"A taxa de juros necessária é: {taxa_juros:.2%}")

# Exemplo de chamada do método calcular_periodos
valor_presente = 1000  # Valor inicial investido
valor_futuro = 2000    # Valor futuro desejado
taxa_juros = 0.05      # 5% de juros
periodo = calcular_periodos(valor_presente, valor_futuro, taxa_juros)
print(f"O número de períodos necessários é: {periodo:.2f}")

