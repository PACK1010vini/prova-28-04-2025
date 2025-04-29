def avaliar_filmes(nome_arquivo="filmes.txt", nome_arquivo_saida="filmes_Avaliacao.txt"):


    avaliacoes = {}
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:

                    titulo = linha.split(',', 1)[-1].strip()  # Pegando o título do filme
                    while True:
                        try:
                            nota = float(input(f"Avalie o filme: {titulo} (Digite uma nota de 0 a 10): "))
                            if 0 <= nota <= 10:
                                avaliacoes[titulo] = nota
                                break
                            else:
                                print("Por favor, digite uma nota entre 0 e 10.")
                        except ValueError:
                            print("Por favor, digite um número válido.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return


    try:
        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            for filme, nota in avaliacoes.items():
                arquivo_saida.write(f"{filme}: {nota}\n")
        print(f"\nAvaliações salvas em '{nome_arquivo_saida}'")
    except Exception as e:
        print(f"Erro ao salvar as avaliações: {e}")



avaliar_filmes()





