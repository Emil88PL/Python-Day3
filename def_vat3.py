def print_vat(gross, vatpc=20, message="Summary: "):
    net = gross / (1 + (vatpc/100))
    vat = gross - net
   # print(message, "Net: {0:5.2f} Vat: {1:5.2f}".format(net, vat))
    return f" {message}, 'Net: {0:5.2f} Vat: {1:5.2f}'.format(net,vat), 'at', {str(vatpc)}"
    

print(print_vat(150))
print(print_vat(150, 5))
print(print_vat(150, 5, "alleluja!"))
