nome = input('Digite o nome do aluno: ')
media = float(input("Digite a media do aluno: "))
aprovado = False

if media >= 50:
    aprovado = True
    estado = 'APV'

else:
    aprovado = False
    estado = 'RPV'


dadosAluno1 = {
    'nome' : nome,
    'media' : media,
    'situacao' : estado
}

print(dadosAluno1)