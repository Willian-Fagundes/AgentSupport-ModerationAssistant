from fpdf import FPDF

def txt_para_pdf(arquivo_entrada, arquivo_saida):
    # Inicializa o PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Define a fonte (Arial, tamanho 12)
    pdf.set_font("Arial", size=12)
    
    # Abre o arquivo de texto
    try:
        with open(arquivo_entrada, "r", encoding="utf-8") as f:
            for linha in f:
                # O método multi_cell é ideal pois quebra a linha automaticamente
                # se o texto for maior que a largura da página
                # 'latin-1' substitui caracteres estranhos por '?' ou similares
                pdf.multi_cell(0, 10, txt=linha.encode('latin-1', 'replace').decode('latin-1'), align='L')
        
        # Salva o arquivo final
        pdf.output(arquivo_saida)
        print(f"Sucesso! PDF salvo como: {arquivo_saida}")
        
    except FileNotFoundError:
        print("Erro: O arquivo de texto não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Uso
txt_para_pdf("artigo.txt", "politica.pdf")