# coding=utf-8
# interpreter Python 2.7.10

import numpy as np
import matplotlib.pyplot as pp
import pandas as pd

def print_menu():  # função menu
    print ""
    print "1. Insira um ficheiro"
    print "2. Ver as caracteristicas do ficheiro"
    print "3. Escolha e analise as caracteristicas"
    print "4. Criar gráfico"
    print "5. Gravar gráfico"
    print "6. Gravar análise"
    print "7. SAIR\n"

def carac(file): #função que analisa as caracteristicas do ficheiro imprimindo todos os elementos da primeira linha.

    caract = list(file.columns.values)

    print '\n'
    print "---------------------------------"
    print "---------------------------------"
    for elem in caract:
        print caract.index(elem), ':', elem
    print "---------------------------------"
    print "---------------------------------"

    raw_input("Pressione enter para continuar...", )

def analise_carac(file): #função que pede ao utilizador quais as caracteristicas que pretendem analisar e analisa as mesmas para os valores minimos, máximos e médios

    escolha1 = raw_input("Escolha a primeira caracteristica para análise (NOTA: Escolha pelo indice ou nome completo) \n ----> ", )
    escolha2 = raw_input("Escolha a primeira caracteristica para análise (NOTA: Escolha pelo indice ou nome completo) \n ----> ", )

    if escolha1.isdigit() == True:

        num = int(escolha1)
        list_escolha1 = file[file.columns[num]]
        min_escolha1 = list_escolha1[list_escolha1 > 0].min()
        max_escolha1 = list_escolha1.max()
        carac1 = workfile.columns[num]
        carac1_min = workfile.get_value(np.argmin(list_escolha1[list_escolha1 > 0]), workfile.columns[0])
        carac1_max = workfile.get_value(np.argmax(list_escolha1), workfile.columns[0])
        carac1_media = int(np.mean(list_escolha1))

        print "-------------------------------------------------------------------------------------------------"
        print("O artigo com valor minimo de {} da caracteristica {} foi no item {}.\n".format(min_escolha1, carac1,carac1_min))
        print("O artigo com valor maximo de {} da caracteristica {} foi no item {}\n".format(max_escolha1, carac1,carac1_max))
        print("O valor medio da caracteristica {} foi de {}").format(carac1, carac1_media)
        print "-------------------------------------------------------------------------------------------------"
    else:

        list_escolha1 = file[escolha1]
        min_escolha1 = list_escolha1[list_escolha1 > 0].min()
        max_escolha1 = list_escolha1.max()
        carac1_min = workfile.get_value(np.argmin(list_escolha1[list_escolha1 > 0]), workfile.columns[0])
        carac1_max = workfile.get_value(np.argmax(list_escolha1), workfile.columns[0])
        carac1 = escolha1
        carac1_media = int(np.mean(list_escolha1))

        print "-------------------------------------------------------------------------------------------------"
        print("O artigo com valor minimo de {} da caracteristica {} foi no item {} \n".format(min_escolha1, escolha1,carac1_min))
        print("O artigo com valor maximo de {} da caracteristica {} foi no item {}\n".format(max_escolha1, escolha1,carac1_max))
        print("O valor medio da caracteristica {} foi de {}").format(carac1, carac1_media)
        print "-------------------------------------------------------------------------------------------------"

    if escolha2.isdigit() == True:

        num = int(escolha2)
        list_escolha2 = file[file.columns[num]]
        min_escolha2 = list_escolha2[list_escolha2 > 0].min()
        max_escolha2 = list_escolha2.max()
        carac2 = workfile.columns[num]
        carac2_min = workfile.get_value(np.argmin(list_escolha2[list_escolha2 > 0]),workfile.columns[0])
        carac2_max = workfile.get_value(np.argmax(list_escolha2),workfile.columns[0])
        carac2_media = int(np.mean(list_escolha2))

        print "-------------------------------------------------------------------------------------------------"
        print("O artigo com valor minimo de {} da caracteristica {} foi no item {} \n".format(min_escolha2,carac2,carac2_min))
        print("O artigo com valor maximo de {} da caracteristica {} foi no item {}\n".format(max_escolha2, carac2,carac2_max))
        print("O valor medio da caracteristica {} foi de {}").format(carac2, carac2_media)
        print "-------------------------------------------------------------------------------------------------"

    else:

        list_escolha2 = file[escolha2]
        min_escolha2 = list_escolha2[list_escolha2 > 0].min()
        max_escolha2 = list_escolha2.max()
        carac2_min = workfile.get_value(np.argmin(list_escolha1[list_escolha1 > 0]), workfile.columns[0])
        carac2_max = workfile.get_value(np.argmax(list_escolha1), workfile.columns[0])
        carac2 = escolha2
        carac2_media = int(np.mean(list_escolha2))

        print "-------------------------------------------------------------------------------------------------"
        print("O artigo com valor minimo de {} da caracteristica {} foi no item {} \n".format(min_escolha2, escolha2,carac2_min))
        print("O artigo com valor maximo de {} da caracteristica {} foi no item {}\n".format(max_escolha2, escolha2,carac2_max))
        print("O valor medio da caracteristica {} foi de {}").format(carac2, carac2_media)
        print "-------------------------------------------------------------------------------------------------\n"

    raw_input("Pressione enter para continuar...", )

    return (list_escolha1,list_escolha2, min_escolha1,min_escolha2,max_escolha1,max_escolha2,carac1,carac1_min,carac1_max,carac2,carac2_min,carac2_max,carac1_media,carac2_media)

def criar_graf(analise): #criação de um grafico baseado nas caracteristicas analisadas


    pp.xlim(0, len(analise[0]))

    if analise[4] > analise[5]:
        pp.ylim(0, analise[4] * 1.05)
    else:
        pp.ylim(0, analise[5] * 1.05)

    pp.plot(analise[0], "r")
    pp.plot(analise[0][analise[0] == analise[2]].index[0], analise[2], "bo")
    pp.plot(analise[0][analise[0] == analise[4]].index[0], analise[4], "go")
    pp.plot(analise[1], "b")
    pp.plot(analise[1][analise[1] == analise[3]].index[0], analise[3], "y*")
    pp.plot(analise[1][analise[1] == analise[5]].index[0], analise[5], "m*")
    pp.show()

def gravar_graf(analise): #gravação do gráfico em formato de imagem das caracteristicas analisadas

    escolha = raw_input("Qual o nome e a extensão (png/jpg) em que deseja salvar o seu grafico?\n ----> ", )

    pp.xlim(0, len(analise[0]))

    if analise[4] > analise[5]:
        pp.ylim(0, analise[4] * 1.05)
    else:
        pp.ylim(0, analise[5] * 1.05)

    pp.plot(analise[0], "r")
    pp.plot(analise[0][analise[0] == analise[2]].index[0], analise[2], "bo")
    pp.plot(analise[0][analise[0] == analise[4]].index[0], analise[4], "go")
    pp.plot(analise[1], "b")
    pp.plot(analise[1][analise[1] == analise[3]].index[0], analise[3], "y*")
    pp.plot(analise[1][analise[1] == analise[5]].index[0], analise[5], "m*")
    pp.savefig(escolha)

    raw_input("Ficheiro criado com sucesso!Pressione ENTER para continuar...", )

def gravar_analise(): #Gravação das informações analisadas num ficheiro novo ou antigo.

    print "1. Novo ficheiro"
    print "2. Ficheiro ja criado"
    choice_file = input("Indique a sua opção [1-2]: ")

    if choice_file == 1:

        escolha_fich = raw_input("Qual o nome do ficheiro que pretende criar? (extensão:txt)\n ----> ", )
        file = open(escolha_fich, "w")
        file.write("''''''''''''''''''''''''''''''''''''\n")
        file.write("''''''''''''''''''''''''''''''''''''\n")
        file.write("Caracteristica|")
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[9]))
        file.write("\n\n")
        file.write('Média|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[13]))
        file.write("\n\n")
        file.write('Valor mínimo|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[7]) + ": " + str(analise[2]))
        file.write("\n\n")
        file.write('Valor máximo|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[8]) + ": " + str(analise[4]))
        file.write("\n\n''''''''''''''''''''''''''''''''''''\n")
        file.write("Caracteristica|")
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[6]))
        file.write("\n\n")
        file.write('Média|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[12]))
        file.write("\n\n")
        file.write('Valor mínimo|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[10]) + ": " + str(analise[3]))
        file.write("\n\n")
        file.write('Valor máximo|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[11]) + ": " + str(analise[5]))
        file.write("\n\n''''''''''''''''''''''''''''''''''''\n")
        file.write("''''''''''''''''''''''''''''''''''''\n")
        file.write("\n")
        file.close()

        raw_input("Ficheiro criado e dados guardados! Pressione enter para continuar...", )

    elif choice_file == 2:

        escolha_fich = raw_input("Qual o nome do ficheiro que pretende usar? (extensão:txt)\n ----> ", )
        file = open(escolha_fich, "a")
        file.write("''''''''''''''''''''''''''''''''''''\n")
        file.write("''''''''''''''''''''''''''''''''''''\n")
        file.write("Caracteristica|")
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[9]))
        file.write("\n\n")
        file.write('Média|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[13]))
        file.write("\n\n")
        file.write('Valor mínimo|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[7]) + ": " + str(analise[2]))
        file.write("\n\n")
        file.write('Valor máximo|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[8]) + ": " + str(analise[4]))
        file.write("\n\n''''''''''''''''''''''''''''''''''''\n")
        file.write("Caracteristica|")
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[6]))
        file.write("\n\n")
        file.write('Média|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[12]))
        file.write("\n\n")
        file.write('Valor mínimo|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[10]) + ": " + str(analise[3]))
        file.write("\n\n")
        file.write('Valor máximo|')
        file.write("\n")
        file.write("-------------")
        file.write("\n")
        file.write(str(analise[11]) + ": " + str(analise[5]))
        file.write("\n\n''''''''''''''''''''''''''''''''''''\n")
        file.write("''''''''''''''''''''''''''''''''''''\n")
        file.write("\n")
        file.close()

        raw_input("Dados guardados no ficheiro seleccionado! Pressione enter para continuar...", )

    else:
        raw_input("Opção não existente, tente novamente")

loop = True

while loop:

    print_menu()
    choice = raw_input("Indique a sua opção [1-8]: ")

    if choice == str(1):

        fich = raw_input("Insira o nome e localização do ficheiro .csv ou .txt. \n ----> ", )
        delimit = raw_input("Insira o delimitador do ficheiro. \n ----> ", )

        try:
            workfile = pd.read_csv(fich, sep=delimit, dtype=None, header=0)
        except IOError:
            print "\nNão foi possivel encontrar o ficheiro com esse delimitador:", fich
            raw_input("Pressione enter para tentar novamente...", )

    elif choice == str(2):
        try:
            carac(workfile)
        except:
            print "\nTem que adicionar um ficheiro primeiro"
            raw_input("Pressione enter para tentar novamente...", )

    elif choice == str(3):
        try:
            analise = analise_carac(workfile)
        except:
            print "\nTem que adicionar um ficheiro primeiro"
            raw_input("Pressione enter para tentar novamente...", )

    elif choice == str(4):
        try:
            criar_graf(analise)
        except:
            print "\nTem que escolher e analisar as caracteristicas primeiro"
            raw_input("Pressione enter para tentar novamente...", )

    elif choice == str(5):
        try:
            gravar_graf(analise)
        except:
            print "\nTem que escolher e analisar as caracteristicas primeiro"
            raw_input("Pressione enter para tentar novamente...", )

    elif choice == str(6):
        try:
            gravar_analise()
        except:
            print "\nTem que escolher e analisar as caracteristicas primeiro"
            raw_input("Pressione enter para tentar novamente...", )

    elif choice == str(7):

        print("||Obrigado por utilizar este programa||")
        loop = False

    else:
        raw_input("Opção não existente, tente novamente")
