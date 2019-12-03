#! /usr/bin/env python3
import argparse
import copy


class Intcode_Computer:
    def __init__(self, intcode_file: str = None, cursor: int = 0):
        self.intcode = []

        if intcode_file:
            with open(intcode_file, 'r') as file_handle:
                for opcode in file_handle.read().split(','):
                    self.intcode.append(int(opcode))

        self.cursor = cursor


    def set_cursor(self, new_cursor):
        self.cursor = new_cursor


    def set_noun(self, new_noun):
        self.intcode[1] = new_noun


    def set_verb(self, new_verb):
        self.intcode[2] = new_verb


    def set_intcode(self, new_intcode):
        self.intcode = new_intcode


    def opcode_1(self):
        """
        Opcode 1 adds together numbers read from two positions
        and stores the result in a third position.  The 3 ints
        immediately following an Opcode 1 indicate the 3 positions.
        The first 2 indicate positions from which to read input
        values, and the third indicates where output should be
        stored.
        
        :param pos_1: value stored at first indicated position
        :type pos_1: int
        :param pos_2: value stored at second indicated position
        :type pos_2: int
        :param pos_3: Location in intcode to insert sum
        :type pos_3: int
        """


        pos_1 = self.intcode[self.cursor + 1]
        pos_2 = self.intcode[self.cursor + 2]
        pos_3 = self.intcode[self.cursor + 3]
        self.intcode[pos_3] = self.intcode[pos_1] + self.intcode[pos_2]
        self.cursor += 4


    def opcode_2(self):
        """
        Opcode 2 multiplies together numbers read from two positions
        and stores the result in a third position.  The 3 ints
        immediately following an Opcode 1 indicate the 3 positions.
        The first 2 indicate positions from which to read input
        values, and the third indicates where output should be
        stored
        
        :param pos_1: value stored at first indicated position
        :type pos_1: int
        :param pos_2: value stored at second indicated position
        :type pos_2: int
        :param pos_3: Location in intcode to insert product
        :type pos_3: int
        """
        
        
        pos_1 = self.intcode[self.cursor + 1]
        pos_2 = self.intcode[self.cursor + 2]
        pos_3 = self.intcode[self.cursor + 3]
        self.intcode[pos_3] = self.intcode[pos_1] * self.intcode[pos_2]
        self.cursor += 4

    
    def opcode_99(self):
        """
        Halts the program and returns the intcode in its current state
        """


        print(self.intcode)
        print("GOODBYE")
        exit(0)


    def opcode_99_dont_exit(self):
        return self.intcode


    def run(self):
        """
        Runs the intcode computer.
        """
        while True:
            if self.intcode[self.cursor] == 1:
                self.opcode_1()
            elif self.intcode[self.cursor] == 2:
                self.opcode_2()
            elif self.intcode[self.cursor] == 99:
                self.opcode_99()
            else:
                print("Halting and catching fire\n1202")
                exit(1202)


    def run_dont_exit(self):
        while True:
            if self.intcode[self.cursor] == 1:
                self.opcode_1()
            elif self.intcode[self.cursor] == 2:
                self.opcode_2()
            elif self.intcode[self.cursor] == 99:
                return self.opcode_99_dont_exit()
            else:
                print("Halting and catching fire\n1202")
                exit(1202)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="File of intcode state as CSV")
    args = parser.parse_args()

    INITIAL_MEMORY_STATE = []
    with open(args.file, 'r') as memory_state:
        for opcode in memory_state.read().split(','):
            INITIAL_MEMORY_STATE.append(int(opcode))

    new_computer = Intcode_Computer()
    new_computer.set_intcode(copy.deepcopy(INITIAL_MEMORY_STATE))

    noun = 0
    verb = 0

    while noun <= 99:
        new_computer.set_noun(noun)
        while verb <= 99:
            new_computer.set_verb(verb)
            test_intcode = new_computer.run_dont_exit()
            print(f'ANSWER = {new_computer.intcode[0]}')
            print(f'ANSWER = {test_intcode[0]}')
            if test_intcode[0] == 19690720:
                print(f'{noun=} | {verb=} | {test_intcode[0]=} | answer={100 * noun + verb}')
                exit(0)
            else:
                print(f'{noun=} | {verb=}')
                new_computer.set_intcode(INITIAL_MEMORY_STATE)
                verb += 1
        noun += 1
        verb = 0

    print('Could not find values')
    print(f'Final Intcode State:\t{test_intcode[0]=} | {test_intcode[1]=} | {test_intcode[2]=}')
    print(f'Final Intcode State:\t{new_computer.intcode[0]=} | {new_computer.intcode[1]=} | {new_computer.intcode[2]=}')
