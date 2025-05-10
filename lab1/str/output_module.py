import global_data

def print_numbered_list():
    print("\nПрізвища у вигляді нумерованого списку:")
    for i in range(len(global_data.surnames_list)):
        print(f"{i + 1}. {global_data.surnames_list[i]}")