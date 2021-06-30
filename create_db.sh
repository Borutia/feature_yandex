#!/bin/bash
psql -c "CREATE USER reports_app WITH PASSWORD 'secret';"
psql -c "ALTER ROLE reports_app SET client_encoding to 'utf8';"
psql -c "ALTER ROLE reports_app SET default_transaction_isolation TO 'read committed';"
psql -c "ALTER ROLE reports_app SET timezone to 'UTC';"
psql -c "CREATE DATABASE reports_app_db WITH OWNER reports_app;"
psql -c "ALTER USER reports_app CREATEDB;"