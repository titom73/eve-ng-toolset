# EVE-NG Python toolset

## About

Script repo to play with EVE-NG lab solution

## Scripts

- __eve-node-connector__:
  - List running nodes for a given topology and list dynamic telnet port.
  - Allow to start a telnet connection to a node

## Installation

### Pypi process

```shell
$ pip install git+https://github.com/titom73/eve-ng-toolset
```

### GIT process

```shell
# Clone repository
$ git clone https://github.com/titom73/eve-ng-toolset.git
$ cd eve-ng-toolset

# Install requirements
$ pip install -r requirements.txt

# Run script
$ python bin/eve-node-connector -h
```

## Usage

### List Nodes with their telnet port

```bash
# Set password to not use --password trigger
$ export EVE_PASSWORD=<my_eve_password>

# Run script with saved EVE_PASSWORD
$ python bin/eve-topo.py -s < eve-ng -instance > -u < username > -l '/Users/Customers/Lab Topology - EOS EVPN'

+-------------------------------+--------------------+-------+-------------+
|            Topology           |     Node Name      |  Type | Telnet Port |
+-------------------------------+--------------------+-------+-------------+
| Lab Topology - EOS EVPN       |     spine-01       |  veos |    60505    |
| Lab Topology - EOS EVPN       |     spine-02       |  veos |    56609    |
| Lab Topology - EOS EVPN       |     leaf-02        |  veos |    33709    |
| Lab Topology - EOS EVPN       |     leaf-01        |  veos |    60005    |
+-------------------------------+--------------------+-------+-------------+
```

### Connect to a node

```bash
# Set password to not use --password trigger
$ export EVE_PASSWORD=<my_eve_password>

# Run script with saved EVE_PASSWORD
$ python bin/eve-topo.py -s < eve-ng -instance > -u < username > -l '/Users/Customers/Lab Topology - EOS EVPN' -c spine-01
```

## Additional resources

- [Wax-Trax](https://github.com/Wax-Trax/beginner-scraps/blob/master/eve-nodes/eve-nodes.py)
- [mystacktrace](https://mystacktrace.com/2020/04/05/eve-ng-api/)

## License

[Apache 2](./LICENSE)
