if __name__ == "__main__":

    my_list = ["apple", "cacao", "lemon"]

    for item in my_list:
        print(item)
        if item == 'banana':
            break
    else:
        raise ValueError("No banana found!")


    try:
        dangerous_call()
    except OSError:
        print("error")
    else:
        after_call()