import time

def test_index_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    print("\r")
    print(" -- / GET test")
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        
        
        
def test_about_route(app, client): 

    """
    GIVEN a Flask application configured for testing 

    WHEN the '/about' route is requested (GET) 

    THEN check that the response is valid 
    """
    print("-- /about GET test") 

    with app.test_client() as test_client: 

        res = test_client.get('/about') 

        assert res.status_code == 200 

        assert b"VTM" in res.data 

        assert b"About VTM" in res.data

def test_estimate_route(app, client): 

    """  

    GIVEN a Flask application configured for testing 

    WHEN the '/estimate' route is requested (GET) 

    THEN check that the user is redirected to the home page 

    """ 

    print("-- /estimate GET test") 

    with app.test_client() as test_client: 

        res = test_client.get('/estimates') 

        assert res.status_code == 200 

        assert b"VTM Cost Estimates" in res.data 

def test_estimate_functionality(app, client): 

    """  

    GIVEN a Flask application configured for testing 

    WHEN the '/estimate' route is requested (POST) 

    THEN check that the new user is added to the list 

    """ 

    print("-- /estimates POST test") 

    with app.test_client() as test_client: 

       estimate_calc = {"radius":"180", "height":"360"} 

       res = test_client.post('/estimates', data=estimate_calc) 

       assert res.status_code == 200 

       assert b"141,300" in res.data 
