'''
Author:                         Marcus Nogueira
Date of latest revision:        12/11/2023
Purpose:                        Use PSUTIL library to get a feel for python using libraries
Resources:                      https://psutil.readthedocs.io/en/latest/index.html#cpu
                                https://www.tutorialspoint.com/configure-sendmail-with-gmail-on-ubuntu
'''

# Libary imports
import psutil

# Color Variables
GREEN = "\033[32m"  # Green text
RESET = "\033[0m"


# Function that fetches information using PSUTIL


def comp_times():
    cpu_times = psutil.cpu_times()  # Output: scputimes(user=5505.38, nice=1146.28, system=13870.9, idle=1422545.62, iowait=1083.21, irq=0.0, softirq=157.08, steal=0.0, guest=0.0, guest_nice=0.0)

    # Reorganize the tuple output of psutil into something useful and printable.
    time_info = {
        "User mode Time": cpu_times.user,
        "Kernel mode Time": cpu_times.system,
        "System Idle Time": cpu_times.idle,
        "User Priority Processes Time": cpu_times.nice,
        "I/O Wait Time": cpu_times.iowait,
        "Servicing Hardware Interrupts Time": cpu_times.irq,
        "Servicing Software Interrupts Time": cpu_times.softirq,
        "Virtualized OS Time": cpu_times.steal,
        "Virtual CPU for Guest OS Time": cpu_times.guest
    }
    return time_info


if __name__ == "__main__":
    info = comp_times()

    with open("psutils-output.txt", "w") as file:
        for key, value in info.items():
            print(f'{GREEN}{key}{RESET}: {value} seconds | {value / 60:.2f} mins')
            file.write(f'{key}: {value} seconds | {value / 60:.2f} mins\n')

    file.close()
