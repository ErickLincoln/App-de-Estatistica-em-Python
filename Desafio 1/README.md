<h1>Quartis</h1>
<p>Este é um programa Python que implementa uma função <code>quartiles</code> para calcular os três quartis de uma lista de números. A função recebe uma lista <code>arr</code> como parâmetro e retorna uma lista contendo os valores dos quartis Q1, Q2 e Q3.</p>
<p>O programa importa as bibliotecas <code>math</code>, <code>os</code>, <code>random</code>, <code>re</code> e <code>sys</code>, mas apenas a <code>os</code> é usada para escrever o resultado em um arquivo de saída. A função <code>quartiles</code> primeiro classifica a lista em ordem crescente, em seguida, divide a lista em duas partes iguais ou quase iguais dependendo do comprimento da lista. Então, chama a função <code>mediana</code> para calcular a mediana de cada uma dessas duas partes e a mediana da lista inteira para obter os três quartis.</p>
<p>A função <code>mediana</code> simplesmente calcula a mediana de uma lista de números. Se a lista tiver um número par de elementos, a mediana é a média dos dois elementos do meio. Caso contrário, a mediana é o elemento do meio.</p>
<p>No código, o programa lê o tamanho da lista <code>n</code> e a própria lista de números <code>data</code> do usuário. Em seguida, chama a função <code>quartiles</code> para calcular os três quartis e escreve-os em um arquivo de saída.</p>
<p>Esse código pode ser útil para quem precisa calcular quartis em uma lista de dados.</p>
<h2>Quartil</h2>
<p>Quartil é uma medida estatística que divide um conjunto de dados ordenados em quatro partes iguais. Os quartis são representados pelas letras Q1, Q2 e Q3 e correspondem aos valores que dividem os dados em quartos, ou seja, 25% dos dados estão abaixo de Q1, 50% estão abaixo de Q2 (mediana) e 75% estão abaixo de Q3. O cálculo dos quartis é útil para analisar a dispersão dos dados e identificar possíveis valores atípicos ou outliers.</p>
<h2>Outlier</h2>
<p>Outlier é um termo estatístico que se refere a um valor que está significativamente fora do padrão de um conjunto de dados. Esses valores são considerados "fora da curva" em relação à maioria dos outros dados e podem ser influenciados por erros de medição, anomalias naturais ou erros de entrada. Em muitos casos, os outliers podem distorcer a análise estatística de um conjunto de dados, prejudicando a precisão das estimativas e conclusões. Portanto, é comum excluí-los ou tratá-los de maneira especial ao realizar análises estatísticas.</p>

<h1>Guia de Uso do Código</h1>
<p>Este código tem como objetivo calcular os três quartis (Q1, Q2 e Q3) de um conjunto de dados.</p>
<h2>Como usar</h2>
<ol>
    <li>Baixe o código ou crie um novo arquivo com a extensão ".py".</li>
    <li>Abra o arquivo em um editor de texto.</li>
    <li>Copie o código e cole no arquivo.</li>
    <li>Salve o arquivo.</li>
    <li>Execute o código em um terminal ou prompt de comando.</li>
</ol>
<h2>Entrada</h2>
<p>O código recebe como entrada um conjunto de dados (array) contendo números inteiros. O número de elementos do array deve ser informado na primeira linha da entrada, seguido dos elementos do array na segunda linha, separados por espaço.</p>
<h2>Saída</h2>
<p>O código retorna um array contendo os três quartis (Q1, Q2 e Q3) do conjunto de dados.</p>
<h2>Exemplo</h2>
<p>Suponha que você tenha um conjunto de dados com os seguintes valores: [3, 7, 8, 5, 12, 14, 21, 15, 18, 14]. Para calcular os quartis desse conjunto de dados, siga os seguintes passos:</p>
<ol>
    <li>Crie um novo arquivo com a extensão ".py" e cole o código.</li>
    <li>Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo foi salvo.</li>
    <li>Digite o seguinte comando para executar o código: <code>python3 nome_do_arquivo.py</code></li>
    <li>Na primeira linha da entrada, digite o número de elementos do array (10).</li>
    <li>Na segunda linha da entrada, digite os elementos do array separados por espaço (3 7 8 5 12 14 21 15 18 14).</li>
    <li>O resultado será um array contendo os três quartis do conjunto de dados: [6, 13, 16].</li>
</ol>
