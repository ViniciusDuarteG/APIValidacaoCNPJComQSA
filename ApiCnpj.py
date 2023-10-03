#-*- coding: utf-8 -*-
import requests
import json

def consulta_cnpj(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request("GET", url, params=querystring)
    
    resp = json.loads(response.text)
    
    razao_social = resp['nome']
    tipo = resp['tipo']
    situacao = resp['situacao']
    nat_jud = resp['natureza_juridica']
    municipio = resp['municipio']
    estado = resp['uf']
    qsa = resp['qsa']
    

    if nat_jud == '201-1' or '203-8' or '204-6' or '205-4' or '206-2' or '207-0' or '208-9' or '209-7' or '212-7' or '213-5' or '214-3' or '215-1' or '216-0' or '223-2' or '224-0' or '225-9' or '226-7' or '229-1' or '230-5' or '231-3' or '306-9' or '330-1' or '399-9' or '409-0' or '412-0':
        print(f'RAZÃO SOCIAL: {razao_social}\nTIPO: {tipo}\nSITUAÇÃO: {situacao}\nNATUREZA JURIDICA: {nat_jud}\nMUNICIPIO: {municipio}\nESTADO: {estado}\nQSA: {qsa}')
        
    else: 
        print("Esse CNPJ não está disponível para emitir a certidão de validação da RFB.")
    

num_cnpj = int(input("Insira o CNPJ (somente números): \n"))
consulta_cnpj(num_cnpj)