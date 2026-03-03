import datetime
import subprocess

boot_time_str = "2025-08-03 14:54:48"
# boot_time_str = "2025-08-02 23:16:00"

dmesg_timestamp = [ 
                  273.680537,
                  205944.341178,
                  205949.161849
]
# dmesg_timestamp = dmesg_timestamp1


print('ЗАПУСКАТЬ надо RPi4 !!!')
print('Start.\n')
boot_time = datetime.datetime.strptime(boot_time_str, "%Y-%m-%d %H:%M:%S")
print(f'Время загрузки: {boot_time}')
for iTimestamp in dmesg_timestamp:
    error_time = boot_time + datetime.timedelta(seconds=iTimestamp)
    print(f"Время ошибки #: {error_time}")
print('\nDone.')

# Для uptime -s
uptime_s = subprocess.check_output(['uptime', '-s'], text=True).strip()

# Для who -b (с извлечением времени загрузки)
who_b_output = subprocess.check_output(['who', '-b'], text=True).strip()
who_b = who_b_output.split()[-2] + ' ' + who_b_output.split()[-1]

print("Ubuntu Dell XPS -> uptime -s:", uptime_s)
print("Ubuntu Dell XPS -> who -b:", who_b)