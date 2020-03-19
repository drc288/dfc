# Deploy Flask Cli (dfc)

[![Build Status](https://travis-ci.com/drc288/dfc.svg?branch=master)](https://travis-ci.com/drc288/dfc)

This package creates a CLI to deploy packages like NGINX, MySQL, Firewall apart from being able to deploy projects based on Flask CLI, it verifies its architecture and makes a deployment on a server, this CLI aims to save time in the deployment of projects apart from being able to install packages on another server.

# Architecture

```
.
├── dfc_pkg
│   ├── alias_dfc.sh
│   ├── commands
│   │   ├── command_build.py
│   │   ├── command_deploy.py
│   │   ├── command_integrate.py
│   │   ├── controllers
│   │   │   ├── config_gunicorn.py
│   │   │   ├── config_nginx.py
│   │   │   └── make_file.py
│   │   ├── __init__.py
│   │   ├── modules
│   │   │   ├── compress.py
│   │   │   ├── create_connection.py
│   │   │   ├── __init__.py
│   │   │   ├── upload_files.py
│   │   │   └── verify_path.py
│   │   ├── mysql_server
│   │   │   ├── integrate_mysql.py
│   │   │   ├── setup_mysql.py
│   │   │   └── verify_mysql.py
│   │   ├── nginx_server
│   │   │   ├── install_nginx.py
│   │   │   └── setup_project.py
│   │   └── templates
│   │       ├── default
│   │       └── gunicorn.service
│   ├── __init__.py
│   └── main.py
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```
## Structure of the project to be verified
This will only be verified in the deploy command
```
.
├──  My_project
│   ├── api
│   ├── models
│   ├── web
│   │   ├── app.py
│   ├── dev
│   │   ├──requirements.txt
│   │   ├──setup_mysql_dev.sql
```

## CMD:Build
This command contains the different services that can be built on the remote server

### Build:Sub-commands
- **nginx**: Install nginx server on the remote server
- **mysql**: Install mysql server on the remote server
#### Examples:
****
**nginx**
``` bash
$ dfc deploy build nginx --ip 192.168.10.5 --path-key $HOME/.path/my_key --user-ssh my_user
```
**Output**
``` bash
Installing NGINX server
NGINX and PIP are installed
```
**mysql**
``` bash
$ dfc deploy build mysql --ip 192.168.10.5 --path-key $HOME/.path/my_key --user-ssh my_user
```
**Output**
``` bash
Starting the installation of mysql-server
MySQL has been installed
```
****
## CMD:Deploy
This command is in charge of deploying a project under the **NAFA** architecture, this means that you need the following files and directories. **Note** that if at any time you want to add a directory or file this will be taken into account and will only require the following files

### Sub-commands
- **project**:  Deploys an application under the NAFA architecture, this deployment contains the configuration of the app, the execution and the recreation of the gunicorn as a daemon, if you have a project in other path, specify it as follows: export **DFC_PATH**.

**As a base this project deploys the base with Nginx Server, Mysql-Server, Python, Vanilla JavaScript**

#### Examples:
****
**project**
``` bash
$ dfc deploy project --ip 192.168.10.10 --path-key --user-ssh admin 
```
or
``` bash
$ DFC_PATH=$HOME/my_project dfc deploy project --ip 192.168.10.10 --path-key --user-ssh admin 
```
**This will execute all the necessary independence for the project, which will be read in the requirements file** (requirement.txt)
****
## CMD:Integrate

This command makes the integration of the different services to the application possible, making the individual integration of each service

### Sub-Commands

- mysql-storage: Integrate the previously displayed project with the database, if you do not find the project displayed, it cannot be executed

### Examples
****
***mysql-storage*
``` bash
$ dfc integrate mysql-storage --ip 192.168.10.5 --path-key --user-ssh admin
```
**Output**
``` bash
Initialized the mysql integration with the project
Integration complete
```
