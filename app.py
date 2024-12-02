from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Generowanie siatki - 365 dni
    grid = [[0 for _ in range(52)] for _ in range(7)]  # 7 dni tygodnia, 52 tygodnie
    return render_template('index.html', grid=grid)

if __name__ == '__main__':
    app.run(debug=True)
