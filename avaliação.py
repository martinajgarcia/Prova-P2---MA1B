#ex1
def verificar_ano(data):
    string = data.split(' ')
    print (string[2])

#ex2
séries_nota10 = []
episódios_nota10 = []
for i in range (0, 10):
    série = str(input('série:'))
    episódio = str(input('episódio:'))
    nota_imdb = float(input('nota IMDB:'))
    nota_netflix = float(input('nota netflix:'))
    if nota_imdb == 10.0 and nota_netflix == 10.0:
        séries_nota10.append(série)
        episódios_nota10.append(episódio)
for k in range (0, len(séries_nota10)):
    print(séries_nota10[k], '-', episódios_nota10[k])


#ex3



#ex4
nota_ep = 0
for m in range (0, 4):
    seriado = str(input('seriado:'))
    n_ep = int(input('número de episódios:')
               for n in range (0, n_ep)
                   nota_ep = float(input('nota do episódio:'))
                   nota_ep =+ nota_ep
                   nota_média = (nota_ep/n_ep)
    print(seriado, ':', nota_media)
