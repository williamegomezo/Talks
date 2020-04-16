RES=`PGPASSWORD=$SQLALCHEMY_PASSWORD psql --host=db --username=$SQLALCHEMY_USERNAME --dbname=$SQLALCHEMY_DBNAME -lqt`

echo $RES;

if echo $RES | cut -d \| -f 1 | grep -qw $SQLALCHEMY_DBNAME; then
    echo 'db exists'
    # database exists
    # $? is 0
else
    PGPASSWORD=$SQLALCHEMY_PASSWORD psql --host=db --username=$SQLALCHEMY_USERNAME --dbname=$SQLALCHEMY_DBNAME /db-scripts/create_db.sql
    # ruh-roh
    # $? is 1
fi