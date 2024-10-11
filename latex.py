from jinja2 import Template

# Função para obter entrada do usuário
def input_text(prompt):
    return input(prompt + ": ").strip()

# Função para coletar subseções e possíveis imagens
def input_subsections_with_images(prompt):
    subsections = []
    while True:
        title = input_text(prompt + " - Digite o título da subseção (ou 'fim' para terminar):")
        if title.lower() == 'fim':
            break
        text = input_text(f"Digite o texto da subseção '{title}':")
        
        # Verificar se o usuário quer inserir uma imagem
        add_image = input_text("Deseja adicionar uma imagem nesta subseção? (sim/não)").lower()
        if add_image == 'sim':
            image_path = input_text("Digite o caminho da imagem:")
            author_name = input_text("Digite o nome do autor da imagem:")
            subsections.append({
                'title': title, 
                'text': text,
                'image': True,
                'image_path': image_path,
                'author_name': author_name
            })
        else:
            subsections.append({
                'title': title, 
                'text': text,
                'image': False
            })
    return subsections

# Solicita informações ao usuário
context = {
    'titulo_trabalho': input_text('Digite o título do trabalho'),
    'nome_autor': input_text('Digite o nome do autor'),
    'mes': input_text('Digite o mês'),
    'ano': input_text('Digite o ano'),
    'secao_introducao': input_text('Digite o título da seção de Introdução'),
    'subsecao_intro': input_subsections_with_images('Digite informações para a subseção da Introdução'),
    'secao_desenvolvimento': input_text('Digite o título da seção de Desenvolvimento'),
    'subsecao_des': input_subsections_with_images('Digite informações para a subseção do Desenvolvimento'),
    'secao_conclusao': input_text('Digite o título da seção de Conclusão'),
    'texto_conclusao': input_text('Digite o texto da seção de Conclusão')
}

# Leia o template com codificação UTF-8
with open('template.tex', 'r', encoding='utf-8') as file:
    template_content = file.read()

# Crie um template Jinja2 e gere o conteúdo LaTeX
template = Template(template_content)
latex_content = template.render(context)

# Escreva o conteúdo gerado em um arquivo .tex
with open('output.tex', 'w', encoding='utf-8') as file:
    file.write(latex_content)

print("Arquivo LaTeX gerado com sucesso!")
