from django.shortcuts import render
import json # importa os modulo json para trabalhar com dados em formato json
from django.http import JsonResponse # A classe JasonResponse retorna os dados em formato Json

# Lista incial de pridutos
lista_produtos = ['pao', 'queijo', 'coca cola']

# Exemplo de GET - Busca dado(s)
def buscar_produtos_get(request):
    print('Teste')
    # Esta view retorna a lista de produtos em formato json
    if request.method == 'GET': # Verifica se o metodo da requisição é GET
        return JsonResponse({'produtos' : lista_produtos}) # Retorna a lista de produtos com JSON - par chave:valor
    
    else: # Se não for GET retorna um erro 405 (Método não permitido)
        return JsonResponse({'erro': 'Metodo não Permitido'})

# Exemplo de PUT - Altera um dado(s)
def altera_produtos_put(request):
    print('Teste')
    if request == 'PUT':
        try:
            body = json.loads(request.body) # Lê o corpo da requisição JSON
            nome_antigo = body.get('pao')
            nome_novo = body.get('pao doce')
            if nome_antigo in lista_produtos:
                index = lista_produtos.index(nome_antigo)
                lista_produtos[index] = nome_novo
                return JsonResponse({'mensagem' : 'Produto atualizado', 'produtos' : lista_produtos})
            else:
                return JsonResponse({'erro' : 'Produto não encontrado'})
        except json.JSONDecodeError:
            return JsonResponse({'erro' : 'JSON Invalido'}, status = 400)
    else:
        return JsonResponse({'erro' : 'Metodo não permitido'}, status=405)

# Exemplo de Post - Inclui um dado(s)
def cadastra_produto_post(request):
    if request == 'POST':
        try:
            body = json.loads(request.body) # Lendo o corpo do json
            novo_produto = body('açucar')
            if novo_produto not in lista_produtos:
                lista_produtos.append(novo_produto)
                return JsonResponse({'mensagem': 'Produto adcionado', 'produtos': lista_produtos})
            else:
                return JsonResponse({'erro': 'Produto já existe na lista'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'erro' : 'JOSN Invalido'})
    else:
        return JsonResponse({'erro' : 'Metodo não permitido'}, status=405)
            

# Create your views here.
