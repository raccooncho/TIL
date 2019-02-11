import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/ssafy')
def ssafy():
    return 'sssssssssafy'

@app.route('/hi/<string:name>')
def hi(name):
    return(f'hi {name}!')

@app.route('/keyword/<string:word>')
def keyword(word):
    return(f'{word} is nothing')

@app.route('/pick_lotto')
def pick_lotto():
    num_list = [str(i) for i in sorted(random.sample(range(1, 46), 6))]
    num = ' '.join(num_list)
    return num

@app.route('/dictionary/<string:word>')
def my_dictionary(word):
    my_dict = { 'apple': '사과', 'banana': '바나나', 'orange': '오렌지', 'coffe': '커피', 'human': '사람'}
    find_word = []
    for key, value in my_dict.items():
        if word == key:
            find_word.append(1)
    if 1 in find_word:
        return f'{word} is {my_dict[word]}'
    else:
        return f'{word} is not in my dictionary'

if __name__ == '__main__':
    app.run(debug=True)
