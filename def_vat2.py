def print_vat(gross, vatpc=20):
    net = gross / (1 + (vatpc/100))
    vat = gross - net
    return "Net: {0:5.2f} Vat: {1:5.2f}".format(net, vat)

print(print_vat(150))