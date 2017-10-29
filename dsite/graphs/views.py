from django.shortcuts import render

def index(request):
	return render(request, 'graphs/index.html')

def novo_index(request):
	return render(request, 'graphs/index.html')