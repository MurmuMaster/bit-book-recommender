from flask import Flask, request, render_template
import pandas as pd

df = pd.read_csv('data.csv', encoding='unicode_escape')

app = Flask(__name__)

# routes
@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template('form.html')
    else:
        branch = request.form['branch']
        sem = int(request.form['sem'])
        sub = request.form['sub']

        # print(type(branch))
        # print(type(sem))
        # print(type(sub))

        # print(branch)
        # print(sem)
        # print(sub)
        
        # Filter the DataFrame based on the form inputs
        filtered_df = df[(df['Branch'] == branch) & (df['Semester'] == sem) & (df['Subject'] == sub)]

        # Convert the filtered DataFrame to a list of dictionaries for rendering
        books = filtered_df.to_dict(orient='records')

        print(books)

        return render_template('form.html', books=books)
    

@app.route("/book/<int:book_id>")
def book_details(book_id):
    book = df.loc[df['bookId'] == book_id].to_dict(orient='records')[0]
    return render_template('book_details.html', book=book)

if __name__ == "__main__":
    app.run(debug=True)
