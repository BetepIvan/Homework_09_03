from double_linked_list import LinkedList, Node


class ExtendedLinkedList(LinkedList):
    """
    Класс наследник с расширенными методами
    """

    def print_ll_from_tail(self):
        """Печать списка в обратном порядке от хвоста к голове"""
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        print("Список выведен с хвоста")

    def insert_at_index(self, data, index):
        """Добавление элемента по указанному индексу"""
        if index < 0:
            raise ValueError("Индекс не может быть отрицательным")

        if index == 0:
            return self.insert_at_head(data)

        new_node = Node(data)
        current_node = self.head
        current_index = 0

        while current_node is not None and current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        if current_node is None:
            return self.insert_at_tail(data)

        new_node.next_node = current_node.next_node
        new_node.prev_node = current_node

        if current_node.next_node is not None:
            current_node.next_node.prev_node = new_node
        else:
            self.tail = new_node

        current_node.next_node = new_node
        print(f"Узел с данными '{data}' добавлен на позицию {index}")

    def remove_node_index(self, index):
        """Удаление элемента по указанному индексу"""
        if self.head is None:
            raise Exception("Список пуст")

        if index < 0:
            raise ValueError("Индекс не может быть отрицательным")

        if index == 0:
            return self.remove_from_head()

        current_node = self.head
        current_index = 0

        while current_node is not None and current_index < index:
            current_node = current_node.next_node
            current_index += 1

        if current_node is None:
            raise IndexError("Индекс выходит за пределы списка")

        if current_node.next_node is None:
            return self.remove_from_tail()

        removed_data = current_node.data
        current_node.prev_node.next_node = current_node.next_node
        current_node.next_node.prev_node = current_node.prev_node

        print(f"Узел с данными '{removed_data}' удален с позиции {index}")
        return removed_data

    def remove_node_data(self, data):
        """Удаление элемента по данным узла"""
        if self.head is None:
            raise Exception("Список пуст")

        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                if current_node == self.head:
                    return self.remove_from_head()
                elif current_node == self.tail:
                    return self.remove_from_tail()
                else:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    print(f"Узел с данными '{data}' удален из списка")
                    return data

            current_node = current_node.next_node

        print(f"Узел с данными '{data}' не найден в списке")
        return None

    def len_ll(self):
        """Узнать длину связанного списка"""
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next_node

        return count

    def contains_from_head(self, data):
        """Проверка на содержание элемента с головы списка"""
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next_node

        return False

    def contains_from_tail(self, data):
        """Проверка на содержание элемента с конца списка"""
        current_node = self.tail

        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.prev_node

        return False

    def contains_from(self, data, from_head=True):
        """Проверка по выбору с начала или с хвоста"""
        if from_head:
            return self.contains_from_head(data)
        else:
            return self.contains_from_tail(data)


if __name__ == '__main__':
    print("=== ДЕМОНСТРАЦИЯ РАБОТЫ EXTENDED LINKED LIST ===\n")

    ext_ll = ExtendedLinkedList()

    print("1. ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ:")
    ext_ll.insert_at_head('element_00')
    ext_ll.insert_at_tail('element_02')
    ext_ll.insert_at_head('element_-01')
    ext_ll.insert_at_tail('element_03')
    ext_ll.insert_at_index('element_01', 2)

    print(f"\n2. ДЛИНА СПИСКА: {ext_ll.len_ll()}")

    print("\n3. ПЕЧАТЬ СПИСКА:")
    print("С головы:")
    ext_ll.print_ll_from_head()
    print("\nС хвоста:")
    ext_ll.print_ll_from_tail()

    print("\n4. ПРОВЕРКА СОДЕРЖАНИЯ ЭЛЕМЕНТОВ:")
    test_data = ['element_01', 'element_05', 'element_-01']
    for data in test_data:
        print(f"Содержит '{data}' (с головы): {ext_ll.contains_from_head(data)}")
        print(f"Содержит '{data}' (с хвоста): {ext_ll.contains_from_tail(data)}")

    print(f"\n5. СОДЕРЖИТ 'element_02' (выбор направления): {ext_ll.contains_from('element_02', False)}")

    print("\n6. УДАЛЕНИЕ ПО ИНДЕКСУ:")
    ext_ll.remove_node_index(1)
    ext_ll.print_ll_from_head()

    print("\n7. УДАЛЕНИЕ ПО ДАННЫМ:")
    ext_ll.remove_node_data('element_02')
    ext_ll.print_ll_from_head()

    print("\n8. ИТОГОВЫЙ СПИСОК:")
    ext_ll.print_ll_from_head()
    print()
    ext_ll.print_ll_from_tail()

    print(f"\n9. ФИНАЛЬНАЯ ДЛИНА СПИСКА: {ext_ll.len_ll()}")