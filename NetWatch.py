#!/usr/bin/python3

"""

__author__ = "ChrishSec"
__copyright__ = "Copyright (C) 2024 ChrishSec"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"

Website: https://ChrishSec.com
GitHub: https://github.com/ChrishSec
Twitter: https://twitter.com/ChrishSec

"""

import re
import sys
import time
import pytz
import random
import argparse
import subprocess
from datetime import datetime

log_file = 'access.log'
previous_connections = set()

def colorize(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def random_color_code():
    return random.randint(31, 37)

def log_error(error_msg):
    error_msg_colored = colorize(error_msg, '91')
    print(f"\n ERROR: {error_msg_colored}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Monitor network connections and log new connections.')
    parser.add_argument('-timezone', help='Specify the timezone (e.g., "SG")', required=True)
    args = parser.parse_args()

    country_name = args.timezone

    try:
        while True:
            result = subprocess.run(['netstat', '-an'], stdout=subprocess.PIPE, text=True, check=True)
            connections = re.findall(r'(\w+)\s+(\d+)\s+(\d+)\s+(\d+\.\d+\.\d+\.\d+:\d+)\s+(\d+\.\d+\.\d+\.\d+:\d+)\s+(\w+)', result.stdout)

            with open(log_file, 'a') as f:
                for proto, recv_q, send_q, local_address, foreign_address, state in connections:
                    if local_address not in previous_connections or foreign_address not in previous_connections:
                        time_zone = pytz.country_timezones.get(country_name, [])[0]
                        if time_zone:
                            utc_now = datetime.utcnow()
                            local_time = utc_now.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(time_zone))
                            formatted_time = local_time.strftime("\033[91m%b %d, %Y - %I:%M:%S %p\033[0m")

                            proto_colored = colorize(proto, '32')
                            recv_q_colored = colorize(recv_q, '32')
                            send_q_colored = colorize(send_q, '32')
                            local_address_colored = colorize(local_address, '32')
                            foreign_address_colored = colorize(foreign_address, '32')

                            if state == 'State:':
                                state_colored = colorize(state, '32')
                            elif state == 'ESTABLISHED':
                                state_colored = colorize(state, '31')
                            else:
                                state_colored = colorize(state, '33')

                            developed_by_chrishsec = colorize("DEVELOPED BY >> ChrishSec.com", random_color_code())
                            developed_by_chrishsec2 = colorize("[+]", '31')

                            log_data = f"\n {developed_by_chrishsec} \n\n {developed_by_chrishsec2} New Connection Established ↓\n\n \033[32mConnection Time: {formatted_time}\033[0m\n \033[32mProto: {proto_colored}\033[0m\n \033[32mRecv-Q: {recv_q_colored}\033[0m\n \033[32mSend-Q: {send_q_colored}\033[0m\n \033[32mLocal Address: {local_address_colored}\033[0m\n \033[32mForeign Address: {foreign_address_colored}\033[0m\n \033[32mState: {state_colored}\033[0m"

                            print(log_data)
                            print("\n------------")

                            f.write(log_data + '\n')

                            previous_connections.add(local_address)
                            previous_connections.add(foreign_address)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n Exiting.")
        sys.exit(0)
    except subprocess.CalledProcessError as e:
        log_error(f" [!] Failed to run NetWatch.py Error: {e}")
    except Exception as e:
        log_error(f" [!] An error occurred: {e}")
