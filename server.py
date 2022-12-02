from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__) 
    # Create a new instance of the Flask class called "app"

# @app.route('/hello_world')
# def hello_world():
#     return "Hello World!"
# #this is a test to make sure everythin is linked up and imported properly

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def play():
    return render_template("index.html", times=3)  # Return the string 'Hello World!' as a response
    # return "This is a page!"

@app.route('/play/<int:times>')
def play_x_times(times):
    return render_template("index.html", times=times)

@app.route('/play/<int:times>/<new_color>')
def play_x_times_color(times, new_color):
    return render_template("index.html", times=times, new_color=new_color)
    # return f" you are entering {times} {new_color}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host='0.0.0.0')    # Run the app in debug mode.