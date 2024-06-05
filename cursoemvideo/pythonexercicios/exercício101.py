####### este programa verifica se o voto é obrigatório, opcional ou negado
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade >= 18 and idade < 65:
        print(f'Você tem {idade} anos e seu voto é OBRIGATÓRIO.')
    if idade >= 16 and idade <= 17 or idade > 65:
        print(f'Você tem {idade} anos e seu voto é FACULTATIVO.')
    if idade < 16:
        print(f'Você tem {idade} anos e NÃO PODE VOTAR.')


votar = int(input('Qual o seu ano de nascimento? '))
print('-='*15)
voto(votar)
