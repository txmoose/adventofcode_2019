#!/usr/bin/env python3
import copy


class Intcode_Computer():
    def __init__(self, memory, pointer = 0):
        self.memory = memory
        self.pointer = pointer


    def set_memory(self, memory):
        self.memory = copy.deepcopy(memory)


    def store_at_address(self, value, address):
        self.memory[address] = value


    def set_pointer(self, pointer):
        self.pointer = pointer


    def set_noun(self, noun):
        self.memory[1] = noun


    def set_verb(self, verb):
        self.memory[2] = verb


    def increment_pointer(self, increment):
        self.pointer += increment


    def op_code_1(self):
        num_of_values = 4
        value_1_location = self.memory[self.pointer + 1]
        value_2_location = self.memory[self.pointer + 2]
        store_location = self.memory[self.pointer + 3]
        value_1 = self.memory[value_1_location]
        value_2 = self.memory[value_2_location]
        store_value = value_1 + value_2
        self.store_at_address(store_value, store_location)
        self.increment_pointer(num_of_values)


    def op_code_2(self):
        num_of_values = 4
        value_1_location = self.memory[self.pointer + 1]
        value_2_location = self.memory[self.pointer + 2]
        store_location = self.memory[self.pointer + 3]
        value_1 = self.memory[value_1_location]
        value_2 = self.memory[value_2_location]
        store_value = value_1 * value_2
        self.store_at_address(store_value, store_location)
        self.increment_pointer(num_of_values)


    def op_code_99(self):
        return self.memory


    def run(self):
        while True:
            if self.memory[self.pointer] == 1:
                self.op_code_1()
                continue
            elif self.memory[self.pointer] == 2:
                self.op_code_2()
                continue
            elif self.memory[self.pointer] == 99:
                return self.op_code_99()
            else:
                print("Halting and catching fire\n1202")
                exit(1202)


if __name__ == "__main__":
    INITIAL_MEMORY = []
    INITIAL_MEMORY_FILE = "/Users/kyle/git/adventofcode/2019/Day 2/pre_1202_error.csv"
    TARGET_SOLUTION = 19690720

    with open(INITIAL_MEMORY_FILE, 'r') as mem:
        for address in mem.read().split(','):
            INITIAL_MEMORY.append(int(address))

    intcode_computer = Intcode_Computer(INITIAL_MEMORY)

    noun = 0
    verb = 0

    while noun <= 99:
        while verb <= 99:
            intcode_computer.set_memory(INITIAL_MEMORY)
            intcode_computer.set_pointer(0)
            intcode_computer.set_noun(noun)
            intcode_computer.set_verb(verb)
            solution = intcode_computer.run()

            if solution[0] == TARGET_SOLUTION:
                print(f'{noun=} | {verb=} | Solution = {100 * noun + verb}')
                exit(0)
            else:
                print(f'{solution[0]=} | {noun=} | {verb=}')
                verb += 1
                continue

        noun += 1
        verb = 0


    print(f'Could not find solution')
    exit(1)
