
'''
This program calculates the value required to be put in the timer register counter
to achieve the desired target frequency under the given main clock frequency, while
taking into account the prescaler value choosen.

Author: Edwin Mwiti
Date: 31st August 24
'''

from tabulate import tabulate

print("="*40)
print("Timer Count Solver (AVR, SAM, ARM)")
print("="*40)

input_frequency = eval(input("Enter main clock frequency(Hz): "))
target_frequency = eval(input("Enter target frequency(Hz): "))
timer_bit_size = eval(input("Enter timer bit size: "))

print("="*20)
print("Result")
print("="*20)

print("Main Clock(Hz): " + str(input_frequency))
print("Target frequency(Hz): " + str(target_frequency))
print("\n")

eight_bit_good = ""
sixteen_bit_good = ""
thirty_two_bit_good = ""

result = []
count_list = []
bit_size_list = []

psk1_list_vals = []
psk8_list_vals = []
psk64_list_vals = []
psk256_list_vals = []
psk1024_list_vals = []

prescaler_values = [1, 8, 64, 256, 1024] # TODO: Add ARM prescaler values
for psk_val in prescaler_values:
    target_timer_count = ((input_frequency / psk_val) / target_frequency) - 1
    result.append(psk_val)
    result.append(target_timer_count)

# separate the timer counts 
for i in range(0, len(result)):
    if i % 2 != 0:
       count_list.append(result[i])

psk1_list_vals.append(prescaler_values[0])
psk1_list_vals.append(count_list[0])

psk8_list_vals.append(prescaler_values[1])
psk8_list_vals.append(count_list[1])

psk64_list_vals.append(prescaler_values[2])
psk64_list_vals.append(count_list[2])

psk256_list_vals.append(prescaler_values[3])
psk256_list_vals.append(count_list[3])

psk1024_list_vals.append(prescaler_values[4])
psk1024_list_vals.append(count_list[4])

# check if the calculated value can fit into the registers
if timer_bit_size == 8:
    sixteen_bit_good = "-"
    thirty_two_bit_good = "-"
    if psk1_list_vals[1] < 256:
        eight_bit_good = "OK"
    else:
        eight_bit_good = "OVFLOW"

    psk1_list_vals.append(eight_bit_good)
    psk1_list_vals.append(sixteen_bit_good)
    psk1_list_vals.append(thirty_two_bit_good)

    if psk8_list_vals[1] < 256:
        eight_bit_good = "OK"
    else:
        eight_bit_good = "OVFLOW"

    psk8_list_vals.append(eight_bit_good)
    psk8_list_vals.append(sixteen_bit_good)
    psk8_list_vals.append(thirty_two_bit_good)

    if psk64_list_vals[1] < 256:
        eight_bit_good = "OK"
    else:
        eight_bit_good = "OVFLOW"

    psk64_list_vals.append(eight_bit_good)
    psk64_list_vals.append(sixteen_bit_good)
    psk64_list_vals.append(thirty_two_bit_good)

    if psk256_list_vals[1] < 256:
        eight_bit_good = "OK"
    else:
        eight_bit_good = "OVFLOW"

    psk256_list_vals.append(eight_bit_good)
    psk256_list_vals.append(sixteen_bit_good)
    psk256_list_vals.append(thirty_two_bit_good)

    if psk1024_list_vals[1] < 256:
        eight_bit_good = "OK"
    else:
        eight_bit_good = "OVFLOW"

    psk1024_list_vals.append(eight_bit_good)
    psk1024_list_vals.append(sixteen_bit_good)
    psk1024_list_vals.append(thirty_two_bit_good)
    

if timer_bit_size == 16:
    eight_bit_good = "-"
    thirty_two_bit_good = "-"
    if psk1_list_vals[1] < 65536:
        sixteen_bit_good = "OK"
    else:
        sixteen_bit_good = "OVFLOW"

    psk1_list_vals.append(eight_bit_good)
    psk1_list_vals.append(sixteen_bit_good)
    psk1_list_vals.append(thirty_two_bit_good)

    if psk8_list_vals[1] < 65536:
        sixteen_bit_good = "OK"
    else:
        sixteen_bit_good = "OVFLOW"

    psk8_list_vals.append(eight_bit_good)
    psk8_list_vals.append(sixteen_bit_good)
    psk8_list_vals.append(thirty_two_bit_good)

    if psk64_list_vals[1] < 65536:
        sixteen_bit_good = "OK"
    else:
        sixteen_bit_good = "OVFLOW"

    psk64_list_vals.append(eight_bit_good)
    psk64_list_vals.append(sixteen_bit_good)
    psk64_list_vals.append(thirty_two_bit_good)

    if psk256_list_vals[1] < 65536:
        sixteen_bit_good = "OK"
    else:
        sixteen_bit_good = "OVFLOW"

    psk256_list_vals.append(eight_bit_good)
    psk256_list_vals.append(sixteen_bit_good)
    psk256_list_vals.append(thirty_two_bit_good)

    if psk1024_list_vals[1] < 65536:
        sixteen_bit_good = "OK"
    else:
        sixteen_bit_good = "OVFLOW"

    psk1024_list_vals.append(eight_bit_good)
    psk1024_list_vals.append(sixteen_bit_good)
    psk1024_list_vals.append(thirty_two_bit_good)

if timer_bit_size == 32:
    eight_bit_good = "-"
    sixteen_bit_good = "-"
    if psk1_list_vals[1] < 4294967296:
        thirty_bit_good = "OK"
    else:
        thirty_bit_good = "OVFLOW"

    psk1_list_vals.append(eight_bit_good)
    psk1_list_vals.append(sixteen_bit_good)
    psk1_list_vals.append(thirty_two_bit_good)

    if psk8_list_vals[1] < 4294967296:
        thirty_bit_good = "OK"
    else:
        thirty_bit_good = "OVFLOW"

    psk8_list_vals.append(eight_bit_good)
    psk8_list_vals.append(sixteen_bit_good)
    psk8_list_vals.append(thirty_two_bit_good)

    if psk64_list_vals[1] < 4294967296:
        thirty_bit_good = "OK"
    else:
        thirty_bit_good = "OVFLOW"

    psk64_list_vals.append(eight_bit_good)
    psk64_list_vals.append(sixteen_bit_good)
    psk64_list_vals.append(thirty_two_bit_good)

    if psk256_list_vals[1] < 4294967296:
        thirty_bit_good = "OK"
    else:
        thirty_bit_good = "OVFLOW"

    psk256_list_vals.append(eight_bit_good)
    psk256_list_vals.append(sixteen_bit_good)
    psk256_list_vals.append(thirty_two_bit_good)

    if psk1024_list_vals[1] < 4294967296:
        thirty_bit_good = "OK"
    else:
        thirty_bit_good = "OVFLOW"

    psk1024_list_vals.append(eight_bit_good)
    psk1024_list_vals.append(sixteen_bit_good)
    psk1024_list_vals.append(thirty_two_bit_good)

table = [['Prescaler', 'Target Timer count', '8-bit', '16-bit', '32-bit'], psk1_list_vals, psk8_list_vals, psk64_list_vals, psk256_list_vals, psk1024_list_vals]
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


