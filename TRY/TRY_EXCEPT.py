try:
    #x = 9/0
    d = 2 + "Hola"
except Exception as ex:
    print("Entra en except, ha ocurrido una excepción,", TypeError(ex))
else:
    print("Entra en else, no ha ocurrido ninguna excepción")
finally:
    print("Entra en finally, por que siempre entra")
