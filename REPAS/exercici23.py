# Crear una funció que mostri, per consola, i guardi en un arxiu extern, 
# un JSON amb una key de nom book que contindrà titel, cover, year i pages. 
# Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values). 

import json

def crearJSON():
    books = []

    for i in range(1, 5):
        books.append(
            {
            "book": {
                    "title": f"title {i}",
                    "cover": f"cover {i}",
                    "year": f"year {i}",
                    "pages": f"page {i}"
                }
            }  
        ) 
                
    with open("books.json", "w") as file:
        json.dump(books, file, indent=2)
    
    with open("books.json", "r") as file:
        result = json.load(file)
        print(json.dumps(result, indent=2))
    
        
crearJSON()