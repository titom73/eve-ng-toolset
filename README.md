# EVE-NG Python toolset

## About

Script repo to play with EVE-NG lab solution

## Scripts

- [__`eve-nodes-connector`__](./bin/eve-lab-manager): Manage management connection to running nodes:
  - list telnet ports,
  - connect to a host,
  - create iTerm2 profile
- [__`eve-lab-manager`__](./bin/eve-lab-manager): Support basic lab operations like *start*, *stop*, *export*, *wipe*

## Installation

### Pypi process

```shell
$ pip install git+https://github.com/titom73/eve-ng-toolset

# Run script
$ eve-nodes-connector -h
```

### GIT process

```shell
# Clone repository
$ git clone https://github.com/titom73/eve-ng-toolset.git
$ cd eve-ng-toolset

# Install requirements
$ pip install -r requirements.txt

# Run script
$ python bin/eve-nodes-connector -h
```

## Usage

### Options

Script can load information from SHELL environment variables

- __EVE_USERNAME__: replace usage of `--username`
- __EVE_PASSWORD__: replace usage of `--password`
- __EVE_SERVER__: replace usage of `--server`
- __EVE_LAB__: replace usage of `--lab`

### List Nodes with their telnet port

```bash
# Set password to not use --password trigger
$ export EVE_PASSWORD=<my_eve_password>

# Run script with saved EVE_PASSWORD
$ eve-node-connector -s < eve-ng -instance > -u < username > -l '/Users/Customers/Lab Topology - EOS EVPN'

+-------------------------------+--------------------+-------+-------------+
|            Topology           |     Node Name      |  Type | Telnet Port |
+-------------------------------+--------------------+-------+-------------+
| Lab Topology - EOS EVPN       |     spine-01       |  veos |    60505    |
| Lab Topology - EOS EVPN       |     spine-02       |  veos |    56609    |
| Lab Topology - EOS EVPN       |     leaf-02        |  veos |    33709    |
| Lab Topology - EOS EVPN       |     leaf-01        |  veos |    60005    |
+-------------------------------+--------------------+-------+-------------+
```

### Create a dynamic iTerm2 profile

```bash
# Set password to not use --password trigger
$ export EVE_PASSWORD=<my_eve_password>

# Run script with saved EVE_PASSWORD
$ eve-node-connector -s < eve-ng -instance > -u < username > -l '/Users/Customers/Lab Topology - EOS EVPN' --iterm
Getting information from < eve-ng -instance >
Create iTerm2 dynamic profile at /Users/< username >/Library/Application Support/iTerm2/DynamicProfiles/Lab Topology - EOS EVPN.json
```

### Connect to a node

```bash
# Set password to not use --password trigger
$ export EVE_PASSWORD=<my_eve_password>

# Run script with saved EVE_PASSWORD
$ eve-node-connector -s < eve-ng -instance > -u < username > -l '/Users/Customers/Lab Topology - EOS EVPN' -c spine-01
```

### Export configuration to EVE-NG

```bash
$ eve-lab-manager --export
+--------------------+--------+---------+
|     Node Name      | Action |  Result |
+--------------------+--------+---------+
|     spine-01       | export | success |
|     spine-02       | export | success |
|     leaf-01        | export | success |
|     leaf-02        | export | success |
+--------------------+--------+---------+
```

## Additional resources

- [Wax-Trax](https://github.com/Wax-Trax/beginner-scraps/blob/master/eve-nodes/eve-nodes.py)
- [mystacktrace](https://mystacktrace.com/2020/04/05/eve-ng-api/)

## License

[Apache 2](./LICENSE)
