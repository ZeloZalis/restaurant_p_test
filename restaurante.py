import sqlite3

def crear_db():
    connection = sqlite3.connect('restaurante.db')
    cursor = connection.cursor()
    try:
        cursor.execute('CREATE TABLE categoria' '(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL)')
        cursor.execute('CREATE TABLE plato' '(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL, categoria_id INTEGER NOT NULL, FOREIGN KEY (categoria_id) REFERENCES categoria(id))')
        connection.commit()
        print('La base de datos se ha creado correctamente.')
    except:
        print('Error, las tablas ya están creadas.')
    connection.close()
# crear_db()

def agregar_categoria():
    con = sqlite3.connect('restaurante.db')
    cursor = con.cursor()
    try:
        new_cat = input('\nIngrese el nombre de la nueva categoría: ')
        add = []
        add.append(new_cat)
        cursor.execute('INSERT INTO categoria VALUES (null,?)', add)
        print(f'Se ha agregado correctamente la categoría {add}')
        con.commit()
    except Exception as e:        
        print(f'Error: {e}\n')
    con.close()

def mostrar_menu():
    while True:
        valor = int(input('\nBienvenido a la Gestión del Menú, qué desea realizar?\n1. Agregar una nueva categoría.\n2. Agregar nuevo plato.\n3. Salir.\n'))
        if valor == 1:
            agregar_categoria()
        elif valor == 2:
            agregar_plato()
        elif valor == 3:
            break
        else:
            print('Ingrese un número válido.')

def agregar_plato():
    print('\nLas categorías existentes son las siguientes, escoja una (marcando su número) para agregar un plato.')
    con = sqlite3.connect('restaurante.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM categoria')
    categories = cursor.fetchall()
    for category in categories:
        print(category)
    valor = int(input(''))
    platillo = input('Ingrese el nombre del plato: ')
    cursor.execute("""INSERT INTO plato VALUES(null,?,?)""", (platillo, valor))
    print(f'Se ha insertado el platillo "{platillo}" en la categoría {valor}.')
    con.commit()
    con.close()
mostrar_menu()