from flask_app import app
from flask import render_template ,redirect,request,flash,session
from flask_app.models.house import House


@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/buy/house')
def get_houses_for_sale():
    houses=House.select_all_houses_for_sale_with_pic()
    return render_template('all_houses_for_sale.html',houses=houses)


@app.route('/sell/house')
def put_a_house_to_sell():
    return render_template('create_a_house_to_sell.html')

@app.post('/create/house/sell')
def sell_the_house():
    data={
        'user_id':session['user_id'],
        **request.form
    }
    
    new_house_id=House.create_a_house(data)
    return redirect('/house/pics_forhouse/'+str(new_house_id))

@app.post('/house/pics/insert')
def insert_pics_to_the_house_to_sell():
    print("IMAGE FORM-----",request.form)
    print("IMAGE FiLE-----",request.files)
    file = request.files['path']
    
    return redirect(f'/house/{request.form['house_id']}')

@app.route('/house/pics_forhouse/<int:id>')
def get_house_by_id(id):
    return render_template('on_house.html', data=id)



