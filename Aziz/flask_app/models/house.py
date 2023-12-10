from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE



class House:
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.type=data['type']
        self.mortage_validation=data['mortage_validation']
        self.mortage_monthly=data['mortage_monthly']
        self.location=data['location']
        self.price=data['price']
        self.bathroom=data['bathroom']
        self.beds=data['beds']
        self.surface=data['surface']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.owner=''
        self.owner_phone_number=''
        self.owner_email=''
        self.pic=''
    
    @classmethod
    def create_a_house(cls,data):
        query="""INSERT INTO houses 
        (user_id,type,mortage_validation,mortage_monthly,location,price,bathroom,beds,surface)
        VALUES
        (%(user_id)s,%(type)s,%(mortage_validation)s,%(mortage_monthly)s,%(location)s,%(price)s,%(bathroom)s,%(beds)s,%(surface)s);"""
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def put_photos_for_the_house(cls,data):
        query="INSERT INTO pics (house_id,path) VALUES (%(house_id)s,%(path)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    


    @classmethod
    def select_one_house_with_pics_and_owner(cls,data):
        query="""SELECT houses.*,first_name,last_name,email,phone_number FROM houses JOIN users ON
            houses.user_id=users.id WHERE houses.id=%(id)s;
            SELECT path FROM pics WHERE house_id=%(house_id)s;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result[0]
    
    @classmethod
    def select_all_houses_with_pic(cls):
        query="SELECT houses.*,path FROM houses JOIN pics ON houses.id=pics.house_id;"
        results=connectToMySQL(DATABASE).query_db(query)
        houses=[]
        for house in results:
            row= cls(house)
            row.pic=house['path']
            houses.append(row)
        return houses
    
    @classmethod
    def select_houses_with_crita(cls,data):
        query = "SELECT houses.*, path FROM houses JOIN pics ON houses.id = pics.house_id WHERE "
        criteria= {key: value for key, value in data.items() if value}
        conditions = []

        if 'min_price' in criteria:
            conditions.append(f"houses.price >= {criteria['min_price']}")

        if 'max_price' in criteria:
            conditions.append(f"houses.price <= {criteria['max_price']}")

        if 'min_surface' in criteria:
            conditions.append(f"houses.surface >= {criteria['min_surface']}")

        if 'max_surface' in criteria:
            conditions.append(f"houses.surface <= {criteria['max_surface']}")

        if 'min_beds' in criteria:
            conditions.append(f"houses.beds >= {criteria['min_beds']}")

        if 'max_beds' in criteria:
            conditions.append(f"houses.beds <= {criteria['max_beds']}")

        if 'min_bathroom' in criteria:
            conditions.append(f"houses.bathroom >= {criteria['min_bathroom']}")

        if 'max_bathroom' in criteria:
            conditions.append(f"houses.bathroom <= {criteria['max_bathroom']}")

        if 'type' in criteria:
            conditions.append(f"houses.type = '{criteria['type']}'")

        if 'location' in criteria:
            conditions.append(f"houses.location = '{criteria['location']}'")

        if 'mortage_validation' in criteria:
            conditions.append(f"houses.mortage_validation = {criteria['mortage_validation']}")
        
        if 'min_mortage_monthly' in criteria:
            conditions.append(f"houses.mortage_monthly >= {criteria['min_mortage_monthly']}")
        
        if 'max_mortage_monthly' in criteria:
            conditions.append(f"houses.mortage_monthly <= {criteria['max_mortage_monthly']}")

        if conditions:
            query += " AND ".join(conditions) +";"

        results = connectToMySQL(DATABASE).query_db(query)
        
        houses = []
        for house in results:
            row = cls(house)
            row.pic = house['path']
            houses.append(row)

        return houses


    @classmethod
    def update_a_house_with_its_picture(cls,data):
        query="""UPDATE houses
                    JOIN pics ON houses.id = pics.house_id
                    SET
                        houses.type =%(type)s,
                        houses.mortage_validation = %(mortage_validation)s,
                        houses.mortage_monthly = %(mortage_monthly)s,
                        houses.location = %(location)s,
                        houses.price = %(price)s,
                        houses.bathroom = %(bathroom)s,
                        houses.beds = %(beds)s,
                        houses.surface = %(surface)s,
                        pics.path = %(path)s
                    WHERE  houses.id=%(id)s
                    AND pics.house_id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    

    @classmethod
    def delete_the_house_with_its_pictures(cls,data):
        query="""DELETE houses, pics
            FROM houses
            JOIN pics ON houses.id = pics.house_id
            WHERE your_condition houses.id=%(id)s
                    AND pics.house_id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)