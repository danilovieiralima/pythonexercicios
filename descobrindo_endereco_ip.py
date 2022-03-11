import socket as s


def descobrir_ip(texto) -> str:
    network = s
    endereco_ip_do_site = network.gethostbyname(texto)
    return endereco_ip_do_site


site = str(input('Nome do site: ')).strip()
print(f'O endereço IP do site {site} é {descobrir_ip(site)}')
