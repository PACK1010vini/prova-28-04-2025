def indicar_melhores_filmes(nome_arquivo_avaliacoes="filmes_Avaliacao.txt", nome_arquivo_indicacoes="filmes_indicacao.txt"):


    avaliacoes = {}
    try:
        with open(nome_arquivo_avaliacoes, 'r') as arquivo_avaliacoes:
            for linha in arquivo_avaliacoes:
                linha = linha.strip()
                if linha:
                    try:
                        filme, nota = linha.split(': ')
                        avaliacoes[filme] = float(nota)
                    except ValueError:
                        print(f"Aviso: Linha inválida encontrada e ignorada: '{linha}'")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_avaliacoes}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo de avaliações: {e}")
        return


    filmes_ordenados = sorted(avaliacoes.items(), key=lambda item: item[1], reverse=True)
    melhores_filmes = [filme for filme, _ in filmes_ordenados[:5]]


    try:
        with open(nome_arquivo_indicacoes, 'w') as arquivo_indicacoes:
            for filme in melhores_filmes:
                arquivo_indicacoes.write(f"{filme}\n")
        print(f"\nOs 5 filmes mais bem avaliados foram salvos em '{nome_arquivo_indicacoes}'")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os filmes indicados: {e}")



indicar_melhores_filmes()