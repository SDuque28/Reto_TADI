
import io

class Reto2:
    
    class Node:
        def __init__(self,value):
            self.value = value
            self.next_node = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.menu()
        self.list_to_text()
    
    def show_nodes_list(self):
        node_list = []
        current_node = self.head
        while (current_node != None):
            node_list.append(current_node.value)
            current_node = current_node.next_node
        print(f'{node_list} Cantidad de nodos {self.length}')
  
    def prepend_node(self,value):
        new_node = self.Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.length+= 1
    
    def append_node(self,value):
        new_node = self.Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length+= 1
    def shift_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            remove_node = self.head
            self.head = remove_node.next_node
            remove_node.next_node = None
            self.length -= 1
            return remove_node
        
    def pop_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current_node = self.head
            new_tail = current_node
            while current_node.next_node != None:
                new_tail = current_node
                current_node = current_node.next_node
            self.tail = new_tail
            self.tail.next_node = None
            self.length -= 1
            return current_node
            
    def reverse_list(self):
        reverse_nodes = None
        current_node = self.head
        self.tail = current_node
        while current_node != None:
            next_node =current_node.next_node
            current_node.next_node = reverse_nodes
            reverse_nodes = current_node
            current_node = next_node
        self.head = reverse_nodes
        return
        
    def get(self,index):
        if index == self.length+1:
            return self.tail    
        elif index == 1:
            return self.head
        elif not (index > self.length+1 or index < 1):
            current_node = self.head
            contador = 1
            while contador != index:
                current_node = current_node.next_node
                contador += 1
            return current_node
        else:
            print('El indice no pertenece la la lista')
            return None
        
    def update(self,index,value):
        nodo_objetivo = self.get(index)
        if nodo_objetivo != None:
            nodo_objetivo.value = value
        else:
            print('El indice no pertenece a la lista')
            return None
        
    def insert(self,index,value):
        if index == self.length+1:
            return self.append_node(value)
        elif index == 1:
            return self.prepend_node(value)
        elif not index > self.length+1 or index <= 0:
            new_node = self.Node(value)
            nodos_anteriores = self.get(index-1)
            nodos_siguientes = nodos_anteriores.next_node
            nodos_anteriores.next_node = new_node
            new_node.next_node = nodos_siguientes
            self.length += 1
        else:
            return None
        
    def remove(self,index):
        if index == 1:
            return self.shift_node()
        elif index == self.length+1:
            return self.pop_node()
        elif not index > self.length or index < 1:
            nodos_anteriores = self.get(index-1)
            nodo_removido = nodos_anteriores.next_node
            nodos_anteriores.next_node = nodo_removido.next_node
            nodo_removido.next_node = None
            self.length -= 1
            return nodo_removido
        else:
            return None
        
    def add_text_to_list(self):
        with io.open('texto_prueba.txt','r+',encoding='utf-8') as data_file:
            file_line = data_file.readline()
            while file_line != '':
                self.append_node(file_line)
                file_line = data_file.readline()
        data_file.close()
    
    def show_file_content(self):
        with io.open('texto_prueba.txt','r+',encoding='utf-8') as data_file:
            file_line = data_file.readline()
            while file_line != '':
                print(file_line,end='')
                file_line = data_file.readline()
        data_file.close()
        
    def menu(self):
        print('>>>>> MENU <<<<<')
        print('a. Desea leer el archivo')
        print('b. Quiere editar el archivo')
        print('c. Desea sobreescribir el archivo')
        while True:
            try:
                seleccion = str(input('Seleccion:  '))
                if seleccion == 'a':
                    self.add_text_to_list()
                    self.show_file_content()
                elif seleccion == 'b':
                    self.vaciar_lista()
                    line_write = input('El texto nuevo que desea añadir es:\n   >>>')
                    with io.open('texto_prueba.txt','w',encoding='utf-8') as data_file:
                        data_file.write(line_write)
                    data_file.close()
                    self.add_text_to_list()
                elif seleccion == 'c':
                    line_write = input('Que le deseas añadir al texto:\n   >>>')
                    with io.open('texto_prueba.txt','a',encoding='utf-8') as data_file:
                        data_file.write('\n'+line_write)
                    data_file.close()
                    self.add_text_to_list()
                elif seleccion != 'a' and seleccion != 'b' and seleccion != 'c':
                    raise ValueError
                print('\nQue deseas continuar haciendo:')
                print('a. Insertar un nuevo nodo')
                print('b. Eliminar un nodo')
                print('c. Consultar el valor de un nodo especificado')
                print('d. Editar el valor de un nodo especificado')
                print('e. Invertir la lista')
                print('f. Vaciar la lista')
                print('g. Salir del sistema')
                while True:
                    try:
                        opcion = str(input('Selecion:  '))
                        if opcion == 'a':
                            print('1. Al inicio')
                            print('2. Al final')
                            print('3. En una posicion especifica')
                            while True:
                                try:
                                    respuesta = int(input('Seleccion:   '))
                                    if respuesta == 1:
                                        añadir = str(input('Escriba lo que desea añadir:\n   >>>'))
                                        self.prepend_node(añadir)
                                        self.show_nodes_list()
                                    elif respuesta == 2:
                                        añadir = str(input('Escriba lo que desea añadir:\n   >>>'))
                                        self.append_node(añadir)
                                        self.show_nodes_list()
                                    elif respuesta == 3:
                                        while True:
                                            try:
                                                indice = int(input('Digite el indice en el cual desea añadir el nodo:\n   >>>'))
                                                añadir = str(input('Escriba lo que desea añadir:\n   >>>'))
                                                self.insert(indice,añadir)
                                                break
                                            except ValueError:
                                                print('Se esperaba un valor numerico')
                                    else:
                                        raise ValueError
                                    break
                                except ValueError:
                                    print('Se esperaba un valor numerico entre 1 y 3')
                        elif opcion == 'b':
                            print('1. Al inicio')
                            print('2. Al final')
                            print('3. En una posicion especifica')
                            while True:
                                try:
                                    respuesta = int(input('Selección:   '))
                                    if respuesta == 1:
                                        self.shift_node()
                                    elif respuesta == 2:
                                        self.pop_node()
                                    elif respuesta == 3:
                                        while True:
                                            try:
                                                indice = int(input('Digite el indice del cual lo desea borar:\n   >>>'))
                                                self.remove(indice)
                                                break
                                            except ValueError:
                                                print('Se esperaba un valor numerico')
                                    else:
                                        raise ValueError
                                    break
                                except ValueError:
                                    print('Se esperava un valor numerico entre 1 y 3')
                        elif opcion == 'c':
                            while True:
                                try:
                                    indice = int(input('Digite el indice del nodo que desea obtener:\n   >>>'))
                                    print(f'El valor del nodo que busca es: {self.get(indice).value}')
                                    break
                                except ValueError:
                                    print('Se esperaba un valor numerico')
                        elif opcion == 'd':
                            while True:
                                try:
                                    indice = int(input('Digite el indice el cual desea reemplazar:\n   >>>'))
                                    valor = str(input('Digite el valor del nodo a reemplazar:\n   >>>'))
                                    self.update(indice,valor)
                                    break
                                except ValueError:
                                    print('Se esperaba un valor numerico')
                        elif opcion == 'e':
                            self.reverse_list()
                        elif opcion == 'f':
                            self.vaciar_lista()
                        elif opcion == 'g':
                            break
                        else:
                            raise ValueError
                        break
                    except ValueError:
                        print('Se esperaba que selecione una de las opciones anteriores')
                break
            except ValueError:
                    print('Se esperaba una letra de las anteriores')
        
    def list_to_text(self):
        with io.open('texto_prueba.txt','w',encoding='utf-8') as data_file:
            current_node = self.head
            contador = 0
            while current_node != None:
                if '\n' in current_node.value:
                    current_node.value = current_node.value.replace('\n','')
                    if contador == 0:
                        data_file.write(current_node.value)
                        contador += 1
                    else:
                        data_file.write('\n'+current_node.value) 
                elif contador == 0:
                    data_file.write(current_node.value)
                    contador += 1
                else:
                    data_file.write('\n'+current_node.value) 
                current_node = current_node.next_node
        data_file.close()
        
        
    def vaciar_lista(self):
        for item in range (0,self.length+1):
            self.pop_node()
