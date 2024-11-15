def check_ip(address):
    number_list = address.split(".")
    # if len(number_list) != 4:
    #     return False
    for number in number_list:
        if not number.isnumeric() or not(0 <= int(number) <= 255):
            return False
    return True

for i in range(int(input())):
    address_ip = input()
    if check_ip(address_ip) == True and address_ip.count(".") == 3:
        print("YES")
    else:
        print("NO")