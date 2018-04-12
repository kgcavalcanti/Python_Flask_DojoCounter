from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.count = 0

@app.route('/')
def make_count():
    session['count'] += 1
    print session['count']
    return render_template('index.html', counter = session['count'] )


@app.route('/reload')
def reload():
	session['count'] += 2
	print session['count']
	return render_template('index.html', counter = session['count'])


@app.route('/reset')
def reset():
	session['count'] = 0
	print session['count']
	return render_template('index.html', counter = session['count'])
app.run(debug=True)


	

