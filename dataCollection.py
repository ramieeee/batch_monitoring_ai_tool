import os
import psutil
import time
import pandas as pd

data = {'cpu1': [],
        'cpu2': [],
        'cpu3': [],
        'cpu4': [],
        'cpu5': [],
        'cpu6': [],
        'cpu7': [],
        'cpu8': [],
        'percent': [],
        'used': [],
        'active': [],
        'buffers': [],
        'cached': [],
        'shared': []
}
df = pd.DataFrame(data)
if 'resource_data.csv' not in os.listdir('./'):
    df.to_csv('./resource_data.csv')

# 8 CPU-s
for i in range(0, 10000):
    cpu = psutil.cpu_percent(interval=None, percpu=True)

    cpu.append(psutil.virtual_memory().percent)
    cpu.append(psutil.virtual_memory().used)
    cpu.append(psutil.virtual_memory().active)
    cpu.append(psutil.virtual_memory().buffers)
    cpu.append(psutil.virtual_memory().cached)
    cpu.append(psutil.virtual_memory().shared)

    df2 = pd.DataFrame([cpu], columns=['cpu1', 'cpu2', 'cpu3', 'cpu4', 'cpu5', 'cpu6','cpu7','cpu8','percent','used','active','buffers','cached','shared'])
    df = pd.concat([df, df2], ignore_index=True)
    print(cpu)
    time.sleep(0.5)
print(df)
df.to_csv('./resource_data.csv')