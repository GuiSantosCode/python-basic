'''
PADRÃO ANSI:
    escape sequence

\033[0;33;44m
    entre [ e m
    0 = style
    33 = text
    44 = back

exemplo: print('\033[1;31;43mOlá, Mundo!')
style padrao, text vermelho, e back amarelo.

7 = style
    inverte as cores do text e back

BIBLIOTECA RICH:
depois de instalar, digite:
    from rich import print
    print('[red] olá mundo [/red]')

    onde:
        [red]...[/red]: modo de delimitação semelhante ao sistema HTML
'''