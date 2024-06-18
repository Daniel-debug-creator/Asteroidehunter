#  Asteroides Hunter

Este projeto implementa um algoritmo genético para encontrar a melhor solução para interceptar um asteroide usando um míssil. O objetivo é calcular o ângulo e a velocidade ideais do míssil para que ele colida com o asteroide em movimento.

## Estrutura do Código

### Constantes

- `GRAVIDADE`: Aceleração da gravidade (9.81 m/s²).
- `DISTANCIA_COLISAO`: Distância máxima para considerar uma colisão (5 unidades).
- `missil_inicio`: Posição inicial do míssil ([0, 0]).

### Parâmetros do Algoritmo Genético

- `tamanho_populacao`: Número de cromossomos na população (100).
- `geracoes`: Número de gerações (1000).
- `taxa_mutacao`: Probabilidade de mutação (0.3).
- `passo_tempo`: Incremento de tempo para simulação (1 segundo).

### Funções

#### 1. `criar_cromossomo()`

Cria um cromossomo com um ângulo e uma velocidade inicial aleatórios.

#### 2. `aptidao(cromossomo, posicao_inicial_asteroide, velocidade_asteroide)`

Calcula a aptidão de um cromossomo com base na proximidade e tempo até a colisão com o asteroide.

#### 3. `cruzamento(pai1, pai2)`

Realiza o cruzamento entre dois cromossomos, gerando um novo cromossomo.

#### 4. `mutacao(cromossomo)`

Realiza a mutação de um cromossomo com base na taxa de mutação definida.

#### 5. `selecao(populacao, posicao_inicial_asteroide, velocidade_asteroide)`

Seleciona os melhores cromossomos da população com base na aptidão.

#### 6. `criar_gif(cromossomo, posicao_inicial_asteroide, velocidade_asteroide, filename)`

Cria um GIF da trajetória do míssil e do asteroide, salvando o arquivo com o nome fornecido.

#### 7. `algoritmo_genetico()`

Executa o algoritmo genético para encontrar a melhor solução (cromossomo) ao longo de várias gerações.

## Execução do Código

A execução do código começa com a chamada da função `algoritmo_genetico()`, que realiza o processo evolutivo para encontrar a melhor solução. A melhor solução encontrada é então usada para criar um GIF da simulação da trajetória do míssil e do asteroide.

### Exemplo de Uso

```python
melhor_solucao, posicao_inicial_asteroide, velocidade_asteroide = algoritmo_genetico()
print("Melhor solução:", melhor_solucao)
criar_gif(melhor_solucao, posicao_inicial_asteroide, velocidade_asteroide)
```

## Dependências

Certifique-se de ter as seguintes bibliotecas instaladas:

- `random`
- `math`
- `matplotlib`
- `imageio`
- `os`

Você pode instalar as dependências necessárias com:

```bash
pip install matplotlib imageio
```

## Conclusão

Este projeto demonstra o uso de algoritmos genéticos para resolver problemas de otimização complexos, como a interceptação de um asteroide em movimento. Através da evolução de uma população de soluções, o algoritmo é capaz de encontrar a combinação ideal de ângulo e velocidade para o míssil.
