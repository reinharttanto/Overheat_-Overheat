
import grab
import calc
import write
import get_stats
from tkinter import *
from tkinter import messagebox
import time
import datetime


THRESHHOLDTEMP_GPU = 20 #thresh hold temp for gpu


def gpu_name():
    gpu = get_stats.get_gpu()
    gpu_name = gpu[0][1]
    return gpu_name

cpu = []
gpu = []
gpu_list = []
cpu_list = []
temp_gpu_array = grab.grab_prev_avg_temps()
loops = 0

gpu = get_stats.get_gpu()

message1 = str("App successfuly started, Components Detected: " + gpu[1] + ", you can close this window.") #confirm start of program
messagebox.showinfo("Overheat", message1)


while True:

    for i in range(10):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %h:%M:%S")

    loops += 1
    cpu = get_stats.get_cpu() #get and write data into txt document
    gpu = get_stats.get_gpu()
    write.write(cpu, "cpu.txt")
    write.write(gpu, "gpu.txt")

    if calc.temp_gpu_compare(gpu, THRESHHOLDTEMP_GPU, temp_gpu_array): #when overheat generate alert
        warn_datetime = now.strftime("%d/%m/%Y %h:%M:%S")
        message2 = str(gpu[1] + " is experiencing abnormal temperatures, we recommend to get it diagnosed. You can ignore this if it appears for the first time when running a substantial load. Please run software again after closing this alert. Time of error: " + warn_datetime)
        messagebox.showinfo("Overheat", message2)
        write.warn_report(gpu[1], warn_datetime, gpu[3])
        break

    temp_gpu_array = calc.avg_temp_gpu(gpu, temp_gpu_array) #Average temperatures
    write.avg_temp_doc_gpu(temp_gpu_array)
    max = calc.max_temp_gpu(gpu)
    write.max_temp_gpu(max)

    print(loops)
    time.sleep(5) #loop runse every 5 seconds