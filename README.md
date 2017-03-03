# Wharton SIMPL Users Application

A reusable application to define SIMPL Users

## Getting Started

Make sure you are working in a virtual environment of some sort (e.g. 'virtualenv').

If you are working in Vagrant you are working in Vagrant using virtualenv, add simpl-users to the code path:

```bash
$ add2virtualenv /vagrant/html/simpl-users
```

If you are working in Vagrant:

```bash
$ cd /vagrant/html/simpl-users
```

Install requirements:

```bash
$ pip install -r requirements.txt
```

### Running tests with py.test

Change into the `simpl_users` subdirectory:

```bash
$ cd simpl_users
```

If you are working in Vagrant, this will be something like:

```bash
$ cd /vagrant/html/simpl-users/simpl_users
```

```bash
$ py.test
```

## Model Schema

![](docs/models.png)

