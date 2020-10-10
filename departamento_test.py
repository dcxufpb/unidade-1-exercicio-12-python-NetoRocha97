import pytest
import departamento

def verifica_campo_obrigatorio_objeto(mensagem_esperada, departamento):
    with pytest.raises(Exception) as excinfo:
        departamento.dados_departamento()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

NOME_DEPTO = "Departamento 1"
SIGLA = "Dep 1"
LOCALIZACAO = "Localização 1"
NOME_COORD = "Coordenador 1"
IDADE = 50
CPF = "123.456.789-01"

COORDENADOR_COMPLETO = departamento.Coordenador(NOME_COORD, IDADE, CPF)
DEPARTAMENTO_COMPLETO = departamento.Departamento(NOME_DEPTO, SIGLA, LOCALIZACAO, COORDENADOR_COMPLETO)

TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO = """Departamento 1, Dep 1
Local do depto: Localização 1
Coordenador 1
Idade do coord: 50
CPF do coord: 123.456.789-01"""

def teste_departamento_completo():
    assert (DEPARTAMENTO_COMPLETO.dados_departamento() == TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO)

SIGLA_NULA = departamento.Departamento(NOME_DEPTO, None, LOCALIZACAO, COORDENADOR_COMPLETO)
SIGLA_VAZIA = departamento.Departamento(NOME_DEPTO, "", LOCALIZACAO, COORDENADOR_COMPLETO)


TEXTO_ESPERADO_SEM_SIGLA = """Departamento 1
Local do depto: Localização 1
Coordenador 1
Idade do coord: 50
CPF do coord: 123.456.789-01"""

def test_valida_sigla():
    assert (SIGLA_NULA.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA)
    assert (SIGLA_VAZIA.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA)

COORD_IDADE_NULA = departamento.Coordenador(NOME_COORD, None, CPF)
COORD_IDADE_VAZIA = departamento.Coordenador(NOME_COORD, "", CPF)
IDADE_NULA = departamento.Departamento(NOME_DEPTO, SIGLA, LOCALIZACAO, COORD_IDADE_NULA)
IDADE_VAZIA = departamento.Departamento(NOME_DEPTO, SIGLA, LOCALIZACAO, COORD_IDADE_VAZIA)

TEXTO_ESPERADO_SEM_IDADE = """Departamento 1, Dep 1
Local do depto: Localização 1
Coordenador 1
CPF do coord: 123.456.789-01"""

def test_valida_idade():
    assert (IDADE_NULA.dados_departamento() == TEXTO_ESPERADO_SEM_IDADE)
    assert (IDADE_VAZIA.dados_departamento() == TEXTO_ESPERADO_SEM_IDADE)

SIGLA_IDADE_VAZIAS = departamento.Departamento(NOME_DEPTO, None, LOCALIZACAO, COORD_IDADE_VAZIA)

TEXTO_ESPERADO_SEM_SIGLA_SEM_IDADE = """Departamento 1
Local do depto: Localização 1
Coordenador 1
CPF do coord: 123.456.789-01"""

def test_valida_sigla_idade():
    assert (SIGLA_IDADE_VAZIAS.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA_SEM_IDADE)

NOME_DEPTO_NULO = departamento.Departamento(None, SIGLA, LOCALIZACAO, COORDENADOR_COMPLETO)
NOME_DEPTO_VAZIO = departamento.Departamento("", SIGLA, LOCALIZACAO, COORDENADOR_COMPLETO)

def test_valida_nome_depto():
    verifica_campo_obrigatorio_objeto(
        "O campo nome do departamento é obrigatório", NOME_DEPTO_NULO)
    verifica_campo_obrigatorio_objeto(
        "O campo nome do departamento é obrigatório", NOME_DEPTO_VAZIO)

LOCALIZACAO_NULA = departamento.Departamento(NOME_DEPTO, SIGLA, None, COORDENADOR_COMPLETO)
LOCALIZACAO_VAZIA = departamento.Departamento(NOME_DEPTO, SIGLA, "", COORDENADOR_COMPLETO)

def test_valida_localizacao():
    verifica_campo_obrigatorio_objeto(
        "O campo localização do departamento é obrigatório", LOCALIZACAO_NULA)
    verifica_campo_obrigatorio_objeto(
        "O campo localização do departamento é obrigatório", LOCALIZACAO_VAZIA)

COORD_NOME_VAZIO = departamento.Coordenador("", IDADE, CPF)
COORD_NOME_NULO = departamento.Coordenador(None, IDADE, CPF)
NOME_COORD_VAZIO = departamento.Departamento(NOME_DEPTO, SIGLA, LOCALIZACAO, COORD_NOME_VAZIO)
NOME_COORD_NULO = departamento.Departamento(NOME_DEPTO, SIGLA, LOCALIZACAO, COORD_NOME_NULO)

def test_valida_nome_coord():
    verifica_campo_obrigatorio_objeto(
        "O campo nome do coordenador do departamento é obrigatório", NOME_COORD_VAZIO)
    verifica_campo_obrigatorio_objeto(
        "O campo nome do coordenador do departamento é obrigatório", NOME_COORD_NULO)

COORD_CPF_VAZIO = departamento.Coordenador(NOME_COORD, IDADE, "")
COORD_CPF_NULO = departamento.Coordenador(NOME_COORD, IDADE, None)
CPF_COORD_VAZIO = departamento.Departamento(NOME_DEPTO, SIGLA, LOCALIZACAO, COORD_CPF_VAZIO)
CPF_COORD_NULO = departamento.Departamento(NOME_DEPTO, SIGLA, LOCALIZACAO, COORD_CPF_NULO)

def test_valida_cpf_coord():
    verifica_campo_obrigatorio_objeto(
        "O campo cpf do coordenador do departamento é obrigatório", CPF_COORD_VAZIO)
    verifica_campo_obrigatorio_objeto(
        "O campo cpf do coordenador do departamento é obrigatório", CPF_COORD_NULO)