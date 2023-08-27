
class Ac01Exercicios:
    """ Exercícios da AC01

    Exercícios no intuito de utilizar o framework pytest, com as funções e o conjunto de testes de unidade.

    """

    def calcular_salario_liquido(valor_hora_aula: float, 
                                 numero_aulas: int, 
                                 percentual_inss: float):
        """ Calcular Salario Liquido

        Note:
            Faça uma função que efetua o cálculo do salário líquido de um professor. Os dados fornecidos serão:
            valor hora aula, número de aulas dadas e o percentual de desconto do INSS.

        Args:
            valor_hora_aula: o valor hora aula .
            numero_aulas: numero de aulas.
            percentual_inss: percentual INSS

        Returns:
            salário líquido

        """       
        salario_bruto = valor_hora_aula * numero_aulas
        desconto_inss = (percentual_inss / 100) * salario_bruto
        salario_liquido = salario_bruto - desconto_inss
        return round(salario_liquido,2)

    def calcular_valor_com_desconto(valor_produto: float):
        """ Calcular valor com desconto

        Note:
           Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto aos
            clientes. Faça uma função que receba um valor de um produto e devolva um novo valor tendo em vista que o 
            desconto foi de 9%.
        Args:
            valor_produto: o valor do produto.

        Returns:
            valor do produto com desconto
        """  
        desconto = valor_produto * 0.09
        novo_valor = valor_produto - desconto
        return novo_valor
 
    def calcular_valor_promocao(valor_original: float, 
                                desconto: float):
        """ Calcular valor da promocao

        Note:
            Faça uma função que leia dois números reais, um será o valor de um produto e o outro o valor do desconto que
            esse produto está recebendo. Devolva quantos reais o produto custa na promoção.
        Args:
            valor_original: o valor original do produto.
            desconto: valor do desconto.

        Returns:
             Devolva quantos reais o produto custa na promoção
        """  
        valor_promocao = valor_original - desconto
        return valor_promocao




    def calcular_conta_e_gorjeta(valor_despesa):
        """ Calcular conta e gorjeta

        Note:
            Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% de comissão para o garçom. Faça
            uma função que receba o valor gasto com despesas realizadas em um restaurante e devolva o valor total da conta e o valor da gorjeta.

        Args:
            valor_original: o valor original do produto.
            desconto: valor do desconto.

        Returns:
             devolva o valor total da conta e o valor da gorjeta
        """  
        gorjeta = valor_despesa * 0.10
        valor_total = valor_despesa + gorjeta
        return round(valor_total, 2), round(gorjeta, 2)
