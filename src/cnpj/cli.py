import argparse
from cnpj.core import fetch_cnpj_data
import sys

def run_cli():
    parser = argparse.ArgumentParser(description="Fetch CNPJ info from minhareceita.org")
    parser.add_argument("cnpj", help="CNPJ number to look up")
    parser.add_argument("--raw", action="store_true", help="Output raw JSON instead of formatted text")
    args = parser.parse_args()

    try:
        data = fetch_cnpj_data(args.cnpj)
        if args.raw:
            print(data)
        else:
            print(f"Razão Social: {data.get('razao_social')}")
            print(f"Nome Fantasia: {data.get('nome_fantasia')}")
            print(f"Situação Cadastral: {data.get('descricao_situacao_cadastral')}")
            print(f"Data de Abertura: {data.get('data_inicio_atividade')}")
            print(f"Natureza Jurídica: {data.get('natureza_juridica')}")
            print(f"Capital Social: R$ {data.get('capital_social')}")
    except Exception as e:
        print(f"Erro ao consultar {args.cnpj}: {e}")
        sys.exit(1)
