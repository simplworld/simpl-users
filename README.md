# Simpl Users Application

A reusable application to define Simpl Users

[![Build Status](https://travis-ci.com/simplworld/simpl-users.svg?token=cyqpBgqLC1o8qUptfcpE&branch=master)](https://travis-ci.com/simplworld/simpl-users)

## Getting Started (assumes working in vagrant)

```bash
$ vagrant ssh
$ mkvirtualenv simpl-users
$ add2virtualenv /vagrant/projects/simpl-users
$ cd /vagrant/projects/simpl-users
```

Install requirements:

```bash
$ pip install -r requirements.txt
```

### Running tests with py.test

```bash
$ python runtests.py
```

## Model Schema

![](docs/models.png)

