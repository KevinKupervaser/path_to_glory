
# hydrogen_weight = 1.00794
# carbon_weight = 12.0107
# oxygen_weight = 15.9994

# formula H20
h2o = (2 * 1.00794) + 15.9994
print("The molecular weight of H2O is: ", h2o)

def molemass():
    hydrogen_atom = float(input("Enter the number of hydrogen atoms: "))
    carbon_atom = float(input("Enter the number of carbon atoms: "))
    oxygen_atom = float(input("Enter the number of oxygen atoms: "))
    carbohydrate = (carbon_atom * 12.0107) \
                   + (hydrogen_atom * 1.00794) \
                   + (oxygen_atom * 15.9994)
    print("The molecular weith of a carbohydrate is", carbohydrate)
molemass()

