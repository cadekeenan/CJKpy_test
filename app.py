from sqlite3 import complete_statement
from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', pageTitle='VTM Site')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Page')

def calculate_top(radius):
    return 3.14*(radius**2)

def calculate_side(radius,height):
    return 2*(3.14*(radius*height))


@app.route('/estimate', methods=['GET','POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        top_area=3.14*(radius**2)
        side_area=2*(3.14*(radius*height))
        total_area = top_area + side_area
        total_sqft = total_area/144
        material_cost = 25 
        total_material_cost = total_sqft*material_cost
        labor_cost = 15
        total_labor_cost = labor_cost*total_sqft
        cost = total_material_cost + total_labor_cost
        return str("${:,.2f}".format(cost))
    return render_template('estimates.html', pageTitle='Estimate')

if __name__ == '__main__':
    app.run(debug=True)

def test_estimate_functionality(app, client): 

    """  

    GIVEN a Flask application configured for testing 

    WHEN the '/estimate' route is requested (POST) 

    THEN check that the new user is added to the list 

    """ 

    print("-- /estimate POST test") 

    with app.test_client() as test_client: 

       estimate_calc = {"radius":"180", "height":"360"} 

       res = test.client.post('/estimate', data=estimate_calc) 

       assert res.status_code == 200 

       assert b"141,300" in res.data   