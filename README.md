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

Copyright © 2018 The Wharton School,  The University of Pennsylvania 

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
