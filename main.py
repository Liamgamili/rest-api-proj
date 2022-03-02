from flask import Flask, request, render_template
import json

app = Flask(__name__)

customers = [{'id': 1, 'name': 'danny', 'address': 'tel-aviv'},
             {'id': 2, 'name': 'marina', 'address': 'beer sheav'},
             {'id': 3, 'name': 'david', 'address': 'herzeliya'}]


@app.route("/")
def home():
    print('hi')
    return '''
        <html>
            Ready!
        </html>
    '''


@app.route('/customers', methods=['GET', 'POST'])
def get_or_post_customer():
    if request.method == 'GET':
        
        return json.dumps(customers)
    if request.method == 'POST':
        #  {'id': 4 [not be sent with DB], 'name': 'david', 'address': 'herzeliya'}
        new_customer = request.get_json()
        customers.append(new_customer)
        return '{"status": "success"}'

@app.route('/customers/<int:id>', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def get_customer_by_id(id):
    global customers
    if request.method == 'GET':
       
        for c in customers:
            if c["id"] == id:
                return json.dumps(c)
        return '{}'
    if request.method == 'PUT':
      
        updated_new_customer = request.get_json()
        for c in customers:
            if c["id"] == id:
                c["id"] = updated_new_customer["id"] if "id" in updated_new_customer.keys() else None
                c["name"] = updated_new_customer["name"] if "name" in updated_new_customer.keys() else None
                c["address"] = updated_new_customer["address"] if "address" in updated_new_customer.keys() else None
                return json.dumps(updated_new_customer)
        customers.append(updated_new_customer)
        return json.dumps(updated_new_customer)
    if request.method == 'PATCH':
        
        updated_customer = request.get_json()
        for c in customers:
            if c["id"] == id:
                c["id"] = updated_customer["id"] if "id" in updated_customer.keys() else c["id"]
                c["name"] = updated_customer["name"] if "name" in updated_customer.keys() else c["name"]
                c["address"] = updated_customer["address"] if "address" in updated_customer.keys() else c["address"]
                return json.dumps(updated_customer)
        return '{"status": "not found"}'
    if request.method == 'DELETE':
        customers = [c for c in customers if c["id"] != id]
        return json.dumps(customers)

app.run()
