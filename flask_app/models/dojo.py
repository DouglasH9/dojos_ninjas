from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'

        results =  connectToMySQL('dojosninjas').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def add_new_dojo(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at) VALUES (%(nDojo)s, NOW(), NOW());"
        return connectToMySQL('dojosninjas').query_db(query,data)

    @classmethod
    def show_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s"
        return connectToMySQL('dojosninjas').query_db(query, data)


    @classmethod
    def show_dojo_ninjas(cls, data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojos.id = ninjas.dojos_id WHERE ninjas.dojos_id = %(id)s;"
        results = connectToMySQL('dojosninjas').query_db(query,data)
        ninjas = []
        for x in results:
            ninjas.append( x )
        return ninjas

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        return connectToMySQL('dojosninjas').query_db(query)

    @classmethod
    def delete_the_dojo(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        results = connectToMySQL('dojosninjas').query_db(query, data)
        return

