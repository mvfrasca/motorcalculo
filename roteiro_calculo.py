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
    entrada['financeiro']['vlPremioNet']+=round(cobertura['vlPremioNet'],2)
    entrada['financeiro']['vlComissao']+=round(cobertura['vlComissao'],2)
    entrada['financeiro']['vlPremioLiquido']+=round(cobertura['vlPremioLiquido'],2)
    entrada['financeiro']['vlIof']+=round(cobertura['vlIof'],2)
    entrada['financeiro']['vlPremioTotal']+=round(cobertura['vlPremioTotal'],2)
