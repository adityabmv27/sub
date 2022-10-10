
from unicodedata import name
import pandas as pd
from flask import Flask,render_template, request
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import numpy as np


app = Flask(__name__, static_folder="static")
database_connection = create_engine('mysql+pymysql://root:aditya9499@localhost/game')
game_dict={}

def get_DataFrame(game_dict):
    game_data=pd.DataFrame(game_dict)
    return game_data

@app.route("/", methods=['GET'])
def main_page():
    print("App Running")
    return render_template('home.html')


@app.route("/results", methods=['GET'])
def results_page():

    get_DataFrame(game_dict).to_sql(con=database_connection,name='statistics', if_exists='replace', index=False)

    
    return "Ok Results Saved !"


@app.route("/", methods=['POST'])
def get_data():
    #Data(Who is the winner)
    
    data = request.form
    if data['O'] not in game_dict.keys():
        game_dict[data['O']] =  [0,0]
    if data['X'] not in game_dict.keys():
        game_dict[data['X']] = [0,0]
    print(data)
    if data['O'] != '' and data['X'] != '' and data['winner'] != '':
        if data['winner'] == 'O':
            game_dict[data['O']][0] += 1
            game_dict[data['X']][1] += 1
        elif data['winner'] == 'X':
            game_dict[data['X']][0] += 1
            game_dict[data['O']][1] += 1
    print(get_DataFrame(game_dict))
    return render_template('home2.html', name1 =data['O'], name2 = data['X'] )

if __name__ == "__main__":
    app.run(debug=True)