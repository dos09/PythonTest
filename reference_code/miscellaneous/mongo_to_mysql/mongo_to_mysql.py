from subprocess import call
# the port can be part of the host option:
# --host=127.0.0.1:27017
mongo_export = ('mongoexport -v -d mytest --host=localhost --port=27017 '
                '-c orcs --type=csv  --fieldFile=./orcs.cols > orcs.csv')
code = call(mongo_export, shell=True)
print('mongo export code:', code)

mysql_import = ('mysql --host=localhost --port=3306 --user=USERNAME '
                '--password=PASSWORD --database=DBNAME < load_orcs.sql')
code = call(mysql_import, shell=True)
print('mysql import code:', code)