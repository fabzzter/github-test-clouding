# Robot Barista

from module import menu
from module import bill

def menu_reading(action, mr_order="-", mr_quantity=0):
    global menu
    global bill
    item_list = "\n"
    
    # Recorre la lista menu
    for mr_item in menu:
        match action:
            # Genera el menú para el cliente, concatenando en item_list todos los elementos que tengan stock
            case "menu_list": 
                if (mr_item[1] == 0):
                    continue
                else:
                    item_list += mr_item[0] + "\n"
            # Busca el item seleccionado dentro del menú, para validar disponibilidad y agregar el costo al total de la orden
            case "stock_validation": 
                if (mr_item[0].lower() == mr_order.lower()):
                    if (int(mr_quantity) > mr_item[1]):
                        print(f"Lo lamentamos, pero solo tenemos {mr_item[1]} unidades de {mr_order}")
                    else:
                        mr_item[1]-= int(mr_quantity)
                        bill += (float(mr_quantity) * float(mr_item[2]))
                    return
                else:
                    continue
    
    match action:
        # Retorna el menú disponible
        case "menu_list":
            return item_list
        # Si se llega a este segmento es porque no se encontró coincidencia del item dentro de la lista del menú
        case "stock_validation":
            print(f"Disculpa, {mr_order} no esta en nuestro menú")
    return

 
# Main------------------------------------------------------------------------
print("Hola, bienvenido a la cafeteria de Fabrizzio")
name = input("¿Cual es tu nombre? \n")

# Ciclo que itera presentando el menú al cliente, y solicitando item y cantidad que requiere en la orden. Finaliza cuando el cliente indica que no quiere seguir ordenando
ans="si"
while (ans.lower() == "si"):
    print(name + ", nuestro menú es el siguiente:")
    menu_list = menu_reading("menu_list")
    print(menu_list)            
    order = input("¿Que deseas ordenar? \n")        
    quantity = input("¿Cuantas unidades deseas? \n")
    menu_reading("stock_validation", order, quantity)
    ans=input("¿Deseas seguir ordenando? (si/no) \n")

#Se imprime en pantalla el total del costo de la orden    
print(f"El valor total de tu orden es: ${bill}")               
    
