import pandas as pd
import numpy as np

if __name__ == '__main__':
    path = "./ISE.xlsx"
    switch = ["T3", "U3", "T4", "V3", "V4", "W4", "Y4", "Y6", "W7", "Y8", "Y7", "T1",
              "U1", "U2", "W1", "W2", "Y1", "AA1", "V2", "Y2"]
    bulb = ["K1", "J1", "H2", "G2", "F1", "E2", "D1", "B1", "B2", "N2", "M3", "K3", "H3", "N4", "L4", "J4"]
    button = ["R4", "AA4", "AB6"]

    df = pd.read_excel(path, header=None)
    array = df.values
    input = array[0]
    output = array[1]
    input_button = []
    clock = []
    if array.shape[0] >= 3:
        input_button = array[2]
    if array.shape[0] >= 4:
        clock = array[3]
    # 去除input的nan
    for i in range(len(input)):
        if isinstance(input[i], float):
            input = input[:i]
            break
    # 去除output的nan
    for i in range(len(output)):
        if isinstance(output[i], float):
            output = output[:i]
            break
    # 去除input_button的nan
    if array.shape[0] >= 3:
        for i in range(len(input_button)):
            if isinstance(input_button[i], float):
                input_button = input_button[:i]
                break
    # 去除clock的nan
    if array.shape[0] >= 4:
        for i in range(len(clock)):
            if isinstance(clock[i], float):
                clock = clock[:i]
                break
    print("input: ", input)
    print("output: ", output)
    if array.shape[0] >= 3:
        print("input_button: ", input_button)
    if array.shape[0] >= 4:
        print("clock: ", clock)
    n_input = 0
    n_output = 0
    n_button = 0
    print("//input")
    for i in input:
        if '[' in i:
            count = int(i[i.index('[')+1:-1])
            name = i[:i.index('[')]
            for j in range(count+1):
                print('NET "{}[{}]" LOC = {};'.format(name, count-j, switch[n_input]))
                n_input += 1
        else:
            print('NET "{}" LOC = {};'.format(i, switch[n_input]))
            if i in clock:
                print('NET "{}" CLOCK_DEDICATED_ROUTE = FALSE;'.format(i))
            n_input += 1
    if array.shape[0] >= 3:
        for i in input_button:
            if '[' in i:
                count = int(i[i.index('[')+1:-1])
                name = i[:i.index('[')]
                for j in range(count+1):
                    print('NET "{}[{}]" LOC = {};'.format(name, count-j, button[n_button]))
                    n_button += 1
            else:
                print('NET "{}" LOC = {};'.format(i, button[n_button]))
                n_button += 1
    print("//output")
    for i in output:
        if '[' in i:
            count = int(i[i.index('[')+1:-1])
            name = i[:i.index('[')]
            for j in range(count+1):
                print('NET "{}[{}]" LOC = {};'.format(name, count-j, bulb[n_output]))
                n_output += 1
        else:
            print('NET "{}" LOC = {};'.format(i, bulb[n_output]))
            n_output += 1
    print("//input&output")
    n_input = 0
    n_output = 0
    for i in input:
        if '[' in i:
            count = int(i[i.index('[')+1:-1])
            name = i[:i.index('[')]
            for j in range(count+1):
                print('NET "{}[{}]" IOSTANDARD = LVCMOS18;'.format(name, count-j))
                n_input += 1
        else:
            print('NET "{}" IOSTANDARD = LVCMOS18;'.format(i))
            n_input += 1
    if array.shape[0] >= 3:
        for i in input_button:
            if '[' in i:
                count = int(i[i.index('[')+1:-1])
                name = i[:i.index('[')]
                for j in range(count+1):
                    print('NET "{}[{}]" IOSTANDARD = LVCMOS18;'.format(name, count-j))
                    n_button += 1
            else:
                print('NET "{}" IOSTANDARD = LVCMOS18;'.format(i))
                n_button += 1
    for i in output:
        if '[' in i:
            count = int(i[i.index('[')+1:-1])
            name = i[:i.index('[')]
            for j in range(count+1):
                print('NET "{}[{}]" IOSTANDARD = LVCMOS18;'.format(name, count-j))
                n_output += 1
        else:
            print('NET "{}" IOSTANDARD = LVCMOS18;'.format(i))
            n_output += 1
    print("//input")
    n_input = 0
    for i in input:
        if '[' in i:
            count = int(i[i.index('[')+1:-1])
            name = i[:i.index('[')]
            for j in range(count+1):
                print('NET "{}[{}]" PULLDOWN;'.format(name, count-j))
                n_input += 1
        else:
            print('NET "{}" PULLDOWN;'.format(i))
            n_input += 1
    if array.shape[0] >= 3:
        for i in input_button:
            if '[' in i:
                count = int(i[i.index('[')+1:-1])
                name = i[:i.index('[')]
                for j in range(count+1):
                    print('NET "{}[{}]" PULLDOWN;'.format(name, count-j))
                    n_button += 1
            else:
                print('NET "{}" PULLDOWN;'.format(i))
                n_button += 1
