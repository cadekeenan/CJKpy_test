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

        res = test_client.get('/estimate') 

        assert res.status_code == 200 

        assert b"VTM Cost Estimates" in res.data 
