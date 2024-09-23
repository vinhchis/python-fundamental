# Reading Json and Install Packages with Pip
> `requests` package - HTTP requests
Data from internet:
    - HTML
    - Raw data
    - ...

***json format = mix of (lists and dictionaries)***

## Pip
> pip - package manager in python

``` bash
    pip3 --version
    pip3 requests
```
`pip3` attach with **python3**

[request package](https://pypi.org/project/requests/)
```bash
    # install
    sudo pacman -S python-requests
    # remove
    sudo pacman -Rs python-requests
```
> arch linux, bảo vệ môi trường python hệ thống

[Open-Notify-Api](http://open-notify.org/Open-Notify-API/)

http://api.open-notify.org/astros.json?

# Create a Python Virtual Environment

### Global

```bash
    pip install requests
```

## Python Virtual Environment (Locally)
> difference version with difference package

### create a `venv` variable enviroment 
```bash
    python -m venv 'venv'
``` 
***create a venv folder*** 

### activate/deactivate virtual enviroment
*Activate*
```bash
    source <venv>/bin/activate
```

After running, `(venv)` in front of the command prompt.

*Deactivate*
```bash
    deactivate
```