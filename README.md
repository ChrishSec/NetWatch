## NetWatch

`NetWatch` is a Python script designed to monitors network connections and logs new connections. It displays information about the established connections, such as connection time, protocol, receive queue, send queue, local and foreign addresses, and connection state.

Note: This script utilizes the netstat command to gather network connection information. Please ensure that the netstat command is available on your system.

### Requirements
- Python 3.x
- Unix-like operating system (tested on Ubuntu 20.04)

### Usage

1. Clone the repository:

```git clone https://github.com/ChrishSec/NetWatch.git```

2. Install the required dependencies:

```pip3 install -r requirements.txt```

3. Run the script:

```python3 NetWatch.py -timezone <YOUR_TIMEZONE>```

Replace ```<YOUR_TIMEZONE>``` with the desired timezone (e.g., "SG").

### Screenshots

Coming Soon

![Screenshot 1](screenshots/screenshot_1.png)
![Screenshot 2](screenshots/screenshot_2.png)

## Disclaimer

This script is intended for educational and research purposes only. Use it at your own risk. The author is not responsible for any damage caused by the use or misuse of this script.

## License

This script is released under the GNU General Public License v3.0. Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

## Author

This script was developed by [ChrishSec](https://github.com/ChrishSec). Feel free to fork, modify, and distribute it. If you have any questions or suggestions, please reach out to the author on [Telegram](https://t.me/ChrishSec).