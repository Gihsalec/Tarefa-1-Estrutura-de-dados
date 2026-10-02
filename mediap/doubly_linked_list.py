import unittest
 
 
class DoublyLinkedList:
 
    class _DoublyNode:
        def __init__(self, elem, prev, next_node):
            self._elem = elem #_elem pq ele é privado, vale pros outros tbm
            self._prev = prev
            self._next = next_node
 
        def __str__(self):
            if self._elem is not None:
                return str(self._elem) + ' '
            else:
                return '|'
 
        @property
        def element(self):
            return self._elem
 
        @element.setter
        def element(self, elem):
            self._elem = elem
 
        @property
        def previous(self):
            return self._prev
 
        @previous.setter
        def previous(self, node):
            self._prev = node
 
        @property
        def next(self):
            return self._next
 
        @next.setter
        def next(self, node):
            self._next = node
 
    def __init__(self, size=0):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header.next = self._trailer
        self._trailer.previous = self._header
        self._length = 0
        for _ in range(size):
            self.append(None)
 
    def __len__(self):
        return self._length

    def insert(self, index, elem):
        if index >= self._length:
            index = self._length
        elif index < 0:
            index = max(self._length + index, 0)
        if self.empty():
            new_node = self._DoublyNode(elem, self._header, self._trailer)
            self._header.next = new_node
            self._trailer.previous = new_node
        elif index == 0:
            new_node = self._DoublyNode(elem, self._header, self._header.next)
            self._header.next.previous = new_node
            self._header.next = new_node
        else:
            this = self._header.next
            successor = this.next
            pos = 0
            while pos < index - 1:
                this = successor
                successor = this.next
                pos += 1
            new_node = self._DoublyNode(elem, this, successor)
            this.next = new_node
            successor.previous = new_node
 
        self._length += 1
 
    def remove(self, elemento):
        if not self.empty():
            node = self._header.next
            pos = 0
            found = False
            while not found and pos < self._length:
                if node.element == elemento:
                    found = True
                else:
                    node = node.next
                    pos += 1
            if found:
                node.previous.next = node.next
                node.next.previous = node.previous
                self._length -= 1
 
    def count(self, elem):
        result = 0
        this = self._header.next
        while this is not self._trailer:
            if this.element == elem:
                result += 1
            this = this.next
        return result
 
    def clear(self):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header.next = self._trailer
        self._trailer.previous = self._header
        self._length = 0
 
    def index(self, elem):
        result = None
        pos = 0
        this = self._header.next
        while not result and pos < self._length:
            if this.element == elem:
                result = pos
                break
            this = this.next
            pos += 1
        return result
 
    def length(self):
        return self._length
 
    def empty(self):
        return self._length == 0
 
    def __str__(self):
        result = ''
        aux = self._header
        result += aux.__str__()
        while aux is not self._trailer:
            aux = aux.next
            result += aux.__str__()
        return result
 
    def remove_all(self, item):
        while self.index(item) is not None:
            self.remove(item)
 
    def remove_at(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        if index == 0:
            self._header.next = self._header.next.next
            self._header.next.previous = self._header
        elif index == self._length - 1:
            self._trailer.previous = self._trailer.previous.previous
            self._trailer.previous.next = self._trailer
        else:
            aux = self._header.next
            for _ in range(index):
                aux = aux.next
            aux.previous.next = aux.next
            aux.next.previous = aux.previous
        self._length -= 1
 
    def append(self, item):
        self.insert(self._length, item)
 
    def replace(self, index, item):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        aux = self._header.next
        for _ in range(index):
            aux = aux.next
        aux.element = item
 
    def __iter__(self):
        aux = self._header.next
        while aux is not self._trailer:
            yield aux.element
            aux = aux.next
 
 
class TestDoublyLinkedList(unittest.TestCase):
 
    def test_inserting_element_at_specific_index(self):
        lista = DoublyLinkedList()
        lista.insert(0, "a")
        lista.insert(1, "b")
        lista.insert(1, "c")
        self.assertEqual(lista.length(), 3)
        self.assertEqual(lista.index("c"), 1)
        self.assertEqual(lista.index("a"), 0)
        self.assertEqual(lista.index("b"), 2)
 
    def test_removing_first_occurrence_of_element(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("a")
        lista.remove("a")
        self.assertEqual(lista.count("a"), 1)
 
    def test_counting_occurrences_of_element(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("a")
        self.assertEqual(lista.count("a"), 2)
        self.assertEqual(lista.count("b"), 1)
 
    def test_clearing_all_elements(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.clear()
        self.assertEqual(lista.length(), 0)
 
    def test_retrieving_index_of_element(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        self.assertEqual(lista.index("b"), 1)
 
    def test_removing_all_occurrences_of_element(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("a")
        lista.remove_all("a")
        self.assertEqual(lista.count("a"), 0)
 
    def test_removing_element_at_specific_index(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("c")
        lista.remove_at(1)
        self.assertEqual(lista.index("c"), 1)
        self.assertEqual(lista.index("a"), 0)
        self.assertIsNone(lista.index('b'))
 
    def test_appending_element_to_end(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        self.assertEqual(lista.index("b"), 1)
 
    def test_replacing_element_at_specific_index(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.replace(1, "c")
        self.assertEqual(lista.index("c"), 1)
 
 
class Playlist:
    """
    Playlist do player (Seção 3.1 do PDF), construída por composição sobre
    a DoublyLinkedList (é ela quem guarda as Tracks; aqui só some o cursor
    e as regras de navegação em cima da lista encadeada).
 
    O "cursor" é guardado como um índice inteiro (posição da faixa em
    execução). play_next()/play_prev() são O(1) porque apenas movem esse
    índice; quem percorre a lista de fato para localizar o nó é a própria
    DoublyLinkedList (as operações de navegação da playlist não percorrem
    a lista inteira a cada chamada, só avançam/recuam 1 posição).
    """
 
    def __init__(self):
        self._faixas = DoublyLinkedList()
        self._cursor = 0  # posição da faixa "atual" (0 = primeira)
 
    def add(self, track):
        """Anexa uma nova faixa ao final da playlist."""
        self._faixas.append(track)
 
    def remove_at(self, pos):
        """Remove a faixa na posição pos da playlist."""
        self._faixas.remove_at(pos)
        if self._cursor >= len(self._faixas) and self._cursor > 0:
            self._cursor = len(self._faixas) - 1
 
    def current(self):
        """Retorna a faixa em execução (ou None se a playlist estiver vazia)."""
        if len(self._faixas) == 0:
            return None
        return self._faixas_get(self._cursor)
 
    def play_next(self):
        """Avança o cursor e retorna a próxima faixa. Erro se já estiver na última."""
        if self._cursor >= len(self._faixas) - 1:
            print("Erro: já está na última faixa da playlist.")
            return None
        self._cursor += 1
        return self.current()
 
    def play_prev(self):
        """Retrocede o cursor e retorna a faixa anterior. Erro se já estiver na primeira."""
        if self._cursor <= 0:
            print("Erro: já está na primeira faixa da playlist.")
            return None
        self._cursor -= 1
        return self.current()
 
    def reset_cursor(self):
        """Reinicializa o cursor para a primeira faixa."""
        self._cursor = 0
 
    def _faixas_get(self, pos):
        """Auxiliar: retorna o elemento na posição pos (percorre a partir do header)."""
        node = self._faixas._header.next
        for _ in range(pos):
            node = node.next
        return node.element
 
    def __len__(self):
        return len(self._faixas)
 
    def __iter__(self):
        return iter(self._faixas)
