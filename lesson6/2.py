def add_item_good(item, box=None):
    if box is None:
        box = []

    box.append(item)
    return box


korobka = ["арбуз"]
print(add_item_good("банан", korobka))

# result_1 = add_item_good("киви")
# print(result_1)
#
# result_2 = add_item_good("яблоко")
# print(result_2)
#
# result_3 = add_item_good("персик")
# print(result_3)


