def cpu_array(file): #grab record files
    with open(file, 'r') as f:
        line_count = 0
        for line in file:
            if line != "\n":
                line_count += 1
            array = []
        for i, line in enumerate(f):
            if i < (line_count + 1):
                array.append(line.strip())
    return array

def gpu_array(file):
    with open(file, 'r') as f:
        line_count = 0
        for line in file:
            if line != "\n":
                line_count += 1
            array = []
        for i, line in enumerate(f):
            if i in line_count:
                array.append(line.strip())
    return array

def grab_prev_avg_temps(): #grab previous avg temps
    with open("25.txt", 'r') as f: #grabing previous values (if not yet then files should have 0)
        value25 = f.readlines()
    with open("50.txt", 'r') as f:
        value50 = f.readlines()
    with open("75.txt", 'r') as f:
        value75 = f.readlines()
    with open("100.txt", 'r') as f:
        value100 = f.readlines()
    total_temp_gpu_array = ["0to25", 0], ["25to50", 0],["50to75", 0],["75to100", 0]
    total_temp_gpu_array[0][1] = int(value25[0])
    total_temp_gpu_array[1][1] = int(value50[0])
    total_temp_gpu_array[2][1] = int(value75[0])
    total_temp_gpu_array[3][1] = int(value100[0])
    return total_temp_gpu_array
    

    