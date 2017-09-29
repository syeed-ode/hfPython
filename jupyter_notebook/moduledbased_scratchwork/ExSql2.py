from moduledbased_scratchwork.DBcm2 import UseDatabase

dbconfig = {   'host': '127.0.0.1'
            ,  'user': 'vsearch'
           }

with UseDatabase(dbconfig) as cursor:
    _SQL = """insert into log
              (phrase, letters, ip, browser_string, results)
              values
              (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, ('galaxy', 'xyz', '127.0.0.1', 'Chrome', "{'x', 'y'}"))