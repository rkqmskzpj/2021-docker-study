#!/bin/sh

# MySQLが立ち上がるまで待つ
echo "Waiting for mysql to start..."
until mysqladmin ping -h$MYSQL_HOST -u$MYSQL_USER -p$MYSQL_PASSWORD --silent; do
    sleep 1
done

cd /app/migrations && alembic upgrade head

# アプリケーションの起動
cd /app && uvicorn main:app --host=0.0.0.0 --reload