# Object Relational Mapping in Python

To interact with database, python makes use of obstractors
on top of the database that enables the programmer to interact with 
database directly using python classes.

# SQLAlchemy

It is an ORM for python that is inbuilt.

## To use SQLAlchemy

Install `sqldb` in your machine (Ubuntu 20.4)<br>
`sudo apt update`<br>
`sudo apt install mysql-server`<br>
Enable the service
`sudo service start mysql`<br>

## Configure MySQL

`sudo mysql`<br>
`> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password 'password'`<br>
`> exit`<hr>

# Run security script

`sudo mysql_secure_installation`

## Use MySQL

`sudo mysql`
