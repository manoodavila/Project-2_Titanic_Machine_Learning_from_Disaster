# Titanic Survival Analysis

Este projeto realiza uma análise dos dados dos sobreviventes do Titanic para tentar responder à pergunta: "Quem é mais provável sobreviver?"

## Descrição

O código analisa os dados dos passageiros do Titanic e utiliza um modelo de machine learning para prever a sobrevivência. O modelo RandomForestClassifier é utilizado para prever a sobrevivência dos passageiros no conjunto de teste.

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
