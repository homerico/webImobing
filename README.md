# WebImobing - Web Scraping de Imóveis

### Aluno: Eduardo de Moraes

### Objetivo

O objetivo deste projeto é realizar a raspagem de dados de imóveis em sites de anúncios de 
aluguel de imóveis na região de Florianópolis-SC, demonstrando habilidade o bastante para 
obter nota necessária para passsar na disciplina de Tópicos Especiais em Gerência de Dados 
(INE5454), ministrada pela profa. Carina Friedrich Dorneles. 

Os sites escolhidos foram [OLX](https://www.olx.com.br/), 
[Ibagy](https://ibagy.com.br/), 
[Giacomelli](https://www.giacomelli.com.br/) e 
[Crédito Real](https://www.creditoreal.com.br/).

### Estrutura do Projeto

Os dados obtidos dos sites de anúncios de imóveis são armazenados em arquivos JSON, na 
pasta "data". Na pasta "settings" se encontram os arquivos de configuração dos sites, 
basicamente é onde se deve preencher as informações para a filtragem dos imóveis, como o 
valor, tamanho e até quantidade de vagas. O código, por sua vez, fica em "src".

### Dependências

- make;
- Python 3.11 ou superior;
- pip;
- venv.

### Instalação

Para instalar as dependências do projeto, basta executar o comando abaixo:

```bash
make install
```
Obs.: Caso dê algum problema com a ativação do venv, é recomendado deletar a pasta do venv
e executar o comando novamente.

### Execução

Para executar o projeto, basta executar o comando abaixo:

```bash
make run
```

