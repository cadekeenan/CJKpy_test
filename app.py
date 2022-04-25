from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', pageTitle= "Home")

@app.route('/about')
def about():
    return render_template('about.html', pageTitle="About")
@app.route('/estimates', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = form(['radius'])
        height = form(['height'])
        radius = float(radius)
        height = float(height)
        area_top = 3.14 * radius**2
        area_side = 2*3.14*radius*height
        total_area = area_top + area_side
        sqft = total_area / 144
        matCost = 25 
        totalMatCost = sqft * matCost
        labor = 15
        total_labor_cost = labor * sqft
        total_cost_estimate = totalMatCost + total_labor_cost
        total_cost_estimate = str(total_cost_estimate)
        return(total_cost_estimate)
    return(render_template('estimates.html', pageTitle="Estimate")) 

if __name__ == '__main__':
    app.run(debug=True)
