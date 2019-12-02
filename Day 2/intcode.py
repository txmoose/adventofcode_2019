#! /usr/bin/env python3
import argparse
import copy


class Intcode_Computer:
    def __init__(self, intcode_file: str, cursor: int = 0):
        self.intcode = []
        with open(intcode_file, 'r') as file_handle:
            for opcode in file_handle.read().split(','):
                self.intcode.append(int(opcode))
        self.cursor = cursor


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

    def find_noun_and_verb_for_specific_output(self, output: int):
        """
        Runs the intcode computer to find a specific noun and verb
        that produce a specific input.  Current limit is 0 - 99 for both.
        
        :param output: Specific Output being searched for
        :type output: int
        :return: Noun and Verb that produce specific output
        :rtype: int, int
        """
        self.INITIAL_MEMORY_STATE = copy.deepcopy(self.intcode)
        self.noun = 0
        self.verb = 0
        while True:
            self.cursor = 0
            self.intcode[1] = self.noun
            self.intcode[2] = self.verb
            print(f'DEBUG: {self.noun=} | {self.verb=} | {self.intcode[0]} | {self.cursor=}')
            if self.intcode[self.cursor] == 1:
                self.opcode_1()
            elif self.intcode[self.cursor] == 2:
                self.opcode_2()
            elif self.intcode[self.cursor] == 99:
                if self.intcode[0] == output:
                    print(f'{self.intcode[1]=}\n{self.intcode[2]=}')
                    print('GOODBYE')
                    exit(0)
                elif self.verb <= 99:
                    self.intcode = self.INITIAL_MEMORY_STATE
                    self.verb += 1
                    continue
                else:
                    if self.noun >= 99 and self.verb >= 99:
                        print('Could not find an initial memory state for given output')
                        print('BYE')
                        exit(1)
                    else:
                        self.intcode = self.INITIAL_MEMORY_STATE
                        self.verb = 0
                        self.noun += 1
                        continue

            else:
                print("Halting and catching fire\n1202")
                exit(1202)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="File of intcode state as CSV")
    args = parser.parse_args()

    new_computer = Intcode_Computer(args.file)
    #new_computer.run()
    new_computer.find_noun_and_verb_for_specific_output(19690720)