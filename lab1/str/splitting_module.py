import global_data

def line_splitting ():
    str_surnames = global_data.str_surnames.split(",")
    for surname in str_surnames:
        cleaned = surname.strip()
        global_data.surnames_list.append(cleaned)
#surnames_list = [surname.strip() for surname in str_surnames.split(',')]
