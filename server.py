import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)  # instantiate the name
print(__name__)  # to see what this is. __name__ is the __main__


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/works.html')
def work():
    return render_template('works.html')


@app.route('/thankyou.html')
def appreciation():
    return render_template('thankyou.html')


# @app.route('/<string:page_name>')
# def html_page(page_name):
#   return render_template('page_name')

def write_to_file(data):  # create a function to redirect data
    with open('database.txt', mode='a') as database:  # renaming database.txt as database
        email = data["email"]  # from data - selecting email
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')  # writing into the database file


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]  # from data - selecting email
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()  # creating a data (contact: email, message)
        write_to_file(data)  # data is everything that contains email, subject, message
        write_to_csv(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. Try Again!'


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
