# Titanic Survival Analysis

Este projeto realiza uma análise dos dados dos sobreviventes do Titanic para tentar responder à pergunta: "Quem é mais provável sobreviver?". Escrevi o código paticipando da competição "Titanic - Machine Learning from Disaster" no Kaggle

## Descrição

Este projeto realiza uma análise detalhada dos dados dos passageiros do Titanic para prever a probabilidade de sobrevivência de novos passageiros com base em características específicas. O código é dividido em várias etapas principais, que são descritas a seguir:

1. **Importação das Bibliotecas Necessárias:**
   - O código começa importando bibliotecas essenciais para análise e modelagem de dados. A biblioteca NumPy é usada para operações matemáticas e manipulação de arrays, enquanto a pandas é utilizada para leitura e processamento dos dados. A biblioteca scikit-learn fornece ferramentas para construir e treinar o modelo preditivo, especificamente o classificador RandomForest.

2. **Carregamento dos Dados:**
   - Os dados são carregados a partir de arquivos CSV, um contendo informações sobre os passageiros que sobreviveram e outro com dados sobre os passageiros do conjunto de teste. Esses dados incluem várias características dos passageiros, como classe, sexo, número de irmãos/cônjuges a bordo, e número de pais/filhos a bordo.

3. **Análise Exploratória dos Dados:**
   - O código realiza uma análise básica para determinar a taxa de sobrevivência entre mulheres e homens. Essa análise ajuda a entender as diferenças nas taxas de sobrevivência entre os dois grupos e fornece uma visão inicial sobre os dados.

4. **Preparação dos Dados para Modelagem:**
   - Antes de treinar o modelo, os dados são preparados e transformados. A variável de resposta (se o passageiro sobreviveu ou não) é extraída do conjunto de treinamento. Em seguida, as características selecionadas para a modelagem, como a classe do passageiro, o sexo, e o número de familiares a bordo, são convertidas em variáveis numéricas usando a codificação one-hot. Isso é necessário porque os modelos de machine learning trabalham melhor com dados numéricos.

5. **Construção e Treinamento do Modelo:**
   - Um modelo de RandomForest é criado e treinado com os dados preparados. O RandomForest é um tipo de ensemble learning que utiliza múltiplas árvores de decisão para melhorar a precisão das previsões. O modelo é ajustado com base nas características dos passageiros e na variável de resposta.

6. **Previsão e Geração do Arquivo de Submissão:**
   - Após o treinamento do modelo, ele é utilizado para prever a sobrevivência dos passageiros no conjunto de teste. As previsões são então combinadas com os IDs dos passageiros e salvas em um arquivo CSV, que pode ser submetido para avaliação ou usado para análise adicional.

Essas etapas juntas permitem que o projeto forneça uma análise compreensiva dos dados dos passageiros do Titanic e gere previsões úteis sobre a sobrevivência de novos passageiros.

## Arquivos

- `titanic_analysis.py`: Script principal que realiza a análise e prevê a sobrevivência.
- `submission.csv`: Arquivo de submissão com as previsões para o conjunto de teste.
- `train.csv`: Dados de treinamento (deve ser baixado do Kaggle e colocado na pasta `data/`).
- `test.csv`: Dados de teste (deve ser baixado do Kaggle e colocado na pasta `data/`).

## Instruções

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/titanic-survival-analysis.git
    cd titanic-survival-analysis
    ```

2. **Instale as dependências:**
    ```bash
    pip install numpy pandas scikit-learn
    ```

3. **Prepare os dados:**
   Baixe os arquivos `train.csv` e `test.csv` do [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data) e coloque-os na pasta `data/`.

4. **Execute o script:**
    ```bash
    python titanic_analysis.py
    ```

5. **Verifique a saída:**
   O arquivo `submission.csv` será gerado com as previsões para o conjunto de teste.

## Contribuições

Sinta-se à vontade para abrir issues e enviar pull requests com melhorias ou correções.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
2. LICENSE
Escolha uma licença apropriada para o seu projeto. Aqui está um exemplo de um arquivo LICENSE para a Licença MIT:

plaintext
Copiar código
MIT License

Copyright (c) [2024] [manoodavila]

Permissão é concedida, gratuitamente, a qualquer pessoa que obter uma cópia deste software e arquivos de documentação associados (o "Software"), para lidar com o Software sem restrição, incluindo, sem limitação, os direitos de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, sujeito às seguintes condições:

A acima nota de copyright e esta nota de permissão devem ser incluídas em todas as cópias ou partes substanciais do Software.

O Software é fornecido "no estado em que se encontra", sem garantia de qualquer tipo, expressa ou implícita, incluindo, mas não se limitando às garantias implícitas de comercialização, adequação a um propósito específico e não infração. Em nenhum caso os autores ou titulares de direitos autorais serão responsáveis por qualquer reivindicação, dano ou outra responsabilidade, seja em uma ação de contrato, ato ilícito ou de outra forma, decorrente de, fora ou em conexão com o Software ou o uso ou outras transações no Software.
3. .gitignore
Crie um arquivo .gitignore para evitar o versionamento de arquivos desnecessários. Exemplo:

plaintext
Copiar código
# Python
__pycache__/
*.pyc

# Jupyter Notebook
.ipynb_checkpoints/

# Data files
data/
submission.csv
