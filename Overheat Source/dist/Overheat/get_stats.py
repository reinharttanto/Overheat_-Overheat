import GPUtil
import psutil


def get_cpu():
    list_cpu = []
    cpu_load = psutil.cpu_percent()
    cpu_temp = 0
    list_cpu.append((cpu_load, cpu_temp))
    return list_cpu



def get_gpu():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id # get the GPU id
        gpu_name = gpu.name # name of GPU
        gpu_load = f"{gpu.load}"# get % percentage of GPU usage of that GPU
        gpu_temperature = f"{gpu.temperature}" # get GPU temperature in Celsius
        list_gpus.append(gpu_id)
        list_gpus.append(gpu_name)
        list_gpus.append(gpu_load)
        list_gpus.append(gpu_temperature)
    return list_gpus
