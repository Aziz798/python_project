from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class House_in_sell:
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.mortage_validation=data['mortage_validation']
        self.mortage_monthly=data['mortage_monthly']
        self.location=data['location']
        self.pic=data['pic']
        self.price=data['price']
        self.bathroom=data['bathroom']
        self.beds=data['beds']
        self.surface=data['surface']
        self.created_at=data=['created_at']
        self.updated_at=data['updated_at']

    # Create a house to sell
    @classmethod
    def create_a_house_to_sell(cls,data):
        query="""INSERT INTO houses_in_sell (user_id,mortage_validation,mortage_monthly,location,pic,price,bathroom,beds,surface)
                VALUES 
                (%(user_id)s,%(mortage_vlidation)s,%(mortage_monthly)s,%(location)s,%(pic)s,%(price)s,%(bathroom)s,%(beds)s,%(surface)s);"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # Update an existing house by it's id
    @classmethod
    def update_a_house_to_sell(cls,data):
        query="""UPDATE houses_in_sell SET mortage_validation=%(mortage_validation)s,mortage_monthly=%(mortage_monthly)s,
                    location=%(location)s,pic=%(pic)s,price=%(price)s,bathroom=%(bathroom)s,beds=%(beds)s,surface=%(surface)s
                    WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # Show all houses in sell (this should be displayed to both buyers and sellers later in display)
    @classmethod
    def show_all_houses_in_sell(cls):
        query="SELECT * FROM houses_in_sell;"
        result=connectToMySQL(DATABASE).query_db(query)
        all_houses_in_sell=[]
        for house in result:
            all_houses_in_sell.append(cls(house))
        return all_houses_in_sell
    
    # Show one seller houses (this functionality unique to only the sellers )
    @classmethod
    def show_the_houses_in_sell_of_one_seller(cls,data):
        query="SELECT * FROM houses_in_sell WHERE user_id=%(user_id)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_of_that_seller_houses=[]
        for house in result:
            all_of_that_seller_houses.append(cls(house))
        return all_of_that_seller_houses
    
    # Delete a house from display (this functionality unique to only the sellers )
    @classmethod
    def delete_one_house(cls,data):
        query= "DELETE FROM houses_in_sell WHERE id =%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # Show one house details (this should be displayed to both buyers and sellers later in display)
    @classmethod
    def show_one_house_thats_for_sale_details(cls,data):
        query="""SELECT houses_in_sell*,first_name,last_name,email,phone_number FROM houses_in_sell JOIN
                users ON houses_in_sell.user_id=users.id 
                WHERE houses_in_sell.id=%(id)s;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result[0]
    
    # Show all houses that can be bought with a morthage
    @classmethod
    def show_all_houses_in_sell_criteria_mortage_availability(cls,data):
        query="SELECT * FROM houses_in_sell WHERE mortage_valiadtion=1;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses
    
    # Show all houses in sell where the monthly mortage is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_mortage_availability_and_monthly_mortage(cls,data):
        query="SELECT * FROM houses_in_sell WHERE mortage_validation=1 AND mortage_monthly<=%(max)s AND mortage_monthly>=%(min)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses
    
    # Show all houses in sell where the bedrooms is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_bedrooms(cls,data):
        query="SELECT * FROM houses_in_sell WHERE beds<=%(max)s AND beds>=%(min)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses


    # Show all houses in sell where the bathrooms is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_bathrooms(cls,data):
        query="SELECT * FROM houses_in_sell WHERE bathroom<=%(max)s AND bathroom>=%(min)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses
    


    # Show all houses in sell where the bedrooms and bathrooms is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_bedrooms_and_bathrooms(cls,data):
        query="SELECT * FROM houses_in_sell WHERE beds<=%(max_bed)s AND beds>=%(min_bed)s AND bathroom<=%(max_bathroom)s AND bathroom>=%(min_bathroom)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses
    

    # Show all houses in sell where no mortage is available is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_no_moratge_availability(cls,data):
        query="SELECT * FROM houses_in_sell WHERE mortage_validation=0;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses

    # Show all houses in sell where bedrooms and bathrooms and mortage available is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_bedrooms_and_bathrooms_moratge_available(cls,data):
        query="SELECT * FROM houses_in_sell WHERE beds<=%(max_bed)s AND beds>=%(min_bed)s AND bathroom<=%(max_bathroom)s AND bathroom>=%(min_bathroom)s AND mortage_validation=1;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses
        
    # Show all houses in sell where bedrooms and mortage available is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_bed_and_mortage_availability(cls,data):
        query="""SELECT * FROM houses_in_sell WHERE 
        beds<=%(max_bed)s AND beds>=%(min_bed)s AND mortage_validation=1;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses
    

    # Show all houses in sell where bedrooms and mortage not available is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_bed_and_mortage_not_available(cls,data):
        query="""SELECT * FROM houses_in_sell WHERE 
        beds<=%(max_bed)s AND beds>=%(min_bed)s AND mortage_validation=0;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses
    

    # Show all houses in sell where bethrooms and mortage  available is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_bathroom_and_mortage_available(cls,data):
        query="""SELECT * FROM houses_in_sell WHERE 
        bathroom<=%(max_bathroom)s AND bethroom>=%(min_bathroom)s AND mortage_validation=1;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses
    

    # Show all houses in sell where bethrooms and mortage not available is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_bathroom_and_mortage_not_available(cls,data):
        query="""SELECT * FROM houses_in_sell WHERE 
        bathroom<=%(max_bathroom)s AND bethroom>=%(min_bathroom)s AND mortage_validation=0;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses
    


    # Show all houses in sell where bedrooms and bathrooms and mortage not available is the criteria
    @classmethod
    def show_all_houses_in_sell_criteria_bedrooms_and_bathrooms_moratge_available(cls,data):
        query="SELECT * FROM houses_in_sell WHERE beds<=%(max_bed)s AND beds>=%(min_bed)s AND bathroom<=%(max_bathroom)s AND bathroom>=%(min_bathroom)s AND mortage_validation=0;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_houses=[]
        for house in result:
            all_houses.append(cls(house))
        return all_houses
        