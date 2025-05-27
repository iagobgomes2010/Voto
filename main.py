import requests
import time

form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeWXyIqcleTTfZj01oO_ZqdZ92AD96ldbAULxDRMjzawcxwyw/formResponse'

data = {
    'entry.1421571259': 'Equipe mãos limpas, cuidado seguro (Setor: auditoria)'
}

while True:
    response = requests.post(form_url, data=data)
    if response.status_code == 200:
        print('Resposta enviada com sucesso!')
    else:
        print(f'Erro ao enviar: {response.status_code}')
    time.sleep(1)
