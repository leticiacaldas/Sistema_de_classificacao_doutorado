import os
import pandas as pd
import requests

class Aluno:
    """
    Esta classe representa um aluno com todas as informações necessárias para o processo de classificação.
    Inclui detalhes pessoais, acadêmicos e documentação.
    """
    def __init__(self, nome_completo, data_nascimento, email, nome_mae, cpf, identidade, data_emissao_identidade, orgao_emissor_identidade,
                 numero_titulo_eleitoral, numero_documento_militar, endereco_residencial, cidade_residencia, estado_residencia,
                 telefone_contato, link_lattes, reservas_vagas, siape, curso1_nome, curso1_tipo, curso1_instituicao, curso1_ano_conclusao,
                 curso2_nome, curso2_tipo, curso2_instituicao, curso2_ano_conclusao, local_trabalho, atuacao, ingles_leitura, ingles_escrita,
                 ingles_fala, tipo_inscricao, semestre_ingresso, orientador_preferencial, segunda_opcao, terceira_opcao,
                 dedicacao_integral, vinculo_empregaticio, interesse_bolsa, link_projeto_memorial, pub1_titulo, pub1_local,
                 pub1_tipo, pub1_qualis, pub1_comprovacao, pub2_titulo, pub2_local, pub2_tipo, pub2_qualis, pub2_comprovacao,
                 pub3_titulo, pub3_local, pub3_tipo, pub3_qualis, pub3_comprovacao, pub4_titulo, pub4_local, pub4_tipo, pub4_qualis,
                 pub4_comprovacao, pub5_titulo, pub5_local, pub5_tipo, pub5_qualis, pub5_comprovacao, link_curriculo_lattes,
                 diploma_graduacao, diploma_mestrado, historico_graduacao, historico_mestrado, identidade_doc, cpf_doc, titulo_eleitor_doc,
                 certificado_militar, certidao_casamento, comprovante_pagamento, documentacao_secao_6, outro_documento, id_usuario, timestamp, pontuacao_historico: float = None):
       
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.email = email
        self.nome_mae = nome_mae
        self.cpf = cpf
        self.identidade = identidade
        self.data_emissao_identidade = data_emissao_identidade
        self.orgao_emissor_identidade = orgao_emissor_identidade
        self.numero_titulo_eleitoral = numero_titulo_eleitoral
        self.numero_documento_militar = numero_documento_militar
        self.endereco_residencial = endereco_residencial
        self.cidade_residencia = cidade_residencia
        self.estado_residencia = estado_residencia
        self.telefone_contato = telefone_contato
        self.link_lattes = link_lattes
        self.reservas_vagas = reservas_vagas
        self.siape = siape
        self.curso1_nome = curso1_nome
        self.curso1_tipo = curso1_tipo
        self.curso1_instituicao = curso1_instituicao
        self.curso1_ano_conclusao = curso1_ano_conclusao
        self.curso2_nome = curso2_nome
        self.curso2_tipo = curso2_tipo
        self.curso2_instituicao = curso2_instituicao
        self.curso2_ano_conclusao = curso2_ano_conclusao
        self.local_trabalho = local_trabalho
        self.atuacao = atuacao
        self.ingles_leitura = ingles_leitura
        self.ingles_escrita = ingles_escrita
        self.ingles_fala = ingles_fala
        self.tipo_inscricao = tipo_inscricao
        self.semestre_ingresso = semestre_ingresso
        self.orientador_preferencial = orientador_preferencial
        self.segunda_opcao = segunda_opcao
        self.terceira_opcao = terceira_opcao
        self.dedicacao_integral = dedicacao_integral
        self.vinculo_empregaticio = vinculo_empregaticio
        self.interesse_bolsa = interesse_bolsa
        self.link_projeto_memorial = link_projeto_memorial
        self.pub1_titulo = pub1_titulo
        self.pub1_local = pub1_local
        self.pub1_tipo = pub1_tipo
        self.pub1_qualis = pub1_qualis
        self.pub1_comprovacao = pub1_comprovacao
        self.pub2_titulo = pub2_titulo
        self.pub2_local = pub2_local
        self.pub2_tipo = pub2_tipo
        self.pub2_qualis = pub2_qualis
        self.pub2_comprovacao = pub2_comprovacao
        self.pub3_titulo = pub3_titulo
        self.pub3_local = pub3_local
        self.pub3_tipo = pub3_tipo
        self.pub3_qualis = pub3_qualis
        self.pub3_comprovacao = pub3_comprovacao
        self.pub4_titulo = pub4_titulo
        self.pub4_local = pub4_local
        self.pub4_tipo = pub4_tipo
        self.pub4_qualis = pub4_qualis
        self.pub4_comprovacao = pub4_comprovacao
        self.pub5_titulo = pub5_titulo
        self.pub5_local = pub5_local
        self.pub5_tipo = pub5_tipo
        self.pub5_qualis = pub5_qualis
        self.pub5_comprovacao = pub5_comprovacao
        self.link_curriculo_lattes = link_curriculo_lattes
        self.diploma_graduacao = diploma_graduacao
        self.diploma_mestrado = diploma_mestrado
        self.historico_graduacao = historico_graduacao
        self.historico_mestrado = historico_mestrado
        self.identidade_doc = identidade_doc
        self.cpf_doc = cpf_doc
        self.titulo_eleitor_doc = titulo_eleitor_doc
        self.certificado_militar = certificado_militar
        self.certidao_casamento = certidao_casamento
        self.comprovante_pagamento = comprovante_pagamento
        self.documentacao_secao_6 = documentacao_secao_6
        self.outro_documento = outro_documento
        self.id_usuario = id_usuario
        self.timestamp = timestamp
        
        # Novos atributos para média e pontuação do histórico e publicações
        self.media_historico = None
        self.pontuacao_historico = pontuacao_historico
        self.pontuacao_publicacoes = [None, None, None]
        self.pontuacao_final_publicacoes = None
        self.nota_final = None
    

def baixar_arquivo(url, destino_download, name_arquivo):
  """
    Baixa um arquivo da internet e o salva em um diretório local.

    Parâmetros:
    url (str): A URL do arquivo a ser baixado.
    pasta_destino (str): O caminho do diretório onde o arquivo será salvo.
    nome_arquivo (str): O nome sob o qual o arquivo será salvo.

    Retorna:
    None
    """
    # Faz a requisição ao servidor com um timeout
  try:
        resposta_http = requests.get(url, timeout=10)
        # Verifica se a requisição foi bem-sucedida (código 200)
        if resposta_http.status_code == 200:
            # Cria o caminho completo onde o arquivo será salvo
            caminho_arquivo = f"{destino_download}/{name_arquivo}/{dest}"
            # Abre o arquivo para escrita no caminho especificado e escreve o conteúdo
            with open(caminho_arquivo, "wb") as arquivo_destino:
                arquivo_destino.write(resposta_http.content)
            print(f"Arquivo {name_arquivo} baixado com sucesso!")
        else:
            print("Falha no download do arquivo. Código de resposta:", resposta_http.status_code)
  except requests.exceptions.Timeout:
        print("O download do arquivo excedeu o tempo limite.")
  except requests.exceptions.RequestException as e:
        print("Erro ao baixar o arquivo: {e}")
    # ... (definição da função baixar_arquivo permanece a mesma)

def calcular_pontuacao_historico(media_historico):
    if media_historico <= 5.0:
        return 0.0
    else:
        return media_historico - 5.0

def calcular_pontuacao_publicacao(quantidade_publicacoes):
    if quantidade_publicacoes <= 0:
        return 0.0
    elif quantidade_publicacoes <= 2:
        return 1.0
    elif quantidade_publicacoes <= 4:
        return 2.0
    elif quantidade_publicacoes <= 6:
        return 3.0
    elif quantidade_publicacoes <= 8:
        return 4.0
    else:
        return 5.0
      
    
quantidade_publicacoes = 5  # Exemplo de quantidade de publicações científicas
nota_publicacoes = calcular_pontuacao_publicacao(quantidade_publicacoes)
print(f"A nota para publicações científicas é: {nota_publicacoes}")


def main():
    input_csv_path = 'C:/Users/letic/Desktop/Programação por pares com Inteligência Artificial/Projeto Sistema de Classificacao/inscricoes.csv'
    media_historico_path = 'C:/Users/letic/Desktop/Programação por pares com Inteligência Artificial/Projeto Sistema de Classificacao/media_historico.csv'

    df = pd.read_csv(input_csv_path)
    df_media_historico = pd.read_csv(media_historico_path)

    alunos = []

    for index, row in df.iterrows():
        if row['Tipo de inscrição'].strip().lower() == 'doutorado':
            aluno = Aluno(
                nome_completo=row['Nome Completo'],
                data_nascimento=row['Data de nascimento'],
                email=row['Seu e-mail'],
                nome_mae=row['Nome da mãe'],
                cpf=row['CPF'],
                identidade=row['Carteira de Identidade, no caso de candidatas/os de nacionalidade brasileira, ou passaporte, no caso de candidatas/os de nacionalidade estrangeira'],
                data_emissao_identidade=row['Data de emissão da carteira de identidade'],
                orgao_emissor_identidade=row['Órgão emissor da carteira de identidade e estado emissor'],
                numero_titulo_eleitoral=row['Número do título eleitoral'],
                numero_documento_militar=row['Número de série do documento militar'],
                endereco_residencial=row['Endereço residencial'],
                cidade_residencia=row['Cidade de residência'],
                estado_residencia=row['Estado de residência'],
                telefone_contato=row['Telefone para contato'],
                link_lattes=row['Link para o currículo Lattes'],
                reservas_vagas=row['Reservas de vagas'],
                siape=row['Informe o número do seu SIAPE ligado a UFPel para confirmar a candidatura às quotas de vagas para servidores da Universidade'],
                curso1_nome=row['Nome do Curso'],
                curso1_tipo=row['Tipo de curso'],
                curso1_instituicao=row['Instituição'],
                curso1_ano_conclusao=row['Ano de conclusão'],
                curso2_nome=row['Nome do curso'],
                curso2_tipo=row['Tipo de curso'],
                curso2_instituicao=row['Instituição'],
                curso2_ano_conclusao=row['Ano de conclusão'],
                local_trabalho=row['Local de trabalho'],
                atuacao=row['Atuação'],
                ingles_leitura=row['Língua Inglesa (Leitura)'],
                ingles_escrita=row['Língua Inglesa (Escrita)'],
                ingles_fala=row['Língua Inglesa (Fala)'],
                tipo_inscricao=row['Tipo de inscrição'],
                semestre_ingresso=row['Em que semestre faria o ingresso?'],
                orientador_preferencial=row['Orientador preferencial'],
                segunda_opcao=row['Segunda opção'],
                terceira_opcao=row['Terceira opção'],
                dedicacao_integral=row['Você teria dedicação integral para o curso?'],
                vinculo_empregaticio=row['Você manteria vínculo empregatício durante a execução do curso?'],
                interesse_bolsa=row['Você tem interesse em concorrer a uma bolsa do programa?'],
                link_projeto_memorial=row['"Enviar arquivo PDF contendo o Projeto de Doutorado e Memorial Acadêmico, conforme especificado no edital."'],
                pub1_titulo=row['Título da publicação'],
                pub1_local=row['Local de publicação'],
                pub1_tipo=row['Tipo da publicação'],
                pub1_qualis=row['Qualis do local de publicação'],
                pub1_comprovacao=row['Comprovação de publicação ou aceite de publicação (PDF)'],
                pub2_titulo=row['Título da publicação'],
                pub2_local=row['Local de publicação'],
                pub2_tipo=row['Tipo da publicação'],
                pub2_qualis=row['Qualis do local de publicação'],
                pub2_comprovacao=row['Comprovação de publicação ou aceite de publicação (PDF)'],
                pub3_titulo=row['Título da publicação'],
                pub3_local=row['Local de publicação'],
                pub3_tipo=row['Tipo da publicação'],
                pub3_qualis=row['Qualis do local de publicação'],
                pub3_comprovacao=row['Comprovação de publicação ou aceite de publicação (PDF)'],
                pub4_titulo=row['Título da publicação'],
                pub4_local=row['Local de publicação'],
                pub4_tipo=row['Tipo da publicação'],
                pub4_qualis=row['Qualis do local de publicação'],
                pub4_comprovacao=row['Comprovação de publicação ou aceite de publicação (PDF)'],
                pub5_titulo=row['Título da publicação'],
                pub5_local=row['Local de publicação'],
                pub5_tipo=row['Tipo da publicação'],
                pub5_qualis=row['Qualis do local de publicação'],
                pub5_comprovacao=row['Comprovação de publicação ou aceite de publicação (PDF)'],
                link_curriculo_lattes=row['Currículo Lattes'],
                diploma_graduacao=row['Diploma de graduação OU atestado de conclusão de curso OU atestado de provável formando OU atestado de provável formando indicando que irá concluir o curso até 30 de julho de 2023 no caso de ingresso em 2023/2'],
                diploma_mestrado=row['Se aplicável, cópia do diploma de mestrado OU comprovação de cumprimento de todos requisitos para obtenção do diploma OU atestado indicando que irá concluir o seu curso de mestrado até 30 de julho de 2023 no caso de ingresso em 2023/2'],
                historico_graduacao=row['Histórico escolar de Graduação'],
                historico_mestrado=row['Histórico escolar de Mestrado'],
                identidade_doc=row['Carteira de Identidade'],
                cpf_doc=row['"CPF, se não disponível na carteira de identidade;"'],
                titulo_eleitor_doc=row['Título de eleitor'],
                certificado_militar=row['Certificado de quitação com serviço militar, ou equivalente, se aplicável'],
                certidao_casamento=row['Certidão de Casamento, no caso de mudança do nome'],
                comprovante_pagamento=row['Comprovante de pagamento ou comprovante de isenção da taxa de inscrição'],
                documentacao_secao_6=row['Documentação relativa a seção 6(l), 6(m), 6(n), 6(o), 6(p) ou 6(q), se aplicável'],
                outro_documento=row['Outro documento se necessário de acordo com o Edital'],
                id_usuario=row['ID do Usuário'],
                timestamp=row['Timestamp']
            )

            alunos.append(aluno)

    # Calcular a pontuação do histórico escolar
    for aluno in alunos:
        media_historico = df_media_historico.loc[df_media_historico['CPF'] == aluno.cpf, 'Media_Historico'].iloc[0]
        aluno.media_historico = media_historico
        aluno.pontuacao_historico = calcular_pontuacao_historico(media_historico)

    # Calcular a pontuação das publicações
    for aluno in alunos:
        aluno.pontuacao_publicacoes[0] = calcular_pontuacao_publicacao(aluno.pub1_comprovacao)
        aluno.pontuacao_publicacoes[1] = calcular_pontuacao_publicacao(aluno.pub2_comprovacao)
        aluno.pontuacao_publicacoes[2] = calcular_pontuacao_publicacao(aluno.pub3_comprovacao)
        aluno.pontuacao_final_publicacoes = sum(aluno.pontuacao_publicacoes) / 3

    # Calcular a nota final e gerar o arquivo CSV
    dados_resultados = []

    for aluno in alunos:
        aluno.nota_final = (aluno.pontuacao_historico + aluno.pontuacao_final_publicacoes) / 2
        dados_resultados.append({
            'Nome Completo': aluno.nome_completo,
            'CPF': aluno.cpf,
            'Média Histórico': aluno.media_historico,
            'Pontuação Histórico': aluno.pontuacao_historico,
            'Pontuação Publicação 1': aluno.pontuacao_publicacoes[0],
            'Pontuação Publicação 2': aluno.pontuacao_publicacoes[1],
            'Pontuação Publicação 3': aluno.pontuacao_publicacoes[2],
            'Pontuação Final Publicações': aluno.pontuacao_final_publicacoes,
            'Nota Final': aluno.nota_final
        })

    df_resultados = pd.DataFrame(dados_resultados)
    df_resultados.to_csv('resultados_doutorado.csv', index=False)

if __name__ == '__main__':
    main()
