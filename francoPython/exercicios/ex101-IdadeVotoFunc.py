import datetime


def voto(ano):
    """
    -> Informe se o usuário ja tem direito de voto elitoral.
    :param ano: Ano de nascimento do usuário.
    :return: A mensagem com o informação de voto.
    """
    idade = datetime.datetime.today().year - ano

    if 16 <= idade <= 17 or idade > 65:
        return f'Com {idade} anos: Voto OPCIONAL!'

    if idade < 16:
        return f'Com {idade} anos: Voto NEGADO!'

    if 65 > idade >= 18:
        return f'Com {idade} anos: Voto OBRIGATÓRIO!'


ano = int(input('Digite o seu ano de nascimento: '))
print(voto(ano))