from sqlalchemy import create_engine, text


class WorksData(object):
    def __init__(self):
        self._engine=create_engine("sqlite:///database.db", echo = True)

    """Возвращает список словарей с информацией по авторам с их id, name,
    birth, и death"""
    def get_persons(self):
        sql = text("SELECT Persons.id AS id, Persons.name as name, Persons.date_of_birth AS birth, Persons.date_of_death"
                   " AS death  FROM Persons ORDER BY name;")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret

    """Возвращает строку со списком стран принадлежности автора по его id"""
    def get_countries(self, person_id):
        sql = text("SELECT GROUP_CONCAT(Countries.country_name, \", \") AS Countries FROM CountriesPersons JOIN Countries "
                   "ON CountriesPersons.country_id = Countries.id WHERE CountriesPersons.person_id = " + str(person_id) +" ;")
        sql_result = self._engine.execute(sql)
        for record in sql_result:
            dictionary = dict(record)
        return dictionary["Countries"]



    """Возвращает строку с именем автора по его id"""
    def get_author_name(self, person_id):
        sql = text("SELECT * FROM Persons WHERE id="+str(person_id) +";")
        sql_result = self._engine.execute(sql)
        for auth in sql_result:
            res = dict(auth)
        return res


    """Возвращает список  с типами и произведениями автора, """
    def get_works(self, author_id):
        sql = text("SELECT Types.type_name AS type, GROUP_CONCAT(Works.title, \", \") as titles "
                   "FROM PersonsWorks JOIN Works ON PersonsWorks.work_id = Works.id JOIN Types ON Works.type = Types.type_id "
                   "WHERE PersonsWorks.person_id=" + str(author_id) + " GROUP BY type")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
            return ret

    def get_work(self):
        sql = text("SELECT * FROM Works JOIN Types ON Works.type = Types.type_id ORDER BY type_name, title;")
        sql_result = self._engine.execute(sql)
        res = []
        for auth in sql_result:
            res.append(dict(auth))
        return res

    def get_types(self):
        sql = text("SELECT * FROM Types ORDER BY type_name;")
        sql_result = self._engine.execute(sql)
        res = []
        for i in sql_result:
            res.append(dict(i))
        return res

    def get_worktypes(self):
        sql = text("SELECT Works.id as id, Works.name as name, Types.type_name as type from Works JOIN Types on Works.type = Types.type_id ORDER BY type, name")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret



    def get_work_name(self, work_id):
        sql = text("SELECT * FROM Works WHERE id="+str(work_id) +";")
        sql_result = self._engine.execute(sql)
        for auth in sql_result:
            res = dict(auth)
        return res


    def get_countries_works(self, work_id):
        sql = text("SELECT GROUP_CONCAT(Countries.country_name, \", \") AS Countries FROM CountriesWorks JOIN Countries "
                   "ON CountriesWorks.country_id = Countries.id WHERE CountriesWorks.work_id = " + str(work_id) +" ;")
        sql_result = self._engine.execute(sql)
        for record in sql_result:
            dictionary = dict(record)
        return dictionary["Countries"]

    def get_authors(self, work_id):
        sql = text("SELECT GROUP_CONCAT(Persons.name, \", \") as persons "
                   "FROM PersonsWorks  JOIN Persons ON Persons.id = PersonsWorks.person_id "
                   "WHERE PersonsWorks.work_id=" + str(work_id) + ";")
        sql_result = self._engine.execute(sql)
        for i in sql_result:
            ret = dict(i)
            return ret

#ТЕСТИРОВАНИЕ:
#bd = WorksData()
#print(bd.get_persons())
#print (bd.get_countries(6))
#print (bd.get_work())
#print (bd.get_author_name(1))
