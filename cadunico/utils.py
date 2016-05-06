def importa(request):
    import csv
    f = csv.reader(open('/Users/paulo/Desktop/base-familias-rendas.csv', 'rU'), dialect='excel',delimiter=';')

    for row in f:
        mun = MunicipioBeneficiado.objects.get(municipio__municipio__iexact=row[0])
        print mun.municipio

        mun.pessoas_renda_77 = row[5]
        mun.pessoas_renda_154 = row[6]
        mun.pessoas_renda_394 = row[7]
        mun.pessoas_renda_acima = row[8]
        mun.familias_renda_77 = row[1]
        mun.familias_renda_154 = row[2]
        mun.familias_renda_394 = row[3]
        mun.familias_renda_acima = row[4]
        mun.renda_d = '2015-04-01'

        mun.save()


        
        """print row[0]
        mun = Municipio.objects.get(municipio__iexact=row[0])
        m = MunicipioBeneficiado()

        m.municipio = mun
        m.populacao = float(row[1])
        m.populacao_d = row[2]
        m.pessoas_cadunico = float(row[3])
        m.pessoas_cadunico_d = row[4]
        m.familias_cadunico = float(row[5])
        m.familias_cadunico_d = row[6]
        m.familias_cadunico_atendidas = float(row[7])
        m.valor_pago = float(row[8])
        m.valor_pago_d = row[9]
        m.agricultura_familiar = float(row[10])
        m.agricultura_familiar_atendidas = float(row[11])
        m.agricultura_familiar_d = row[12]
        m.idh = float(row[13])
        m.idh_d = row[14]
        if(row[15] != ''):
            m.pib_percapita = float(row[15])
        else:
            m.pib_percapita = 0
        m.pib_percapita_d = row[16]
        
        m.save()""" 