import random
import math
import matplotlib.pyplot as plt
import imageio
import os

GRAVIDADE = 9.81
DISTANCIA_COLISAO = 5

missil_inicio = [0, 0]

tamanho_populacao = 100
geracoes = 1000
taxa_mutacao = 0.3
passo_tempo = 1

def criar_cromossomo():
    """
    Cria um cromossomo com ângulo e velocidade inicial.

    Returns
    -------
    tuple
        Um cromossomo representado por (ângulo, velocidade).
    """
    return (random.uniform(math.pi/8, math.pi/2), random.uniform(100, 3000))

def fitness(cromossomo, posicao_inicial_asteroide, velocidade_asteroide):
    """
    Calcula a aptidão do cromossomo com base na distância e tempo.

    Parameters
    ----------
    cromossomo : tuple
        Cromossomo representado por (ângulo, velocidade).
    posicao_inicial_asteroide : list
        Posição inicial do asteroide [x, y].
    velocidade_asteroide : list
        Velocidade do asteroide [vx, vy].

    Returns
    -------
    float
        Valor de aptidão do cromossomo.
    """
    angulo, velocidade = cromossomo
    x, y = missil_inicio
    ast_x, ast_y = posicao_inicial_asteroide
    velocidade_y = 0
    tempo_decorrido = 0
    
    while y >= 0:
        velocidade_y -= GRAVIDADE * passo_tempo
        x += math.cos(angulo) * velocidade * passo_tempo
        y += (math.sin(angulo) * velocidade + velocidade_y) * passo_tempo
        ast_x += velocidade_asteroide[0] * passo_tempo
        ast_y += velocidade_asteroide[1] * passo_tempo
        tempo_decorrido += passo_tempo
        
        distancia = math.sqrt((x - ast_x)**2 + (y - ast_y)**2)
        if distancia < DISTANCIA_COLISAO:
            return 1000 / (tempo_decorrido + 1)
        
        if y < 0:
            y = 0
            break
    
    distancia = math.sqrt((x - ast_x)**2 + (y - ast_y)**2)
    return 1 / (distancia + 1 + tempo_decorrido)

def cruzamento(pai1, pai2):
    """
    Realiza o cruzamento entre dois cromossomos.

    Parameters
    ----------
    pai1 : tuple
        Cromossomo do primeiro pai (ângulo, velocidade).
    pai2 : tuple
        Cromossomo do segundo pai (ângulo, velocidade).

    Returns
    -------
    tuple
        Novo cromossomo gerado pelo cruzamento.
    """
    if random.random() < 0.5:
        angulo = pai1[0]

    else:
        angulo = pai2[0]
    if random.random() < 0.5:
        velocidade = pai1[1]
    else:
        velocidade = pai2[1]   
    return (angulo, velocidade)

def mutacao(cromossomo):
    """
    Realiza a mutação de um cromossomo.

    Parameters
    ----------
    cromossomo : tuple
        Cromossomo a ser mutado (ângulo, velocidade).

    Returns
    -------
    tuple
        Cromossomo mutado.
    """
    angulo, velocidade = cromossomo
    if random.random() < taxa_mutacao:
        angulo += random.uniform(-math.pi/18, math.pi/18)
        velocidade += random.uniform(-50, 50)
        angulo = max(0, min(angulo, math.pi/2))
        velocidade = max(10, min(velocidade, 300))
    return (angulo, velocidade)

def selecao(populacao, posicao_inicial_asteroide, velocidade_asteroide):
    """
    Seleciona os melhores cromossomos da população.

    Parameters
    ----------
    populacao : list
        Lista de cromossomos.
    posicao_inicial_asteroide : list
        Posição inicial do asteroide [x, y].
    velocidade_asteroide : list
        Velocidade do asteroide [vx, vy].

    Returns
    -------
    list
        Lista de cromossomos selecionados.
    """
    populacao.sort(key=lambda crom: fitness(crom, posicao_inicial_asteroide, velocidade_asteroide), reverse=True)
    selecionados = populacao[:tamanho_populacao//2]
    return selecionados + random.choices(selecionados, k=tamanho_populacao//2)

def algoritmo_genetico():
    """
    Executa o algoritmo genético para encontrar a melhor solução.

    Returns
    -------
    tuple
        Melhor cromossomo, posição inicial do asteroide, velocidade do asteroide.
    """
    posicao_inicial_asteroide = [random.uniform(500, 2000), random.uniform(1000, 3000)]
    velocidade_asteroide = [random.uniform(-50, 50), random.uniform(-50, 50)]
    populacao = [criar_cromossomo() for _ in range(tamanho_populacao)]
    melhor_fitness = float('-inf')
    melhor_cromossomo = None

    for geracao in range(geracoes):
        populacao = selecao(populacao, posicao_inicial_asteroide, velocidade_asteroide)
        proxima_geracao = []
        for i in range(0, len(populacao), 2):
            pai1, pai2 = populacao[i], populacao[i+1]
            filho1 = cruzamento(pai1, pai2)
            proxima_geracao.extend([mutacao(filho1)])
            
        populacao = proxima_geracao
        melhor_cromossomo_atual = max(populacao, key=lambda crom: fitness(crom, posicao_inicial_asteroide, velocidade_asteroide))
        melhor_fitness_atual = fitness(melhor_cromossomo_atual, posicao_inicial_asteroide, velocidade_asteroide)

        if melhor_fitness_atual > melhor_fitness:
            melhor_fitness = melhor_fitness_atual
            melhor_cromossomo = melhor_cromossomo_atual
        
        print(f"Geração {geracao}: Melhor Fitness = {melhor_fitness}")

    return melhor_cromossomo, posicao_inicial_asteroide, velocidade_asteroide

def criar_gif(cromossomo, posicao_inicial_asteroide, velocidade_asteroide, filename="simulacao.gif"):
    """
    Cria um GIF da simulação.

    Parameters
    ----------
    cromossomo : tuple
        Cromossomo (ângulo, velocidade) a ser simulado.
    posicao_inicial_asteroide : list
        Posição inicial do asteroide [x, y].
    velocidade_asteroide : list
        Velocidade do asteroide [vx, vy].
    filename : str
        Nome do arquivo para salvar o GIF.

    Returns
    -------
    None
    """
    angulo, velocidade = cromossomo
    x, y = missil_inicio
    ast_x, ast_y = posicao_inicial_asteroide
    velocidade_y = 0
    posicoes_missil = [(x, y)]
    posicoes_asteroide = [(ast_x, ast_y)]
    
    while y >= 0:
        velocidade_y -= GRAVIDADE * passo_tempo
        x += math.cos(angulo) * velocidade * passo_tempo
        y += (math.sin(angulo) * velocidade + velocidade_y) * passo_tempo
        ast_x += velocidade_asteroide[0] * passo_tempo
        ast_y += velocidade_asteroide[1]* passo_tempo 
        
        distancia = math.sqrt((x - ast_x)**2 + (y - ast_y)**2)
        if distancia < DISTANCIA_COLISAO:
            break
        
        if y < 0:
            y = 0
            break
        posicoes_missil.append((x, y))
        posicoes_asteroide.append((ast_x, ast_y))
    
    frames = []
    for i in range(len(posicoes_missil)):
        fig, ax = plt.subplots()
        ax.clear()
        ax.plot([pos[0] for pos in posicoes_missil[:i+1]], [pos[1] for pos in posicoes_missil[:i+1]], 'r-', label='Missil')
        ax.plot([pos[0] for pos in posicoes_asteroide[:i+1]], [pos[1] for pos in posicoes_asteroide[:i+1]], 'bo', label='Asteroide')
        ax.legend()
        ax.set_xlim(0, 5000)
        ax.set_ylim(0, 5000)
        ax.set_xlabel('Posição X')
        ax.set_ylabel('Posição Y')
        ax.set_title('Missil vs Asteroide')
        plt.grid(True)
        
        frame_filename = f"frame_{i}.png"
        plt.savefig(frame_filename)
        plt.close()
        frames.append(imageio.imread(frame_filename))
        os.remove(frame_filename)
    
    imageio.mimsave(filename, frames, duration=0.1)
    print(f"GIF salvo como {filename}")
    
melhor_solucao, posicao_inicial_asteroide, velocidade_asteroide = algoritmo_genetico()
print("Melhor solução:", melhor_solucao)
criar_gif(melhor_solucao, posicao_inicial_asteroide, velocidade_asteroide)
