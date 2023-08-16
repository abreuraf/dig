def handle_uploaded_file(f):
    with open('bom/teste.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
