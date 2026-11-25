
# -*- coding: utf-8 -*
# fase2_caminhos.py — Fase 2: funções, custo de um caminho e os valores g, h e f.
# Rode com: python fase2_caminhos.py

# ----- PASSO 1: importar os dados ----
# Importa o mapa da Romênia e a heurística até Bucareste.
from mapa import mapa_romenia, heuristica_bucareste

print('Mapa da Romenia e heuristicas carregados!')
print()

# ----- PASSO 2: função que devolve o custo de UMA estrada ----
def custo_da_estrada(origem, destino):
    """Devolve os km da estrada origem -> destino, ou None se ela não existe."""

    # Percorre os vizinhos da cidade de origem.
    for vizinho, custo in mapa_romenia[origem]:

        # Verifica se o vizinho é a cidade de destino.
        if vizinho == destino:
            return custo

    # Se não encontrar a cidade, significa que não existe estrada direta.
    return None


# ----- PASSO 3: função que soma o custo de um caminho inteiro ----
# Tive que corrigir o return desta parte.
# Ele precisa ficar fora do for para somar todas as estradas.
def custo_do_caminho(caminho):
    """Recebe uma lista de cidades e devolve a soma das estradas, em km."""

    total = 0

    # Percorre cada par de cidades consecutivas do caminho.
    for i in range(len(caminho) - 1):

        # Soma o custo da estrada entre a cidade atual e a próxima.
        total = total + custo_da_estrada(caminho[i], caminho[i + 1])

    # Retorna o custo total depois de percorrer todas as estradas.
    return total


# ----- PASSO 4: testar as funções ----

print('--- TESTE DO CUSTO DE UMA ESTRADA ---')

# Testa uma estrada que existe no mapa.
print('Arad -> Sibiu custa', custo_da_estrada('Arad', 'Sibiu'), 'km')

# Testa uma ligação que não existe diretamente.
print('Arad -> Bucharest custa', custo_da_estrada('Arad', 'Bucharest'),
      '(não existe estrada direta)')

# Define dois caminhos possíveis de Arad até Bucareste.
por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']

print()
print('--- TESTE DO CUSTO DE CAMINHOS COMPLETOS ---')

# Mostra o caminho que passa por Fagaras e calcula seu custo.
print('Caminho por Fagaras:', ' -> '.join(por_fagaras))
print('   custo =', custo_do_caminho(por_fagaras), 'km')

# Mostra o caminho que passa por Pitesti e calcula seu custo.
print('Caminho por Pitesti:', ' -> '.join(por_pitesti))
print('   custo =', custo_do_caminho(por_pitesti), 'km')


# ----- PASSO 5: g(n), h(n) e f(n) ao longo de um caminho ----
def mostrar_g_h_f(caminho):
    """
    Para cada cidade do caminho imprime:
    g = custo já percorrido
    h = estimativa da distância que falta
    f = soma de g + h
    """

    print(f'  {"cidade":<15} {"g(n)":>5} {"h(n)":>5} {"f(n)":>5}')

    # Percorre todas as cidades do caminho.
    for i in range(len(caminho)):

        # Cidade que está sendo analisada no momento.
        cidade = caminho[i]

        # g(n): calcula o custo acumulado desde Arad até a cidade atual.
        g = custo_do_caminho(caminho[:i + 1])

        # h(n): consulta a heurística, ou seja, a estimativa até Bucareste.
        h = heuristica_bucareste[cidade]

        # f(n): soma o custo percorrido com a estimativa do que falta.
        f = g + h

        # Exibe os valores organizados em colunas.
        print(f'  {cidade:<15} {g:>5} {h:>5} {f:>5}')

# Primeiro caminho: passando por Fagaras.
print()
print('Valores ao longo do caminho por Fagaras:')
mostrar_g_h_f(por_fagaras)

# Segundo caminho: passando por Pitesti.
print()
print('Valores ao longo do caminho por Pitesti:')
mostrar_g_h_f(por_pitesti)

print()
print('==========================================')
print('          FIM DA EXECUCAO')
print('==========================================')
