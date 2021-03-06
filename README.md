PIAsync: A simple, respectful management tool for Private Internet Access VPN configs
=====================================================================================

**PIAsync** aims to be a simple and lightweight tool that automaticaly manages configuration information in the [NetworkManager](https://developer.gnome.org/NetworkManager/stable/NetworkManager.html) data domain for the VPN servers operated by Private Internet Access.

In addition, **PIAsync** is respectful of your user and system configuration. It will never:

* Execute any external processes
* Write anything on the filesystem itself
* Require superuser privileges
* Require native packages to be installed

All interactions with NetworkManager are performed using the latter's D-Bus API, the way it should be.

### How Do I Use It?

1. Install **PIAsync** (you'll need Python 3 and ``pip``):
    ```
    $ pip3 install piasync
    ```
2. Run it:
    ```
    $ piasync -h
    usage: piasync [-h] [-n] [-a] [-v] username cert

    Maintains Network Manager connections for the Private Internet Access VPN
    servers

    positional arguments:
      username         Username to use for the VPN connections
      cert             Path to the PIA root CA

    optional arguments:
      -h, --help       show this help message and exit
      -n, --dry-run    Do not manipulate the NetworkManager configuration
      -a, --all-users  Make the connections available to all users
      -v, --verbose    Output debug information
    ```

### But Why?

Because PIA's [list of servers](https://www.privateinternetaccess.com/pages/network/) is quite large and setting up connections manually for each one would be tedious. There are automated solutions available, but tools that write config files without my informed consent upset me very much, so I wanted a tool that would _not_ do that.

### Shout Outs

* **PIASync** uses [jeepney](https://jeepney.readthedocs.io/en/latest/) for interacting with NetworkManager over D-Bus.
* The [requests](http://docs.python-requests.org/en/master/) library is used to download fresh configuration information from the PIA website.
* Lastly, [countrynames](https://pypi.org/project/countrynames/) is used to match the names given by PIA to its servers to a country code for the purpose of injecting a cute Emoji flag in the user-visible connection name.
