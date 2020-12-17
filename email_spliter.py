import sys
from time import sleep
import argparse
import os
import re


def read_emails_from_file(file_path: str) -> list:
    """
    Lê um arquivo de emails retornando uma lista com os mesmos.
    E-mails inválidos são retornados em uma segunda lista.
    """
    def check_valid_email(email: str) -> bool:
        if not re.match(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):
            return True
        else:
            return False

    emails_list = []
    invalid_emails = []

    with open(file_path, 'r') as emails:
        for email in emails:
            if email.strip() != '':
                if check_valid_email(email) -- True:
                    emails_list.append(email)
                else:
                    invalid_emails.append(email)
    return emails_list, invalid_emails


def print_file_out(out_path: str, file_name: str, text: str) -> None:
    """
    Escreve linhas em um arquivo específico.
    """
    #file = f'{out_path}+{file_name}'
    file = os.path.join(out_path, file_name)
    with open(file, 'a') as out:
            out.write(text)


def check_dir(dir_path: str) -> None:
    if os.path.isdir(dir_path) == True:
        pass
    else:
        print(f'Diretório informado inválido: {dir_path}.')
        sys.exit()


def check_file(file_path: str) -> None:
    if os.path.isfile(file_path) == True:
        pass
    else:
        print(f'Arquivo não encontrado: {file_path}.')
        sys.exit()


def main():
    """
    emails_file_path: Arquivo original contendo todos os e-mails.
    emails_path_out: Diretório de saída dos arquivos gerados.
    emails_per_file: Quantidade de e-mails por arquivo.
    """

    parser = argparse.ArgumentParser(description='E-mail Spliter.\nExemplo: email_spliter.exe --file_in C:\\Users\\guilh\\Documents\\dev\\email-spliter\\email_list_exemplo.txt --dir_out C:\\Users\\guilh\\Desktop\\out\\ --qty 10')
    parser.add_argument('--file_in', dest='file_in', type=str, help='Caminho do arquivo contendo a lista completa de e-mails.')
    parser.add_argument('--dir_out', dest='dir_out', type=str, help='Diretório de saída para os arquivos de e-mails splitados.')
    parser.add_argument('--qty', dest='qty', type=int, help='Quantidade de e-mails por arquivo. Exemplo: 50')
    
    args = parser.parse_args()
    emails_file_path = args.file_in
    emails_path_out = args.dir_out
    emails_per_file = args.qty

    check_file(emails_file_path)
    check_dir(emails_path_out)

    emails_list, invalid_emails_list = read_emails_from_file(emails_file_path)
    email_index = 0
    emails_file_list = []

    while email_index < len(emails_list):
        temp_emails_list = []

        for email in range(0, emails_per_file):
            temp_emails_list.append(emails_list[email_index])
            email_index += 1

        emails_file_list.append(temp_emails_list.copy())
        temp_emails_list.clear()

    print_lista = 1
    for email_list in emails_file_list:
        print(f'List number: {print_lista}\nLista: {email_list}\n')
        print_lista += 1

    arquivo = 1
    for email_list in emails_file_list:
        for email in email_list:
            file_name = f'emails_{arquivo}_{arquivo+emails_per_file-1}.txt'
            print_file_out(emails_path_out, file_name, email)
        arquivo += emails_per_file

    for invalid_string in invalid_emails_list:
        print_file_out(emails_path_out, 'emails_invalidos.txt', invalid_string)
        

if __name__ == '__main__':
    main() 