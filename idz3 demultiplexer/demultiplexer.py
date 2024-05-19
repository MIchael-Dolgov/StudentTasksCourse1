class Demultiplexer:
    def __init__(self, num_output):
        self.num_output = num_output
        self.outputs = [False] * num_output

    def select(self, input_signal, select_line):
        if select_line < 0 or select_line >= self.num_output:
            print("Error: Invalid select line")
            return
        for i in range(self.num_output):
            if i == select_line:
                self.outputs[i] = input_signal
            else:
                self.outputs[i] = False

# Пример использования:
demux = Demultiplexer(4)  # Создаем демультиплексор с 4 выходами

demux.select(True, 2)    # Выбираем выход 2 и устанавливаем его в True
print("Outputs:", demux.outputs)  # Ожидаемый вывод: Outputs: [False, False, True, False]

demux.select(False, 0)   # Выбираем выход 0 и устанавливаем его в False
print("Outputs:", demux.outputs)  # Ожидаемый вывод: Outputs: [False, False, False, False]
