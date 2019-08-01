class MotorCalculo():
    """
    Classe responsável por expor os métodos de configuração e execução do motor de cálculo.
    """
    def __init__(self):
       pass

    def executar_roteiro(self, roteiro: list):
        """
        Dado um roteiro de cálculo, executa o cálculo passo-a-passo.
        """
        result = {}
        for expr in roteiro:
            expr = expr.strip()
            # expr = self.replace_vars(expr, result)
            pos = expr.find('=')
            if pos == -1:
                continue
            key = expr[:pos].strip()
            value = expr[pos+1:]
            result[key] = eval(value, None, result)
        return result

    # def replace_vars(self, expr: str, values: dict):
    #     """
    #     Substitui uma variável por seu valor
    #     """
    #     for key in values:
    #         expr = expr.replace(key, str(values[key]))
    #     return expr