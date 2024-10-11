# Gerador de Template para Relatórios em LaTeX (Beta)

Este projeto é um gerador simples de relatórios em LaTeX que permite ao usuário inserir seu próprio conteúdo e gera automaticamente um arquivo `.tex`. A ferramenta utiliza o motor de templates **Jinja2** para preencher um modelo LaTeX com os dados fornecidos pelo usuário.

## Funcionalidades

- Coleta dados do usuário para seções como Introdução, Desenvolvimento e Conclusão.
- Permite a criação de subseções, com a opção de incluir imagens e créditos.
- Gera um arquivo LaTeX completo (`output.tex`) com base nos dados inseridos.
- Interface simples via linha de comando (CLI).

## Como Funciona

1. O script solicita ao usuário que insira detalhes-chave (ex.: título, autor, seções).
2. O usuário pode fornecer várias subseções e, opcionalmente, incluir imagens.
3. O script gera um arquivo LaTeX (`output.tex`) com base nos dados fornecidos.
4. O arquivo gerado pode ser compilado com um editor LaTeX para gerar o relatório final em PDF.

## Como Usar

1. Clone o repositório:
    ```bash
    git clone <url-do-repositorio>
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd Template-Generator-for_LaTeX
    ```

3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o script:
    ```bash
    python latex.py
    ```

5. Siga as instruções no terminal para inserir seus dados e gerar o arquivo LaTeX.

6. Abra o arquivo gerado `output.tex` em um editor LaTeX para compilar o relatório final.

## Requisitos

- Python 3.6+
- Ambiente LaTeX (para compilar o arquivo gerado)
- Biblioteca `Jinja2` para renderização de templates

## Instalação

Para instalar as bibliotecas Python necessárias, execute:

```bash
pip install -r requirements.txt
