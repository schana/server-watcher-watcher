# server-watcher-watcher

For those pesky things that prevent your server from starting if the connection to their server fails.

## Setup

1. [Install Python 3](https://www.python.org/downloads/windows/)
1. Download this repository and unzip it
1. Install dependencies by running `pip3 install -r requirements.txt`
1. Add `127.0.0.1 clauzier.dev` to the end of `C:\Windows\System32\drivers\etc\hosts`
1. Run the webserver with `python3 main.py`

The program is configured to attempt the request, but won't crash your server if that attempt fails.
If you don't care about having your data tracked, change `should_forward = True` to `should_forward = False` in `main.py`
