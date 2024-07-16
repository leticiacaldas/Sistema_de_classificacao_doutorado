**Classificação Automática de Alunos Inscritos no Doutorado**
Descrição:

Este projeto tem como objetivo desenvolver um programa para a classificação automática de alunos inscritos em programas de mestrado e doutorado de pós-graduação, de acordo com o histórico escolar e publicações científicas dos candidatos. Os critérios de classificação seguem o Edital de Seleção do PPGC da UFPEL.
Objetivo da Aula 6

Na aula de hoje, focaremos na classificação dos alunos inscritos no DOUTORADO. Utilizaremos os critérios de classificação especificados no edital do PPGC da UFPEL.
Atividades

    Selecionar os alunos de doutorado:
        Filtrar os alunos cujo campo "Tipo de Inscrição" seja "Doutorado" (ignorando maiúsculas e minúsculas).

    Calcular a pontuação do histórico escolar:
        Calcular a pontuação de acordo com os itens 27.b e 27.c do edital. Obter a média do histórico de outra planilha que contém o nome, CPF e média do histórico.

    Calcular a pontuação das publicações:
        Atualizar a pontuação das publicações e calcular a pontuação final.

    Adaptação da classe Aluno:
        Modificar a classe Aluno para incluir atributos como média do histórico, pontuação de cada publicação e pontuação geral das publicações.

    Calcular a nota final:
        Calcular a nota final de cada aluno e mostrar a lista classificada dos alunos com todas as publicações parciais e finais. Gerar um arquivo CSV com os resultados.

Requisitos

    O programa deve ser escrito em Python.
    Utilizar bibliotecas padrão de Python para leitura de arquivos CSV e download de arquivos.
    Documentar o código com comentários explicativos.

Organização e Modularização do Código

    Modularização: Organizar o código de forma modular para que ele possa ser facilmente estendido. Dividir as funcionalidades em funções e classes conforme necessário.
    Controle de Versão: Utilizar controle de versões para manter um registro das mudanças realizadas e versões anteriores do código.
    Interação com o GitHub Copilot: Interagir com o Copilot Chat para sugestões de organização do programa. Projetar o programa antes de começar a programar.
    Compreensão do Código: Revisar e corrigir o código gerado pelo Copilot, garantindo modularidade, limpeza e boa documentação.



├── data/

│   ├── inscricoes.csv  # Planilha fictícia de alunos inscritos

│   └── inscricoes.csv   # Planilha com média do histórico escolar


├── results/

│   └── projeto_sistema_de_classificacao.csv  # Arquivo CSV com os resultados finais

└── README.md                 # Este arquivo


Classe Aluno

A classe Aluno foi adaptada para incluir os seguintes atributos:

    Média do histórico escolar
    Pontuação de cada publicação
    Pontuação geral das publicações

Como Executar

    Certifique-se de ter o Python instalado em sua máquina.
    Instale as bibliotecas necessárias (se houver):

    pip install pandas

Considerações Finais

Este projeto é uma aplicação prática de conceitos de programação em Python, leitura e manipulação de arquivos CSV, e aplicação de critérios específicos para classificação de candidatos.
A interação com ferramentas de IA, como o GitHub Copilot, é utilizada para auxiliar no desenvolvimento, mas é essencial a revisão crítica do código gerado para garantir sua funcionalidade e qualidade.
