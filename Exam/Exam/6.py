# urls = ["http://stackoverflow.com:8080/some/folder?test=/questions/9626535/get-domain-name-from-url",
#         "www.Stackoverflow.com:8080/some/folder?test=/questions/9626535/get-domain-name-from-url",
#         "http://stackoverflow.com/some/folder?test=/questions/9626535/get-domain-name-from-url",
#         "https://StackOverflow.com:8080?test=/questions/9626535/get-domain-name-from-url",
#         "stackoverflow.com?test=questions&v=get-domain-name-from-url"]
url = input('Enter URL address: ')

split_address = url.split("://")[-1].split('www.')
domain = split_address[-1].split("?")[0].split('/')[0].split(':')[0].split('.')[0].lower()
print(domain)
