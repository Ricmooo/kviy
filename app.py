from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = {
    'Easy Peasy': [
        {'question': 'Ko je osvojio SP 2022', 'choices': ['argentina', 'francuska', 'njemacka'], 'answer': 'argentina'},
        {'question': 'Koje godine je odrzano SP u Brazilu?', 'choices': ['2010', '2018', '2014'], 'answer': '2014'},
        {'question': 'Gdje je odrazno evropsko prvenstvo 2016?', 'choices': ['Francuska', 'Njemacka', 'Engleska'], 'answer': 'Francuska'},
        {'question': 'Koliko traje jedna utakmica?', 'choices': ['90-minuta', '60-minuta', '100-minuta'], 'answer': '90-minuta'},
        {'question': 'Kada igrac zabije sam sebi gol to je', 'choices': ['zgoditak', 'auto-gol', 'harakiri'], 'answer': 'auto-gol'}
    ],
    'Not Too Shabby': [
        {'question': 'Koliko Messi ima zlatnih lopti?', 'choices': ['5', '6', '8'], 'answer': '8'},
        {'question': 'Koliko Ronaldo ima zlatnih lopti?', 'choices': ['6', '5', '7'], 'answer': '5'},
        {'question': 'Ko je osvojio UCl 2016?', 'choices': ['Juve', 'Real', 'Atletico'], 'answer': 'Real'},
        {'question': 'Koliko real madrid ima ligi sampiona?', 'choices': ['8', '14', '32'], 'answer': '14'},
        {'question': 'koliko barcelona ima ligi sampiona?', 'choices': ['4', '5', '8'], 'answer': '5'}
    ],
    'Let\'s Get Serious': [
        {'question': 'Koji broj na dresu nosi Benzema?', 'choices': ['9', '10', '14'], 'answer': '9'},
        {'question': 'Koji je trenutno trener Bayern Minhena"?', 'choices': ['Vincent Kompany', 'Thomas Tuchel', 'Pep Guardiola'], 'answer': 'Vincent Kompany'},
        {'question': 'Koji broj nosi toni kross?', 'choices': ['6', '7', '8'], 'answer': '8'},
        {'question': 'Ko je osvojio SP 2014?', 'choices': ['Brazil', 'Argentina', 'Njemacka'], 'answer': 'Njemacka'},
        {'question': 'Gdje se igralo Euro 2004?', 'choices': ['Portugal', 'Grcka', 'Spanija'], 'answer': 'Portugal'}
    ],
    'Getting Tricky': [
        {'question': 'Ko od njih nije igrao finale Lige prvaka?', 'choices': ['Dzeko', 'Pjanic', 'Kolasinac'], 'answer': 'Kolasinac'},
        {'question': 'Ko od njih nema zlatnu loptu?', 'choices': ['Nedved', 'Shevchenko', 'Maldini'], 'answer': 'Maldini'},
        {'question': 'Ko od njih je jedini osvojio LS', 'choices': ['Mandzukic', 'Buffon', 'Ibrahimovic'], 'answer': 'Mandzukic'},
        {'question': 'Gdje se Igralo finale LS 2013', 'choices': ['Engleska', 'Njemacka', 'Italija'], 'answer': 'Engleska'},
        {'question': 'Ko je izgubio u finalu LS 2013"?', 'choices': ['Brusija', 'Bayern', 'Real'], 'answer': 'Brusija'}
    ],
    'Ultimate Challenge': [
        {'question': 'U koliko klubova je igaro Zalatn Ibrahimovic?', 'choices': ['8', '9', '10'], 'answer': '9'},
        {'question': 'Ko je bio treci na SP 2010?', 'choices': ['Njemacka', 'Brazil', 'Urugvaj'], 'answer': 'Njemacka'},
        {'question': 'Ko je osvojio LS 1997?', 'choices': ['Brusija', 'Crvena Zvezda', 'Ajax'], 'answer': 'Brusija'},
        {'question': 'Ko je izgubio Finale LS 2010?', 'choices': ['Bayern', 'Real', 'Chealse'], 'answer': 'Bayern'},
        {'question': 'Ko je najbolji igrac svih vremena?', 'choices': ['Ronaldo', 'Messi', 'Ricmo'], 'answer': 'Ricmo'}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/level/<level>', methods=['GET', 'POST'])
def level(level):
    if level not in questions:
        return redirect(url_for('index'))

    if request.method == 'POST':
        user_answers = request.form.to_dict()
        score = 0
        for idx, question in enumerate(questions[level]):
            if user_answers.get(str(idx)) == question['answer']:
                score += 1
        return redirect(url_for('result', level=level, score=score))

    return render_template('level.html', questions=list(enumerate(questions[level])), level=level)

@app.route('/result/<level>/<score>')
def result(level, score):
    return render_template('result.html', level=level, score=score, questions=questions[level])

if __name__ == '__main__':
    app.run(debug=True)
