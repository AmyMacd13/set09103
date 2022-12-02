from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'SUPERSEKRETKEY'


@app.route("/")
def hello():
    return render_template('home.html')


#Addition

@app.route("/add/")
def add():
    return render_template('add.html')


#start addition quiz one 

@app.route("/add/add-start-one/")
def starting():
    session['question'] = 1
    return render_template('index.html')



@app.route("/add/add-quiz-one/")
def add_quiz1():
    q = None
    qa = {
        "1":{
            "text":"5+2?",
            "answer":1,
            "answers":["7", "3", "8", "6" ]
        },
        "2":{
            "text":"8+4?",
            "answer":3,
            "answers":["10", "4", "12", "14" ]
        },
        "3":{
            "text":"3+7?",
            "answer":1,
            "answers":["10", "13", "11", "9" ]
        },
        "4":{
            "text":"4+5?",
            "answer":4,
            "answers":["7", "11", "8", "9" ]
        },
        "5":{
            "text":"2+6?",
            "answer":2,
            "answers":["7", "8", "4", "9" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1
answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success.html')
            else:
                return render_template('quiz.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong.html', text="OOPS! wrong answer")
    else:
        return render_template('quiz.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)




#starting addition quiz 2


@app.route("/add/add-start-two/")
def starting2():
    session['question'] = 1
    return render_template('index1.html')

@app.route("/add/add-quiz-two/")
def add_quiz2():
    q = None
    qa = {
        "1":{
            "text":"8+11?",
            "answer":4,
            "answers":["17", "20", "18", "19" ]
        },
        "2":{
            "text":"7+9?",
            "answer":2,
            "answers":["15", "16", "17", "18" ]
        },
        "3":{
            "text":"6+13?",
            "answer":2,
            "answers":["15", "19", "21", "18" ]
        },
        "4":{
            "text":"12+9?",
            "answer":1,
            "answers":["21", "23", "18", "20" ]
        },
        "5":{
            "text":"10+11?",
            "answer":3,
            "answers":["25", "22", "21", "20" ]
        },
        "6":{
            "text":"14+8?",
            "answer":4,
            "answers":["24", "19", "18", "22" ]
        },
        "7":{
            "text":"7+16?",
            "answer":1,
            "answers":["23", "19", "18", "20" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success.html')
            else:
                return render_template('quiz1.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong1.html', text="OOPS! wrong answer")
    else:
        return render_template('quiz1.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)



#starting addition quiz 3


@app.route("/add/add-start-three/")
def starting3():
    session['question'] = 1
    return render_template('index2.html')

@app.route("/add/add-quiz-three/")
def add_quiz3():
    q = None
    qa = {
        "1":{
            "text":"13+12?",
            "answer":3,
            "answers":["22", "27", "25", "23" ]
        },
        "2":{
            "text":"18+9?",
            "answer":2,
            "answers":["29", "27", "30", "26" ]
        },
        "3":{
            "text":"11+23?",
            "answer":2,
            "answers":["34", "33", "36", "35" ]
        },
        "4":{
            "text":"14+13?",
            "answer":3,
            "answers":["30", "26", "27", "29" ]
        },
        "5":{
            "text":"15+23?",
            "answer":1,
            "answers":["38", "42", "36", "39" ]
        },
        "6":{
            "text":"13+28?",
            "answer":4,
            "answers":["40", "39", "43", "41" ]
        },
        "7":{
            "text":"27+34?",
            "answer":2,
            "answers":["55", "61", "62", "59" ]
        },
        "8":{
            "text":"19+23?",
            "answer":3,
            "answers":["40", "41", "42", "43" ]
        },
        "9":{
            "text":"33+21?",
            "answer":4,
            "answers":["57", "64", "52", "54" ]
        },
        "10":{
            "text":"17+44?",
            "answer":1,
            "answers":["61", "59", "62", "60" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success.html')
            else:
                return render_template('quiz2.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong2.html', text="OOPS! wrong answer")
    else:
        return render_template('quiz2.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)


@app.route("/add/add-quiz-one/success/")
def success():
    return render_template('success.html')


#Subtraction


@app.route("/subtract/")
def subract():
    return render_template('subtract.html')



#start subract quiz one

@app.route("/subtract/sub-start-one/")
def starting4():
    session['question'] = 1
    return render_template('index3.html')



@app.route("/subtract/sub-quiz-one/")
def sub_quiz1():
    q = None
    qa = {
        "1":{
            "text":"4-2?",
            "answer":3,
            "answers":["1", "3", "2", "0" ]
        },
        "2":{
            "text":"8-3?",
            "answer":2,
            "answers":["7", "5", "4", "6" ]
        },
        "3":{
            "text":"9-3?",
            "answer":4,
            "answers":["7", "12", "3", "6" ]
        },
        "4":{
            "text":"7-4?",
            "answer":4,
            "answers":["7", "2", "4", "3" ]
        },
        "5":{
            "text":"5-1?",
            "answer":1,
            "answers":["4", "3", "6", "5" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success2.html')
            else:
return render_template('quiz3.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong3.html', text="OOPS! wrong answer")
    else:
        return render_template('quiz3.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)



#start subtract quiz two

@app.route("/subtract/sub-start-two/")
def starting5():
    session['question'] = 1
    return render_template('index4.html')



@app.route("/subtract/sub-quiz-two/")
def sub_quiz2():
    q = None
    qa = {
        "1":{
            "text":"12-4?",
            "answer":4,
            "answers":["12", "10", "9", "8" ]
        },
        "2":{
            "text":"13-5?",
            "answer":2,
            "answers":["7", "8", "4", "6" ]
        },
        "3":{
            "text":"19-3?",
            "answer":1,
            "answers":["16", "17", "13", "15" ]
        },
        "4":{
            "text":"14-4?",
            "answer":4,
            "answers":["12", "9", "13", "10" ]
        },
        "5":{
            "text":"9-7?",
            "answer":3,
            "answers":["6", "5", "2", "3" ]
        },
        "6":{
            "text":"18-7?",
            "answer":4,
            "answers":["17", "12", "14", "11" ]
        },
        "7":{
            "text":"11-5?",
            "answer":1,
            "answers":["6", "4", "7", "5" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1
answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success2.html')
            else:
                return render_template('quiz4.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong4.html', text="OOPS! wrong answer")
    else:
        return render_template('quiz4.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)




#start subtract quiz three

@app.route("/subtract/sub-start-three/")
def starting6():
    session['question'] = 1
    return render_template('index5.html')



@app.route("/subtract/sub-quiz-three/")
def sub_quiz3():
    q = None
    qa = {
        "1":{
            "text":"20-14?",
            "answer":3,
            "answers":["7", "8", "6", "4" ]
        },
        "2":{
            "text":"27-8?",
            "answer":4,
            "answers":["21", "18", "20", "19" ]
        },
        "3":{
            "text":"29-13?",
            "answer":2,
            "answers":["17", "16", "13", "15" ]
        },
        "4":{
            "text":"7-11?",
            "answer":1,
            "answers":["-4", "4", "5", "-3" ]
        },
        "5":{
            "text":"33-19?",
            "answer":4,
            "answers":["13", "15", "16", "14" ]
        },
        "6":{
            "text":"18-27?",
            "answer":2,
            "answers":["-11", "-9", "8", "-8" ]
        }, "7":{
            "text":"23-16?",
            "answer":3,
            "answers":["6", "4", "7", "5" ]
        },
        "8":{
            "text":"39-17?",
            "answer":3,
            "answers":["26", "25", "22", "21" ]
        },
        "9":{
            "text":"25-18?",
            "answer":1,
            "answers":["7", "6", "4", "8" ]
        },
        "10":{
            "text":"54-22?",
            "answer":4,
            "answers":["33", "31", "36", "32" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success2.html')
            else:
                return render_template('quiz5.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong5.html', text="OOPS! wrong answer")
    else:
        return render_template('quiz5.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)


@app.route("/subtract/sub-quiz-one/success2/")
def success2():
    return render_template('success2.html')




#multiply

@app.route("/multiply/")
def multiply():
    return render_template('multiply.html')




#start multiply quiz one
@app.route("/multiply/multiply-start-one/")
def starting7():
    session['question'] = 1
    return render_template('index6.html')

@app.route("/multiply/multiply-quiz-one/")
def multiply_quiz1():
    q = None
    qa = {
        "1":{
            "text":"2x3?",
            "answer":3,
            "answers":["3", "9", "6", "2" ]
        },
        "2":{
            "text":"3x4?",
            "answer":1,
            "answers":["12", "16", "9", "8" ]
        },
        "3":{
            "text":"2x5?",
            "answer":3,
            "answers":["5", "15", "10", "8" ]
        },
        "4":{
            "text":"10x4?",
            "answer":2,
            "answers":["14", "40", "400", "10" ]
        },
        "5":{
            "text":"5x3?",
            "answer":4,
            "answers":["5", "30", "25", "15" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success3.html')
            else:
                return render_template('quiz6.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong6.html', text="OOPS! wrong answer")
    else:
        return render_template('quiz6.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)



#start multiply quiz two
@app.route("/multiply/multiply-start-two/")
def starting8():
    session['question'] = 1
    return render_template('index7.html')

@app.route("/multiply/multiply-quiz-two/")
def multiply_quiz2():
    q = None
    qa = {
        "1":{
            "text":"6x4?",
            "answer":1,
            "answers":["24", "28", "20", "22" ]
        },
        "2":{
            "text":"3x7?",
            "answer":4,
            "answers":["12", "18", "23", "21" ]
        },
        "3":{
            "text":"4x8?",
            "answer":3,
            "answers":["38", "30", "32", "40" ]
        },
        "4":{
            "text":"6x7?",
            "answer":1,
            "answers":["42", "40", "39", "56" ]
        },
        "5":{
            "text":"8x5?",
            "answer":2,
            "answers":["56", "40", "45", "38" ]
        },
        "6":{
            "text":"7x4",
            "answer":1,
            "answers":["28", "30", "26", "29" ]
        },
        "7":{
            "text":"6x6?",
            "answer":4,
            "answers":["35", "40", "38", "36" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success3.html')
            else:
                return render_template('quiz7.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong7.html', text="OOPS! wrong answer")
      else:
        return render_template('quiz7.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)



#start multiply quiz three

@app.route("/multiply/multiply-start-three/")
def starting9():
    session['question'] = 1
    return render_template('index8.html')

@app.route("/multiply/multiply-quiz-three/")
def multiply_quiz3():
    q = None
    qa = {
        "1":{
            "text":"6x8?",
            "answer":4,
            "answers":["62", "56", "74", "54" ]
        },
        "2":{
            "text":"9x7?",
            "answer":3,
            "answers":["70", "69", "63", "61" ]
        },
        "3":{
            "text":"4x8?",
            "answer":3,
            "answers":["38", "30", "32", "40" ]
        },
        "4":{
            "text":"6x7?",
            "answer":1,
            "answers":["42", "40", "39", "56" ]
        },
        "5":{
            "text":"8x11?",
            "answer":2,
            "answers":["78", "88", "480", "98" ]
        },
        "6":{
            "text":"7x7",
            "answer":4,
            "answers":["37", "40", "52", "49" ]
        },
        "7":{
            "text":"12x6?",
            "answer":2,
            "answers":["66", "72", "63", "74" ]
        },
        "8":{
            "text":"8x3?",
            "answer":3,
            "answers":["26", "20", "24", "22" ]
        },
        "9":{
            "text":"7x8",
            "answer":1,
            "answers":["56", "58", "62", "70" ]
        },
        "10":{
            "text":"5x13?",
            "answer":2,
            "answers":["37", "65", "66", "130" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success3.html')
            else:
                return render_template('quiz8.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong8.html', text="OOPS! wrong answer")
    else:
        return render_template('quiz8.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)



#Divide

@app.route("/divide/")
def divide():
    return render_template('divide.html')




#start divide quiz one

@app.route("/divide/divide-start-one/")
def starting10():
    session['question'] = 1
    return render_template('index9.html')

@app.route("/divide/divide-quiz-one/")
def divide_quiz1():
    q = None
    qa = {
        "1":{
            "text":"10÷5?",
            "answer":2,
            "answers":["3", "5", "6", "2" ]
        },
        "2":{
            "text":"3÷3?",
            "answer":1,
            "answers":["1", "0", "3", "6" ]
        },
        "3":{
            "text":"8÷2?",
            "answer":3,
            "answers":["5", "2", "4", "8" ]
        },
         "4":{
            "text":"9÷3?",
            "answer":2,
            "answers":["6", "3", "2", "9" ]
        },
        "5":{
            "text":"6÷2?",
            "answer":4,
            "answers":["6", "2", "5", "3" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success4.html')
            else:
                return render_template('quiz9.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong9.html', text="OOPS! wrong answer")
    else:
        return render_template('quiz9.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)


#start divide quiz two

@app.route("/divide/divide-start-two/")
def starting11():
    session['question'] = 1
    return render_template('index10.html')

@app.route("/divide/divide-quiz-two/")
def divide_quiz2():
    q = None
    qa = {
        "1":{
            "text":"20÷10?",
            "answer":2,
            "answers":["3", "2", "5", "12" ]
        },
        "2":{
            "text":"15÷3?",
            "answer":1,
            "answers":["5", "0", "3", "6" ]
        },
        "3":{
            "text":"36÷6?",
            "answer":1,
            "answers":["6", "5", "4", "8" ]
        },
        "4":{
            "text":"27÷3?",
            "answer":3,
            "answers":["4", "3", "9", "8" ]
        },
        "5":{
            "text":"70÷7?",
            "answer":4,
            "answers":["7", "2", "5", "10" ]
        },
        "6":{
            "text":"45÷9?",
            "answer":3,
            "answers":["4", "9", "5", "8" ]
        },
        "7":{
            "text":"16÷8?",
            "answer":2,
            "answers":["7", "2", "5", "10" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success4.html')
            else:
                return render_template('quiz10.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong10.html', text="OOPS! wrong answer")
    else:
        return render_template('quiz10.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)



#start divide quiz three

@app.route("/divide/divide-start-three/")
def starting12():
    session['question'] = 1
    return render_template('index11.html')

@app.route("/divide/divide-quiz-three/")
def divide_quiz3():
    q = None
    qa = {
        "1":{
            "text":"32÷4?",
            "answer":2,
            "answers":["3", "8", "6", "2" ]
        },
        "2":{
            "text":"42÷7?",
            "answer":1,
            "answers":["6", "0", "3", "7" ]
        },
        "3":{
            "text":"32÷8?",
            "answer":3,
            "answers":["5", "2", "4", "8" ]
        },
        "4":{
            "text":"72÷8?",
            "answer":2,
            "answers":["6", "9", "10", "7" ]
        },
        "5":{
            "text":"63÷9?",
            "answer":4,
            "answers":["6", "8", "5", "7" ]
        },
        "6":{
            "text":"80÷5?",
            "answer":2,
            "answers":["31", "16", "8", "12" ]
        },
        "7":{
            "text":"72÷9?",
            "answer":1,
            "answers":["8", "0", "16", "9" ]
        },
        "8":{
            "text":"49÷7?",
            "answer":3,
            "answers":["5", "14", "7", "8" ]
        },
        "9":{
            "text":"27÷3?",
            "answer":2,
            "answers":["6", "9", "2", "3" ]
        },
        "10":{
            "text":"64÷8?",
            "answer":4,
            "answers":["6", "2", "5", "8" ]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success4.html')
            else:
                return render_template('quiz11.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong11.html', text="OOPS! wrong answer")
       else:
        return render_template('quiz11.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
