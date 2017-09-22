# Wharton SIMPL Users Application

A reusable application to define SIMPL Users

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

Change into the `simpl_users` subdirectory:

```bash
$ cd simpl_users
```

If you are working in Vagrant, this will be something like:

```bash
$ cd /vagrant/projects/simpl-users/simpl_users
```

```bash
$ py.test
```

## Model Schema

![](docs/models.png)

