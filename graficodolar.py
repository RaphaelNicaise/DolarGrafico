import requests
import csv

headers = {
    'Authorization': 'BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDIwMDAzNDIsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJyYXBoYW5pY2Fpc2VAZ21haWwuY29tIn0.LUbh29u8bhczmrSs-unifDSdTEbvlkFCdoC0g9l8_eSTIofvlIDFjqU5AXx_rX-EzqYW31-GEP7sLD2-Q2HIAg'
}

def usd_a_csv(nombre_archivo, url_api):
    
        response = requests.request("GET", url_api, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            with open(nombre_archivo, 'w', newline='',encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Fecha', 'Valor'])
                for dato in data:
                    datov = str(dato['v']).replace('.',',')
                    
                    csv_writer.writerow([dato['d'], datov])
                print('Archivo', nombre_archivo, 'creado y escrito con exito')
                
usd_a_csv('usd.csv', 'https://api.estadisticasbcra.com/usd')
usd_a_csv('usd_of.csv', 'https://api.estadisticasbcra.com/usd_of')

