"""
fields:
-ID
-guest count
-dietary options: vegetarian / non-vegetarian
-special dietary restrictions

-Record timestamp whenever user creates or updates an entry

Relevant http request/response types:
-RSVP creation:
--POST: 201 (Created), 'Location' header with link to /customers/{id} containing new ID.
        404 (Not Found)
        409 (Conflict) if resource already exists
-Reading/querying:
--GET: 200 (OK), list of customers. Use pagination, sorting and filtering to navigate big lists.
       200 (OK), single customer.
       404 (Not Found), if ID not found or invalid.
-RSVP modification 
--PATCH: 405 (Method Not Allowed), unless you want to modify the collection itself.	200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid.

-Throttle dynamodb so that requests don't exceed > some fraction of 1M / month
"""

from flask import Flask, current_app, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_update():
    #Verify that request came from a human using invis recapcha

    #Get data from request
    form_data = request.form.to_dict()
    
    #Send update to dynamodb
    
    
    #Construct and return response
    resp = current_app.make_default_options_response()
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp

if __name__ == "__main__":
    app.run()
