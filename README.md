# Shilengae Backend Setup

How to setup Postgres Database on Linux.

Install PostgreSQL from PostgreSQL Apt Repository

    a) Add PostgreSQL Repository

Import the GPG repository key with the commands:
`sudo apt-get install wget ca-certificates`

`wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -`

Then, add the PostgreSQL repository by typing:
`` sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list' ``

    b) Update the Package List.
    ```sudo apt-get update```

    c)  Install PostgreSQL:
    `sudo apt-get install postgresql postgresql-contrib`

## Create Database

a) Enter an interactive Postgres session by typing:
`sudo -u postgres psql`

    b) ```CREATE DATABASE shilengae;```

    c) Create User for Database: ```CREATE USER shilengae_dev_user WITH PASSWORD ‘dev_password‘;```

    d) We set the default encoding to UTF-8, which is expected by Django:
    ```ALTER ROLE shilengae_dev_user SET client_encoding TO ‘utf8’;```

    e) Set a default transaction isolation scheme to “read commits”:
    ```ALTER ROLE shilengae_dev_user SET default_transaction_isolation TO ‘read committed’;```

    f) Finally, we set the time zone. By default, our Django project will be set to use UTC:
    ```ALTER ROLE shilengae_dev_user SET timezone TO ‘UTC’;```

    g) Give our database user access rights to the database that we created:
    ```GRANT ALL PRIVILEGES ON DATABASE shilengae TO shilengae_dev_user;```

    h) Give our shilengae_dev_user access to create test databases
    ```ALTER USER shilengae_dev_user CREATEDB;```

    i) Exit the SQL prompt to return to the postgres user shell session:
    ```\q```
