pcComissao = entrada['pcComissao'] / 100
entrada['financeiro'] = {
    'vlPremioNet': 0.0,
    'vlComissao': 0.0,
    'vlPremioLiquido': 0.0,
    'vlIof': 0.0,
    'vlPremioTotal': 0.0
}
for cobertura in entrada['lsConjuntoCobertura']:
    cobertura['vlPremioNet'] = round(cobertura['vlImportanciaSegurada'] * (cobertura['pcTaxaNet'] / 100), 2)
    cobertura['vlPremioLiquido'] = round(cobertura['vlPremioNet'] / (1 - pcComissao),2)
    cobertura['vlComissao'] = round(cobertura['vlPremioLiquido'] * pcComissao)
    cobertura['vlIof'] = round(cobertura['vlPremioLiquido'] * (cobertura['pcIof'] / 100), 2)
    cobertura['vlPremioTotal'] = cobertura['vlPremioLiquido'] + cobertura['vlIof']
    entrada['financeiro']['vlPremioNet']+=cobertura['vlPremioNet']
    entrada['financeiro']['vlComissao']+=cobertura['vlComissao']
    entrada['financeiro']['vlPremioLiquido']+=cobertura['vlPremioLiquido']
    entrada['financeiro']['vlIof']+=cobertura['vlIof']
    entrada['financeiro']['vlPremioTotal']+=cobertura['vlPremioTotal']
