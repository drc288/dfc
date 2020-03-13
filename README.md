# Deploy Flask Cli (dfc)

[![Build Status](https://travis-ci.com/drc288/dfc.svg?branch=master)](https://travis-ci.com/drc288/dfc)

This package creates a command line interpreter for Flask CLI, which verifies its architecture and makes a deploy in a server, this project aims to save time in the deployment and development of applications.

# Architecture

```
.
├── dfc_pkg
│   ├── deploy
│   │   ├── controllers
│   │   │   ├── config_gunicorn.py
│   │   │   ├── config_nginx.py
│   │   │   └── make_file.py
│   │   ├── modules
│   │   │   ├── compress.py
│   │   │   ├── create_connection.py
│   │   │   ├── upload_files.py
│   │   │   └── verify_path.py
│   │   ├── mysql_server
│   │   │   ├── setup_mysql.py
│   │   │   └── verify_mysql.py
│   │   ├── nginx_server
│   │   │   └── setup_nginx.py
│   │   ├── templates
│   │   |   ├── default
│   │   |   └── gunicorn.service
|   |   └── main_dfc.py
│   ├── alias_dfc.sh
│   └── main.py
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## Commands

## -- deploy -- 
It contains the commands to make a deploy of an application from 0, this must already have the Flask Cli architecture

### Sub-commands
- deploy-project:  Deploys an application under the NAFA architecture, this deployment
  contains the configuration of the app, the execution and the recreation of
  the gunicorn as a daemon, if you have a project in other path, specify it
  as follows: export **DFC_PATH**.
  
#### Examples:

**deploy-project**
``` bash
$ dfc deploy deploy-project --ip 192.168.10.10 --path-key --user-ssh admin
```

## -- config-server --
It contains the individual settings for each service, for example running nginx, mysql or setting up a haproxy

### Sub-commands
- run-nginx: Default installation of **nginx** on a server
- run-mysql: Default installation of **mysql** on a server

#### Examples:
**run-nginx**
``` bash
$ dfc config-server run-nginx --ip 192.168.10.10 --path-key --user-ssh admin 
```
**run-mysql**
``` bash
$ dfc config-server run-mysql --ip 192.168.10.10 --path-key --user-ssh admin
```
