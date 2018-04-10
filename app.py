from flask import Flask, render_template, request
import model

# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return '''
# 		<img src="/static/blockM.png"/>
# 		<h1>Michigan Sports Info!</h1>
# 		<ul>
# 			<li><a href="/bball"> Men's Basketball </a></li>
# 		</ul>
# 	'''

# # @app.route('/bball')
# # def bball():
# # 	return render_template("seasons.html", seasons=model.get_bball_seasons())


# @app.route('/bball', methods=['GET', 'POST'])
# def bball():
#     if request.method == 'POST':
#         sortby = request.form['sortby']
#         sortorder = request.form['sortorder']
#         seasons = model.get_bball_seasons(sortby, sortorder)
#     else:
#         seasons = model.get_bball_seasons()
        
#     return render_template("seasons.html", seasons=seasons)

# @app.route('/hello', methods=['GET', 'POST'])
# def hello():
# 	if request.method == 'POST':
# 	    firstname = request.form['firstname']
# 	    lastname = request.form['lastname']
# 	else:
# 		firstname = ''
# 		lastname = ''

# 	return render_template("hello.html", firstname = firstname, lastname = lastname)


#     # return render_template("hello.html")

# if __name__ == '__main__':
# 	model.init_bball()
# 	app.run(debug=True)


app = Flask(__name__)

@app.route('/')
def index():
	return '''
		<img src="/static/blockM.png"/>
		<h1>Michigan Sports Info!</h1>
		<ul>
			<li><a href="/ftball"> Men's Football </a></li>
		</ul>
	'''

# @app.route('/bball')
# def bball():
# 	return render_template("seasons.html", seasons=model.get_bball_seasons())


@app.route('/ftball', methods=['GET', 'POST'])
def ftball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_ftball_seasons(sortby, sortorder)
    else:
        seasons = model.get_ftball_seasons()
        
    return render_template("seasons.html", seasons=seasons)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
	    firstname = request.form['firstname']
	    lastname = request.form['lastname']
	else:
		firstname = ''
		lastname = ''

	return render_template("hello.html", firstname = firstname, lastname = lastname)


    # return render_template("hello.html")

if __name__ == '__main__':
	model.init_ftball()
	app.run(debug=True)

