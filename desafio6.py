
# -*- coding: utf-8 -*-
# desafio6.py — Desafios da busca A*.
# Rode com: python desafio6.py

# ----- PASSO 1: importar os dados ----
from mapa import mapa_romenia, heuristica_bucareste


# ----- PASSO 2: função de apoio para imprimir a fronteira ----
def resumo_fronteira(fronteira):
    """Mostra as cidades da fronteira e seus valores de f."""
    return ', '.join(f'{cidade}({f})' for f, g, cidade, caminho in fronteira)


# ----- PASSO 3: função da busca A* com contador de iterações ----
def busca_a_estrela(inicio, objetivo, grafo, heuristica, mostrar=True):
    """
    Devolve caminho, custo e quantidade de iterações.

    Cada nó da fronteira possui:
    (f, g, cidade, caminho)
    """

    # Cria a fronteira inicial com a cidade de origem.
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]

    # Guarda as cidades que já foram exploradas.
    explorados = set()

    # Contador de quantas vezes o while executou.
    iteracao = 0

    if mostrar:
        print(f'--- Busca A* de {inicio} para {objetivo} ---')

    # Continua enquanto existirem nós na fronteira.
    while fronteira:

        # Conta mais uma iteração do laço.
        iteracao = iteracao + 1

        # Ordena a fronteira pelo menor valor de f.
        fronteira.sort(key=lambda no: no[0])

        # Retira o nó com menor f.
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        if mostrar:
            print(f'{iteracao}. Expandindo: {cidade_atual} | '
                  f'g(n)={g_atual}, h(n)={heuristica[cidade_atual]} '
                  f'-> f(n)={f_atual}')

        # Verifica se chegou ao objetivo.
        if cidade_atual == objetivo:
            return caminho, g_atual, iteracao

        # Se a cidade já foi explorada, pula para a próxima.
        if cidade_atual in explorados:
            continue

        explorados.add(cidade_atual)

        # Gera os vizinhos da cidade atual.
        for vizinho, custo_estrada in grafo.get(cidade_atual, []):
            if vizinho not in explorados:

                # Calcula o novo custo percorrido.
                novo_g = g_atual + custo_estrada

                # Calcula o novo custo estimado.
                novo_f = novo_g + heuristica[vizinho]

                # Adiciona o novo nó na fronteira.
                fronteira.append(
                    (novo_f, novo_g, vizinho, caminho + [vizinho])
                )

        if mostrar:
            fronteira.sort(key=lambda no: no[0])
            print('   fronteira:', resumo_fronteira(fronteira))

    # Caso não encontre um caminho.
    return None, float('inf'), iteracao


# ----- PASSO 4: criar uma heurística com valor zero ----

# ALTERAÇÃO: todos os valores de h(n) passam a ser zero.
# Assim, a busca deixa de usar a estimativa até Bucareste
# e passa a escolher os nós apenas pelo custo já percorrido (g).
h_zero = {c: 0 for c in mapa_romenia}


# ----- PASSO 5: comparar A* normal com heurística zero ----

print('==========================================')
print('       DESAFIO 1 - HEURISTICA ZERO')
print('==========================================')
print()

# Executa a busca usando a heurística original.
caminho, custo, iteracoes = busca_a_estrela(
    'Arad', 'Bucharest', mapa_romenia, heuristica_bucareste
)

print()
print('--- Resultado com heurística original ---')
print('Caminho:', ' -> '.join(caminho))
print('Custo:', custo, 'km')
print('Iterações:', iteracoes)

# Executa novamente usando a heurística zero.
caminho_zero, custo_zero, iteracoes_zero = busca_a_estrela(
    'Arad', 'Bucharest', mapa_romenia, h_zero, mostrar=False
)

print()
print('--- Resultado com heurística zero ---')
print('Caminho:', ' -> '.join(caminho_zero))
print('Custo:', custo_zero, 'km')
print('Iterações:', iteracoes_zero)

# Compara os resultados das duas buscas.
print()
print('--- Comparação ---')
print('Custo com heurística original:', custo, 'km')
print('Custo com heurística zero:', custo_zero, 'km')
print('Iterações com heurística original:', iteracoes)
print('Iterações com heurística zero:', iteracoes_zero)


# ----- PASSO 6: testar outras cidades como origem ----

print()
print('==========================================')
print('       DESAFIO 2 - OUTRAS ORIGENS')
print('==========================================')

# Lista das cidades que serão utilizadas como origem.
for origem in ['Lugoj', 'Mehadia', 'Eforie']:

    # Executa a busca de cada cidade até Bucareste.
    caminho, custo, iteracoes = busca_a_estrela(
        origem, 'Bucharest', mapa_romenia,
        heuristica_bucareste, mostrar=False
    )

    print()
    print('Origem:', origem)

    if caminho:
        print('Caminho:', ' -> '.join(caminho))
        print('Custo:', custo, 'km')
        print('Iterações:', iteracoes)
    else:
        print('Não foi possível encontrar um caminho.')


# ----- PASSO 7: fim da execução ----

print()
print('==========================================')
print('          FIM DOS DESAFIOS')
print('==========================================')