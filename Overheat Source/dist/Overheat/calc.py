

def avg_temp_gpu(gpu, array): #create array with average temps for each load
    temp = int(float(gpu[3]) )
    usage = float(gpu[2])
    if usage < float(0.25):
        array[0][1] = (array[0][1] + temp)//2
    elif usage < float(0.50):
        array[1][1] = (array[1][1] + temp)//2
    elif usage < float(0.75):
        array[2][1] = (array[2][1] + temp)//2
    elif usage < float(1.00):
        array[3][1] = (array[3][1] + temp)//2
    return array

def temp_gpu_compare(gpu, THRESHHOLDTEMP, array): #compare average temps collected
    temp = int(float(gpu[3]) )
    usage = float(gpu[2])
    warning = False
    if usage < float(0.25):
        if temp > (array[0][1] + THRESHHOLDTEMP):
            warning = True
    elif usage < float(0.50):
        if temp > (array[1][1] + THRESHHOLDTEMP):
            warning = True
    elif usage < float(0.75):
        if temp > (array[2][1] + THRESHHOLDTEMP):
            warning = True
    elif usage < float(1.00):
        if temp > (array[3][1] + THRESHHOLDTEMP):
            warning = True
    return warning

def max_temp_gpu(gpu):
    with open("max_gpu.txt", 'r') as f:
        max = f.readlines()
    if int(float(max[0])) < int(float(gpu[3])):
        max = gpu[3]
    else:
        max = int(float(max[0]))
    return max


