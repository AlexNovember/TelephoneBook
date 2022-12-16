
def import_data(data, sep=None):
    with open('base_phone.csv', 'a+') as file:
            file.write(join(data))
            file.write(f"\n")