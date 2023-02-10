'''Pedro Balle Sanguinetti
   107283
   LEIC-T'''

#TAD Gerador
def cria_gerador(bits, seed):
    if not isinstance(bits, int) or not isinstance(seed, int):
        raise ValueError('cria_gerador: argumentos invalidos')
    if seed < 1:
        raise ValueError('cria_gerador: argumentos invalidos')
    if bits != 32 and bits != 64:
        raise ValueError('cria_gerador: argumentos invalidos')
    if bits == 32 and seed > 0xFFFFFFFF:
        raise ValueError('cria_gerador: argumentos invalidos')
    if bits == 64 and seed > 0xFFFFFFFFFFFFFFFF:
        raise ValueError('cria_gerador: argumentos invalidos')
    return[bits, seed]

def cria_copia_gerador(gerador):
    return gerador.copy()

    #seletores
def obtem_estado(gerador):
    return gerador[1]

    #modificadores
def define_estado(gerador, s):
    gerador = gerador[:0] + [s]
    return s

def atualiza_estado(gerador):
    if gerador[0] == 32:
        gerador[1] ^= (gerador[1] << 13) & 0xFFFFFFFF
        gerador[1] ^= (gerador[1] >> 17) & 0xFFFFFFFF
        gerador[1] ^= (gerador[1] << 5) & 0xFFFFFFFF
    else:
        gerador[1] ^= (gerador[1] << 13) & 0xFFFFFFFFFFFFFFFF
        gerador[1] ^= (gerador[1] >> 7) & 0xFFFFFFFFFFFFFFFF
        gerador[1] ^= (gerador[1] << 17) & 0xFFFFFFFFFFFFFFFF
    return gerador[1]

    #reconhecedores
def eh_gerador(gerador):
    if not isinstance(gerador, list):
        return False
    if len(gerador) != 2:
        return False
    if not isinstance(gerador[0], int) or\
         not isinstance(gerador[1], int):
        return False
    if gerador[1] < 1:
        return False
    if gerador[0] != 32 and gerador[0] != 64:
        return False
    if (gerador[0] == 32 and gerador[1] > 0xFFFFFFFF) or \
        (gerador[0] == 64 and gerador[1] > 0xFFFFFFFFFFFFFFFF):
        return False
    
    return True

    #testes
def geradores_iguais(gerador1, gerador2):
    if gerador1[0] == gerador2[0] and gerador1[1] == gerador2[1]:
        return True
    return False

    #transformador
def gerador_para_str(gerador):
    return 'xorshift' + str(gerador[0]) + '(s=' + str(gerador[1]) + ')'

    #funçoes de alto nível
def gera_numero_aleatorio(gerador, n):
    atualizado = atualiza_estado(gerador)
    return 1 + (atualizado % n)

def gera_carater_aleatorio(gerador, c):
    atualizado = atualiza_estado(gerador)
    length = (ord(c) + 1) - ord('A')
    return chr(ord('A') + atualizado % length)

#TAD coordenada
    #construtor
def cria_coordenada(coluna, linha):
    if not isinstance(coluna, str) or not isinstance(linha, int):
        raise ValueError('cria_coordenada: argumentos invalidos')
    if len(coluna) > 1:
        raise ValueError('cria_coordenada: argumentos invalidos')
    if coluna < 'A' or coluna > 'Z':
        raise ValueError('cria_coordenada: argumentos invalidos')
    if linha < 1 or linha > 99:
        raise ValueError('cria_coordenada: argumentos invalidos')
    if linha <= 9:
        return coluna + '0' + str(linha) 
    return coluna + str(linha)

#seletores
def obtem_coluna(coordenada):
    return coordenada[0]

def obtem_linha(coordenada):
    return int(coordenada[1:])

    #reconhecedores
def eh_coordenada(coordenada):
    if not isinstance(coordenada, str):
        return False
    if len(coordenada) > 3:
        return False
    if coordenada[0] < 'A' or coordenada[0] > 'Z':
        return False
    for i in coordenada[1:]:
        if i < '0' or i > '9':
            return False
    return True

    #testes
def coordenadas_iguais(coordenada1, coordenada2):
    if coordenada1[0] == coordenada2[0] and \
        coordenada1[1:] == coordenada2[1:]:
        return True
    return False

    #transformadores
def coordenada_para_str(coordenada):
    return coordenada

def str_para_coordenada(cadeia):
    return cadeia

    #funções de alto nível
def obtem_coordenadas_vizinhas(coordenada):
    #tuplo contendo as coordenadas vizinhas
    if obtem_linha(coordenada) < 9:
        tup = (chr(ord(obtem_coluna(coordenada))-1) + '0' + str(int(obtem_linha(coordenada))-1),\
             obtem_coluna(coordenada) + '0' + str(int(obtem_linha(coordenada))-1),\
             chr(ord(obtem_coluna(coordenada))+1) + '0' + str(int(obtem_linha(coordenada))-1),\
             chr(ord(obtem_coluna(coordenada))+1) + '0' + str(obtem_linha(coordenada)),\
             chr(ord(obtem_coluna(coordenada))+1) + '0' + str(int(obtem_linha(coordenada))+1),\
             obtem_coluna(coordenada) + '0' + str(int(obtem_linha(coordenada))+1),\
             chr(ord(obtem_coluna(coordenada))-1) + '0' + str(int(obtem_linha(coordenada))+1),\
             chr(ord(obtem_coluna(coordenada))-1) + '0' + str(obtem_linha(coordenada)))
    else:
        tup = (chr(ord(obtem_coluna(coordenada))-1) + str(int(obtem_linha(coordenada))-1),\
             obtem_coluna(coordenada) + str(int(obtem_linha(coordenada))-1),\
             chr(ord(obtem_coluna(coordenada))+1) + str(int(obtem_linha(coordenada))-1),\
             chr(ord(obtem_coluna(coordenada))+1) + str(obtem_linha(coordenada)),\
             chr(ord(obtem_coluna(coordenada))+1) + str(int(obtem_linha(coordenada))+1),\
             obtem_coluna(coordenada) + str(int(obtem_linha(coordenada))+1),\
             chr(ord(obtem_coluna(coordenada))-1) + str(int(obtem_linha(coordenada))+1),\
             chr(ord(obtem_coluna(coordenada))-1) + str(obtem_linha(coordenada)))
    #filtra as coordenadas vizinhas que não estejam no tabuleiro
    i = 0
    while i < len(tup):
        if tup[i][0] < 'A' or tup[i][0] > 'Z' or int(tup[i][1:]) < 1 or int(tup[i][1:]) > 99:
            tup = tup[:i] + tup[i+1:]
        else:
            i += 1
    return tup

def obtem_coordenada_aleatoria(coordenada, gerador):
    coluna_aleatoria = str(gera_carater_aleatorio(gerador, obtem_coluna(coordenada)))
    linha_aleatoria  =str(gera_numero_aleatorio(gerador, obtem_linha(coordenada)))
    if int(linha_aleatoria) <= 9:
        return coluna_aleatoria + '0' + linha_aleatoria
    return coluna_aleatoria + linha_aleatoria
    
#TAD parcela
    #construtores
def cria_parcela():
    return ['T',0]

def cria_copia_parcela(parcela):
    return parcela.copy()
    
    #modificadores
def limpa_parcela(parcela):
    parcela[0] = 'L'
    return parcela

def marca_parcela(parcela):
    parcela[0] = 'F'
    return parcela

def desmarca_parcela(parcela):
    parcela[0] = 'T'
    return parcela

def esconde_mina(parcela):
    parcela[1] = 'M'  
    return parcela

    #reconhecedores
def eh_parcela(parcela):
    if not isinstance(parcela, list):
        return False
    if not (len(parcela) == 2):
        return False
    if not (parcela[0] == 'L' or parcela[0] == 'F' or parcela[0] == 'T' or\
         parcela[1] == 'M' or parcela[1] == 0):
        return False
    return True

def eh_parcela_tapada(parcela):
    if eh_parcela(parcela) and parcela[0] == 'T':
        return True
    return False

def eh_parcela_marcada(parcela):
    if eh_parcela(parcela) and parcela[0] == 'F':
        return True
    return False

def eh_parcela_limpa(parcela):
    if eh_parcela(parcela) and parcela[0] == 'L':
        return True
    return False

def eh_parcela_minada(parcela):
    if eh_parcela(parcela) and parcela[1] == 'M':
        return True
    return False

    #testes
def parcelas_iguais(parcela1, parcela2):
    if eh_parcela(parcela1) and eh_parcela(parcela2) and parcela1 == parcela2:
        return True
    return False

    #transformadores
def parcela_para_str(parcela):
    if eh_parcela_tapada(parcela):
        return '#'
    if eh_parcela_marcada(parcela):
        return '@'
    if eh_parcela_limpa(parcela) and not eh_parcela_minada(parcela):
        return '?'
    if eh_parcela_minada(parcela) and eh_parcela_limpa(parcela):
        return 'X'

    #funções de alto nível
def alterna_bandeira(parcela):
    if eh_parcela_marcada(parcela):
        parcela = desmarca_parcela(parcela)
        return True
    if eh_parcela_tapada(parcela):
        parcela = marca_parcela(parcela)
        return True
    return False

#TAD campo
    #construtores
def cria_campo(col_max, lin_max):
    campo = {}
    if not isinstance(col_max, str) or not isinstance(lin_max, int):
        raise ValueError('cria_campo: argumentos invalidos')
    if len(col_max) != 1:
        raise ValueError('cria_campo: argumentos invalidos')
    if col_max > 'Z' or col_max < 'A' or lin_max < 1 or lin_max > 99:
        raise ValueError('cria_campo: argumentos invalidos')
    for c in range(ord('A'), ord(col_max)+1):
        for l in range(1, lin_max +1):
            campo[cria_coordenada(chr(c), l)] = cria_parcela()
    return campo

def cria_copia_campo(campo):
    return campo.copy()

    #seletores
def obtem_ultima_coluna(campo):
    maior_col = 'A'
    for k in campo.keys():
        if k[0] > maior_col:
            maior_col = k[0]
    return maior_col

def obtem_ultima_linha(campo):
    maior_col = 1
    for k in campo.keys():
        if int(k[1:]) > maior_col:
            maior_col = int(k[1:])
    return maior_col

def obtem_parcela(campo, coordenada):
    return campo[coordenada]

def obtem_coordenadas(campo, tipo):
    #cria um tuplo com as coordenadas do tipo requerido e depois coloca o mesmo na ordem requerida atravez de uma adaptação do bubble sort classico
    coordenadas = ()
    l = 0
    if tipo == 'limpas':
        for k,i in campo.items():
            if i[0] == 'L':
                coordenadas += (k,)
    if tipo == 'tapadas':
        for k,i in campo.items():
            if i[0] == 'T':
                coordenadas += (k,)
    if tipo == 'marcadas':
        for k,i in campo.items():
            if i[0] == 'F':
                coordenadas += (k,)
    if tipo == 'minadas':
        for k,i in campo.items():
            if i[1] == 'M':
                coordenadas += (k,)
    while l < len(coordenadas):
        j = 0
        while j < len(coordenadas) - l - 1:
            if int(coordenadas[j][1:]) > int(coordenadas[j + 1][1:]):
               coordenadas = coordenadas[:j] + (coordenadas[j + 1],) + (coordenadas[j],) + coordenadas[j + 2:]
            if int(coordenadas[j][1:]) == int(coordenadas[j + 1][1:]) and coordenadas[j][0] > coordenadas[j + 1][0]:
                coordenadas = coordenadas[:j] + (coordenadas[j + 1],) + (coordenadas[j],) + coordenadas[j + 2:]
            j += 1
        l += 1
    return coordenadas

def obtem_numero_minas_vizinhas(campo, coordenada):
    contador = 0
    minas = obtem_coordenadas(campo, 'minadas')
    for i in obtem_coordenadas_vizinhas(coordenada):
        if i in minas:
            contador += 1
    return contador

    #reconhecedores
def eh_campo(campo):
    if not isinstance(campo, dict):
        return False
    for k,i in campo.items():
        if not eh_coordenada(k) or not eh_parcela(i):
            return False
        if k[0] < 'A' or k[0] > 'Z' or int(k[1:]) < 1 or int(k[1:]) > 99:
            return False
    return True

def eh_coordenada_do_campo(campo, coordenada):
    if coordenada in campo.keys():
        return True
    return False

    #testes
def campos_iguais(campo1, campo2):
    if eh_campo(campo1) and eh_campo(campo2) and campo1 == campo2:
        return True
    return False

    #transformadores
def campo_para_str(campo):
    #gera as duas primeiras linhas obtendo as colunas presentes no campo atual
    #obtem as linhas do campo e gera as linhas com parcelas usando da representação em string das mesmas
    #gera a última linha, que é igual à segunda
    matriz = '   '
    colunas = ''
    linhas = ()
    for i in campo.keys():
        if i[0] not in colunas:
            colunas += i[0]
    colunas = sorted(colunas)
    for s in colunas:
        matriz += s
    matriz += '\n  +'
    matriz += '-' * len(colunas)
    matriz += '+\n'
    for l in campo.keys():
        if l[1:] not in linhas:
            linhas += (l[1:],)
    for n in linhas:
        matriz += n + '|'
        for k in colunas:
            if parcela_para_str(campo[k + n]) == '?':
                if obtem_numero_minas_vizinhas(campo, k + n):
                    matriz += str(obtem_numero_minas_vizinhas(campo, k + n))
                else:
                    matriz += ' '
            else:
                matriz += parcela_para_str(campo[k + n])
        matriz += '|\n'
    matriz += '  +'
    matriz += '-' * len(colunas)
    matriz += '+'
    return matriz

    #funções de alto nível
def coloca_minas(campo, coordenada, gerador, n_minas):
    #é gerada uma coordenada aleatória em uma cópia da coordenada dada.
    # se a coordenada aleatoria não pertencer a vizinhança da coordenada inicial ou não for a própria, é colocada uma mina na parcela correspondente
    coordenada_aleatoria = coordenada[:]
    contador_minas = 0
    while contador_minas < n_minas:
        coordenada_aleatoria = obtem_coordenada_aleatoria(cria_coordenada(\
            obtem_ultima_coluna(campo), obtem_ultima_linha(campo)), gerador)
        if coordenada_aleatoria != coordenada and\
             coordenada_aleatoria not in obtem_coordenadas_vizinhas(coordenada) and\
                 coordenada_aleatoria not in obtem_coordenadas(campo, 'minadas'):
            esconde_mina(obtem_parcela(campo, coordenada_aleatoria))
            contador_minas += 1
    return campo

def limpa_campo(campo, coordenada):
    #limpa a parcela atual, se não for marcada, e se a visinhança não tiver minas realiza recursão pelas parcelas vizinhas à atual.
    #se a parcela atual ja for limpa, quer dizer que a função ja passou por ela, por isso retorna o campo.
    if eh_parcela_limpa(obtem_parcela(campo, coordenada)):
        return campo
    if not eh_parcela_marcada(obtem_parcela(campo, coordenada)):
        limpa_parcela(obtem_parcela(campo, coordenada))
    vizinhas = obtem_coordenadas_vizinhas(coordenada)
    visitar = ()
    vizinhanca_limpa = True
    for f in vizinhas:
        if f in obtem_coordenadas(campo, 'minadas'):
            vizinhanca_limpa = False
    if vizinhanca_limpa:
        for i in vizinhas:
            if eh_coordenada_do_campo(campo, i):
                visitar += (i,)
        for l in visitar:
            if eh_parcela_tapada(obtem_parcela(campo, l)):
                limpa_campo(campo, l)
    return campo 

#funções adicionais
def jogo_ganho(campo):
    parcelas_limpas = 0
    parcelas_minadas = 0
    parcelas_total = 0
    #conta as parcelas limpas e minadas e se a soma das duas quantidades for o número de parcelas no campo o jogo esta ganho, se não, ainda não acabou 
    for i in campo.values():
        if eh_parcela_limpa(i):
            parcelas_limpas += 1
        if eh_parcela_minada(i):
            parcelas_minadas += 1
        parcelas_total += 1
    if parcelas_limpas + parcelas_minadas == parcelas_total:
        return True
    return False

def turno_jogador(campo):
    x = 0
    y = '000'
    #recebe os inputs do jogador
    while x != 'L' and x != 'M':
        x = str(input('Escolha uma ação, [L]impar ou [M]arcar:'))
    while not eh_coordenada_do_campo(campo, y):
        y = str(input('Escolha uma coordenada:'))
    #realiza as operações desejadas pelo jogador
    if x == 'L' and not eh_parcela_minada(obtem_parcela(campo, cria_coordenada(y[0], int(y[1:])))):
        limpa_campo(campo,  cria_coordenada(y[0], int(y[1:])))
    elif x == 'M':
        marca_parcela(obtem_parcela(campo,  cria_coordenada(y[0], int(y[1:]))))
    if eh_parcela_minada(obtem_parcela(campo,  cria_coordenada(y[0], int(y[1:])))) and x == 'L':
        limpa_parcela(obtem_parcela(campo,  cria_coordenada(y[0], int(y[1:]))))
        return False
    else:
        return True
    
def minas(col, lin, n_minas, bits, seed):
    campo = cria_campo(col, lin)
    gerador = cria_gerador(bits, seed)
    y = '000'
    contador_bandeiras = 0
    #faz o print da iinterface inicial
    print('   [Bandeiras ' + str(contador_bandeiras) + '/' + str(n_minas) + ']')
    print(campo_para_str(campo))
    #obtem o primeiro input para depois gerar as minas e limpar o campo
    while not eh_coordenada_do_campo(campo, y):
        y = str(input('Escolha uma coordenada:'))
    campo = coloca_minas(campo, y, gerador, n_minas)
    limpa_campo(campo, y)
    #faz com que o jogador jogue até ganhar ou limpar uma mina e printa as interfaces alem de retornar os valores pedidos
    while not jogo_ganho(campo):
        marcadas = obtem_coordenadas(campo, 'marcadas')
        contador_bandeiras = len(marcadas)
        print('   [Bandeiras ' + str(contador_bandeiras) + '/' + str(n_minas) + ']')
        print(campo_para_str(campo))
        if not turno_jogador(campo):
            print('   [Bandeiras ' + str(contador_bandeiras) + '/' + str(n_minas) + ']')
            print(campo_para_str(campo))
            print('BOOOOOOOM!!!')
            return False
    print('   [Bandeiras ' + str(contador_bandeiras) + '/' + str(n_minas) + ']')
    print(campo_para_str(campo))
    print('VITORIA!!!')
    return True

#pra jogar chama a função minas(colunas no campo(uma letramaiuscula), linhas no campo( 1-99),o número de minas no campo, o número de bits do gerador(32/64), seed do gerador, um número entre 1 e o máximo dos integers)
#é importante que não tenha tabs nem espaços antes da chamada da função e não precisa de ';' depois da função

minas('Y', 25, 40, 64, 2499999999)