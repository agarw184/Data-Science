def histogram(data,n,l,h):
    if (n > 0 and h >= l):
        hist = []         
        w = ((h-l)/n)
        hist = n*[0]
        for i in range(n):
            for counter in range(len(data)):
                    if (data[counter] <= l or data[counter] >= h):
                        counter = counter + 1
                    else:
                        if(data[counter] >= (l+(i*w)) and data[counter] < (l+(i+1)*w)):
                            hist[i] = hist[i] + 1
    else:
        print("Error")
        return hist
    return hist


def addressbook(name_to_phone,name_to_address):
    address_to_all = {}                          ##New dictionary
    for name in name_to_address:
        if name_to_address[name] not in address_to_all:
            address_to_all[name_to_address[name]] = ([name],name_to_phone[name]) 
        else:
            address_to_all[name_to_address[name]][0].append(name)
            if name_to_phone[name] == address_to_all[name_to_address[name]][1]:
                continue
            else:
               print('Warning: {0} has a different number for {1} than {2}. Using the number for {3}' .format(name, name_to_address[name], address_to_all[name_to_address[name]][0][0], address_to_all[name_to_address[name]][0][0]))
    return address_to_all


    