## Metas da sprint

| **Capacidade estimada da Equipe por Sprint:** | 58 Story Points |
|-----------------------------------------------|-----------------|
| **Meta da Sprint:**                           | Spike Story (Rank 1) e User Stories de rank 2, rank 3, rank 4, rank 5 (total de *50 Story Points*) |
| **Previsão da Sprint (extras, sem compromisso de entrega):** | User Story de rank 6 (*8 Story Points*) |

# Backlog da Sprint 1

| Rank | Prioridade | User Story | Requisitos Relacionados | Estimativa (Story Points) | Sprint |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [1](#us6) |  Alta | **Spike Story:** Como um sistema de ingestão de dados geoespaciais, eu quero processar arquivos .gdb.zip de forma assíncrona e eficiente, para que eu possa disponibilizar dados tratados e georreferenciados no banco de dados para análise e visualização. | [`RF1-DATA-INGEST`](../requisitos.md#rf1-data-ingest---ingestão-de-dados-regulatórios) | - | 1 | 
| [2](#us1) |  Alta | Como um consultor comercial/técnico da Tecsys, eu quero visualizar uma tabela de classificação calculando o Índice de Criticidade (desvio percentual de DEC e FEC com base nos limites da ANEEL) de cada conjunto elétrico, para que eu possa identificar e priorizar rapidamente quais regiões possuem a pior eficiência estrutural. | [`RF1-DATA-INGEST`](../requisitos.md#rf1-data-ingest---ingestão-de-dados-regulatórios), [`RF2-ANALYTICS-CRIT`](../requisitos.md#rf2-analytics-crit---cálculo-de-criticidade-e-perdas) | 18 | 1 | 
| [3](#us2) |  Alta | Como um membro do time comercial/técnico, eu quero visualizar um gráfico de barras ordenado pelos conjuntos elétricos com maior índice SAM, para que eu saiba rapidamente quais regiões têm prioridade máxima de implantação de sensores. | [`RF2-ANALYTICS-CRIT`](../requisitos.md#rf2-analytics-crit---cálculo-de-criticidade-e-perdas) | 10 | 1 |  
| [4](#us3) |  Alta | Como um membro do time comercial/técnico, eu quero visualizar um gráfico de barras empilhadas que compare o volume absoluto (em MWh) das Perdas Técnicas (PT) e Não Técnicas (PNT) de cada conjunto elétrico, para evidenciar a magnitude das falhas estruturais da rede.| [`RF2-ANALYTICS-CRIT`](../requisitos.md#rf2-analytics-crit---cálculo-de-criticidade-e-perdas) | 10 | 1 |
| [5](#us4) |  Alta | Como um consultor comercial/técnico da Tecsys, eu quero visualizar um ranking com os 10 conjuntos elétricos com maior extensão de média tensão (TAM), para demonstrar os pontos de maior vulnerabilidade operacional.| [`RF1-DATA-INGEST`](../requisitos.md#rf1-data-ingest---ingestão-de-dados-regulatórios), [`RF2-ANALYTICS-TAM`](../requisitos.md#rf2-analytics-tam---dimensionamento-físico-tam) | 12 | 1 | 
| [6](#us5) |  Média | Como um consultor comercial/técnico da Tecsys, eu quero visualizar um mapa de calor georreferenciado indicando os circuitos mais críticos com base no Índice de Criticidade, para justificar investimentos em sensores inteligentes. | [`RF4-MAPS-HEATMAP`](../requisitos.md#rf4-maps-heatmap---mapas-de-calor-e-polígonos) | 8 | 1 | 

---

**Requisitos detalhados:** [`Clique aqui para ir até a página`](../requisitos.md)

---

## [01 - SPIKE STORY] — Processamento assíncrono de arquivos .gdb.zip <a id="us6"></a>

### Resultados Esperados

**CA6.1 - Validação da Solução (Prova de Conceito)**  

**Dado que** o sistema deve atuar como uma plataforma de ingestão de dados geoespaciais;  
**Quando** realizar a leitura de arquivos `.gdb.zip`;  
**Então** a equipe deve analisar as melhores bibliotecas e estratégias arquiteturais para extrair o Geodatabase de forma assíncrona;  
**E** carregar as feições georreferenciadas na base de dados para uso posterior.

---

## [02 - USER STORY] — Cálculo do Índice de Criticidade e Tabela de Classificação <a id="us1"></a>

### Critérios de Aceite

**CA1.1 - Cálculo correto**  

**Dado que** o sistema importa os dados regulatórios da ANEEL (Dataset de Indicadores Coletivos - DEC/FEC);  
**Quando** processar a criticidade de um conjunto elétrico com base nos limites definidos pela ANEEL e nos valores de DEC e FEC informados pela concessionária;  
**Então** o sistema deve aplicar rigorosamente a fórmula de desvio percentual.

---

**CA1.2 - Exibição da tabela**  

**Dado que** os cálculos foram concluídos;  
**Quando** o usuário acessar a tela;  
**Então** o sistema deve exibir uma tabela contendo todos os conjuntos elétricos.

---

**CA1.3 - Ordenação**  

**Dado que** os cálculos foram realizados com sucesso;  
**Quando** a tabela for exibida;  
**Então** o sistema deve apresentar os conjuntos elétricos ordenados de forma decrescente (do maior Score de Criticidade para o menor).

---

**CA1.4 - Formato dos dados**  

- O Score de Criticidade deve ser exibido em formato percentual (%).  
- Os valores de DEC e FEC devem apresentar, de forma clara, os valores **realizados** e **meta (limite)**.

---

**CA1.5 - Origem dos dados** 

**Dado que** os dados são utilizados na exibição;  
**Então** os dados apresentados devem ser provenientes do banco de dados contendo informações reais da ANEEL.

---

## [03 - USER STORY] — Gráfico de Barras do Índice de Potencial de Sensoriamento (SAM) <a id="us2"></a>

### Critérios de Aceite

**CA2.1 - Renderização do gráfico**  

**Dado que** o sistema processou o índice SAM para todos os conjuntos elétricos, considerando sua extensão e religadores;  
**Quando** o gráfico for plotado;  
**Então** o sistema deve exibir um gráfico de barras vertical, ordenado estritamente do maior valor de SAM para o menor (ordem decrescente).

---

**CA2.2 - Ordenação**  

**Dado que** os valores de SAM foram calculados;  
**Quando** o gráfico for plotado;  
**Então** as barras devem estar ordenadas estritamente do maior para o menor valor de SAM.

---

**CA2.3 - Cálculo correto**  

**Dado que** os dados necessários estão disponíveis;  
**Quando** o sistema calcular o índice SAM;  
**Então** o cálculo deve seguir exatamente a fórmula definida.

---
## [04 - USER STORY] — Gráfico de Barras Empilhadas de Perdas (PT x PNT) <a id="us3"></a>

### Critérios de Aceite

**CA3.1 - Renderização do gráfico empilhado**  
**Dado que** o sistema processou os dados em Megawatt-hora (MWh);  
**Quando** o gráfico de barras empilhadas for plotado;  
**Então** a altura total de cada barra deve representar o Volume Total de Perdas;  
**E** suas fatias internas devem respeitar a seguinte lógica:

- Eixo Y (vertical): Lista dos conjuntos elétricos  
- Eixo X (horizontal): Volume absoluto de perdas (em MWh)  
- Cada barra representa o total de perdas de um conjunto elétrico  
- O primeiro segmento da barra representa Perdas Técnicas (PT)  
- O segundo segmento, empilhado à direita, representa Perdas Não Técnicas (PNT)  

---

**CA3.2 - Cálculo exato das porcentagens**  
**Dado que** o back-end está processando os dados em MWh;  
**Quando** calcular os indicadores para exibição no gráfico;  
**Então** o sistema deve aplicar estritamente a fórmula definida.

---

**CA3.3 - Demonstração da porcentagem**  
**Dado que** o usuário está visualizando o gráfico;  
**Quando** o gráfico de barras empilhadas for exibido;  
**Então** o sistema deve apresentar, diretamente sobre cada segmento da barra (PT e PNT), o valor percentual correspondente a cada tipo de perda;  
**E** essas porcentagens devem ser calculadas com base no total de perdas (PT + PNT) do conjunto elétrico, representando a participação de cada tipo dentro do total.

**Exemplo:**
- Perdas Totais: 70 MWh  
- Perdas Técnicas: 30 MWh → 42,86%  
- Perdas Não Técnicas: 40 MWh → 57,14%

## [05 - USER STORY] — Cálculo e Visualização do TAM (Extensão de Rede) <a id="us4"></a>

### Critérios de Aceite

**CA4.1 - Cálculo da Extensão Total (TAM)**  

**Dado que** o sistema processa a base de dados geográficos da concessionária;  
**Quando** calcular o TAM de cada conjunto elétrico;  
**Então** o sistema deve realizar a soma do comprimento físico de todos os trechos de linha classificados estritamente como "Média Tensão" dentro da região de cada conjunto elétrico.

---

**CA4.2 - Renderização do Gráfico de Barras Horizontais (Top 10)**  

**Dado que** o TAM foi calculado e ordenado de forma decrescente para todos os conjuntos;  
**Quando** a tabela for exibida;  
**Então** o sistema deve renderizar um gráfico de barras horizontais exibindo exclusivamente o "Top 10" (os maiores valores);  
**E** o Eixo Y (vertical) deve exibir os nomes dos conjuntos elétricos;  
**E** o Eixo X (horizontal) deve representar a escala de tamanho numérico em quilômetros (km).

## [06 - USER STORY] — Mapa de Calor do Índice de Criticidade por Conjunto Elétrico <a id="us5"></a>

### Critérios de Aceite

**CA5.1 - Cruzamento geográfico e aplicação de cores**  

**Dado que** o Índice de Criticidade já foi calculado;  
**Quando** o mapa for renderizado;  
**Então** os segmentos de rede devem ser preenchidos com base nas seguintes regras de cor:

- 🟢 Verde: Criticidade igual a 0% (dentro ou muito próximo da meta)  
- 🟠 Laranja: Criticidade entre 0% e 10% (regiões que demandam atenção)  
- 🔴 Vermelho: Criticidade maior que 10% (alta criticidade, foco prioritário)  

---

**CA5.2 - Carregamento do mapa base e linhas de distribuição**  

**Dado que** o usuário visualizar ou exportar os dados;  
**Quando** o mapa geográfico for renderizado;  
**Então** o sistema deve exibir as linhas de distribuição de energia (alimentadores) sobrepostas ao mapa da região de concessão.