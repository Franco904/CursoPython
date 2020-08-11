import colorize

# Exemplo:

print('\033[7;30mOlá mundo!\033[m')
print('\033[0;31mHello!\033[m')
print('\033[4;32mThanks!\033[m')
print('\033[1;36mYou are welcome!\033[m')

# Sintaxe: \033['style', 'text', 'background'm


# estilos:

# 0 -- sem formatacao
# 1 -- negrito
# 4 -- sublinhado
# 7 -- alterar cor do fundo com cor do texto

# cores do texto:
#
# 30 -- branco
# 31 -- vermelho
# 32 -- verde
# 33 -- amarelo
# 34 -- azul
# 35 -- roxo
# 36 -- ciano
# 37 -- cinza
#
# cores de fundo:
#
# 40 -- branco
# 41 -- vermelho
# 42 -- verde
# 43 -- amarelo
# 44 -- azul
# 45 -- roxo
# 46 -- ciano
# 47 -- cinza

#cores sem estilo

# 'vermelho': '\033[31m',
# 'azul': '\033[34m',
# 'amarelo': '\033[33m',
# 'branco': '\033[30m',
# 'roxo': '\033[35m',
# 'verde': '\033[32m',
# 'ciano': '\033[36m',
# 'limpa': '\033[m',
# 'preto e branco': '\033[7;30;m',
#
# # cores em negrito:
#
# 'vermelho em negrito': '\033[1;31m',
# 'azul em negrito': '\033[1;34m',
# 'amarelo em negrito': '\033[1;33m',
# 'branco em negrito': '\033[1;30m',
# 'roxo em negrito': '\033[1;35m',
# 'verde em negrito': '\033[1;32m',
# 'ciano em negrito': '\033[1;36m',
#
# # cores sublinhadas
#
# 'vermelho sublinhado': '\033[4;31m',
# 'azul sublinhado': '\033[4;34m',
# 'amarelo sublinhado': '\033[4;33m',
# 'branco sublinhado': '\033[4;30m',
# 'roxo sublinhado': '\033[4;35m',
# 'verde sublinhado': '\033[4;32m',
# 'ciano sublinhado': '\033[4;36m'