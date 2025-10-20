with open("Table_de_multiplication.txt","w") as file:
   for i in range (1,11) :
       file.write(f"La table de multiplication de {i} est : \n")
       for j in range (1,11) :
          file.write(f"{i} x  {j} = {i*j} \n")