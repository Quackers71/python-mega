phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for details in phone_numbers.items():
    print("%s" % (details[1]).replace('+', '00'))
    #print("{}").format(details[1]).replace('+', '00')