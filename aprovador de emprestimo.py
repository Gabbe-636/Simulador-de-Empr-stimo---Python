casa = float(input('Qual o valor do imóvel?'))
sal = float(input('Qual o teu salário?'))
anos = int(input('Em quantos anos deseja pagar?'))
presta = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}'.format(casa, anos, presta))
min = sal * 30 / 100

if presta <= min: #NESSE CASO, O VALOR DO EMPRÉSTIMO NÃO COMPROMETE 30% DA RENDA DO INTERESSADO, CONCEDENDO A APROVAÇÃO.
    print('EMPRESTIMO APROVADO!')
else:
    print('EMPRÉSTIMO NEGADO!')