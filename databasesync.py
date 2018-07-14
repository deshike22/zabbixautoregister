import pymysql.cursors
import sys
import logging

logging.basicConfig(filename='/tmp/dbsync.log',level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def read_sql(filename):
    logging.debug("reading {} sql query".format(filename))
    data = open(filename, 'r')
    sql = " ".join(data.readlines())
    return sql


def get_db2_data(sql, connection):
    try:
        logging.debug("opening db server 2 connection")
        with connection.cursor() as cursor:
            sql = read_sql(sql)
            cursor.execute(sql)
            results = cursor.fetchall()
            logging.info("reading data from db server 2: SUCCESS")
    finally:
        connection.close()
        logging.debug("closing db server 2 connection")
    return results

def main():
    conndb1 = pymysql.connect(host='<db server 1>',
                                 user='',
                                 password='',
                                 db='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)


    conndb2 = pymysql.connect(host='<db server 2>',
                                 user='',
                                 password='',
                                 db='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    mappings = get_ecosys_data('<SQL file path>', connecosys)
    try:
        logging.debug("opening db server 1 connection")
        with connzabbix.cursor() as cursor:

            cursor.execute("TRUNCATE TABLE db1.table1")
            logging.debug("TRUNCATE TABLE db1.table1: SUCCESS")

            for result in mappings:
                sql = "INSERT INTO `db1.table1` (`<field1>`,`<field2>`) VALUES (%s,%s)"
                cursor.execute(sql,(result['<field1>'],result['<field2>']))
                logging.debug("Inserting values for {}".format(result['<field1>']))
        logging.info("db 2 data sync: SUCCESS")
        connzabbix.commit()
    finally:
        connzabbix.close()
        logging.debug("closing db server 1 connection")



if __name__ == "__main__":
    main()
