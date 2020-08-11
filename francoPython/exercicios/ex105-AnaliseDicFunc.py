def notas(* notas, sit=False):

    """
    -> Análise de notas de alunos, retornando um dicionário com o total de notas,
    a maior e a menor, a média e a situação do aluno (opcional).
    :param notas: Notas a serem lidas.
    :param sit: Situação do aluno (opcional).
    :return: O relatório com as informações em um dicionário.
    """

    relatorio = dict()

    relatorio['total'] = len(notas)
    relatorio['maior'] = max(notas)
    relatorio['menor'] = min(notas)
    relatorio['media'] = sum(notas)/len(notas)

    if sit:
        if 0 <= relatorio['media'] <= 5:
            relatorio['situacao'] = 'Ruim'

        if 8 > relatorio['media'] > 5:
            relatorio['situacao'] = 'Razoável'

        if relatorio['media'] >= 8:
            relatorio['situacao'] = 'Boa'

    return relatorio


resp = notas(2, 3, 6, 6, 2, sit=True)
print(resp)

