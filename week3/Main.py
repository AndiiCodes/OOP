from flask import Flask, render_template, request, redirect, url_for,session

app = Flask(__name__)
app.secret_key = 'dsadsadsds'
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        selected_crust = request.form.get('crust')
        selected_size = request.form.get('size')
        selected_topping = request.form.get('topping')
        quantity = request.form.get('quantity')
        pickup_time = request.form.get('time')
        location = request.form.get('location')
        name = request.form.get('name')
        contact_numb=request.form.get("number")
        pizzaPrice=15
        if selected_size == 'medium':
            pizzaPrice+=2
            

        if selected_size == 'large':
            pizzaPrice+=5.5
            
        totalPrice= pizzaPrice * int(quantity)
        

        session_data = {
            'price' :  '$' + str(pizzaPrice),
            'total' : '$'+ str(totalPrice),
            'selected_crust': selected_crust,
            'selected_size': selected_size,
            'selected_topping': selected_topping,
            'quantity': quantity,
            'pickup_time': pickup_time,
            'location': location,
            'name': name,
            'contact number' : contact_numb
        }
        print(session_data)


        session['order_data'] = session_data

        return redirect(url_for('receipt'))

    return render_template('index.html')

@app.route('/receipt')
def receipt():

    order_data = session.get('order_data', {})
    print(order_data)
    session.pop('order_data', None)
    return render_template('user-info.html', content=order_data)

if __name__ == '__main__':
    app.run(debug=True)
