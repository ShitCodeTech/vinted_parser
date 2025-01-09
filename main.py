from utils.json_handler import get_items, get_my_ip


if __name__ == "__main__":
    print(get_items())
    with open('1.txt', 'rw') as file:
        file.write(get_items())
    get_my_ip()