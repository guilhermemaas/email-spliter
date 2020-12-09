# email-spliter

### Objetivo:
"Quebrar" em vários arquivos menores uma lista única de e-mails continda em um arquivo.

### Downloads:
[email_spliter.exe](https://github.com/guilhermemaas/email-spliter/blob/main/dist/email_spliter.exe).
[lista_exemplo.txt](https://github.com/guilhermemaas/email-spliter/blob/main/lista_exemplo/lista_exemplo.txt)

### Como usar:
1. Tenha uma lista de e-mails .txt, seguindo o padrão abaixo:
email1.xpto@xpto.com.br
email2.xpto@xpto.com.br
email3.xpto@xpto.com.br
email4.xpto@xpto.com.br
email5.xpto@xpto.com.br
2. Abra o CMD no diretório do executável, ou então utilize o caminho absoluto do mesmo.
3. Passe os parâmetros --file_in, --dir_out e --qty. Onde:
--file_in: Caminho do arquivo contendo a lista completa de e-mails.
--dir_out: Diretório de saída para os arquivos de e-mails splitados.
--qty: Quantidade de e-mails por arquivo. Exemplo: 50.
Exemplo:
email_spliter.exe --file_in C:\Users\guilh\Desktop\out\mails_list.txt --dir_out C:\Users\guilh\Desktop\out\out --qty 10
4. Verifique no diretório de saída os arquivos gerados.