import json
import plotly
import pandas as pd
from flask import Flask
from flask import render_template
from plotly.graph_objs import Bar



app = Flask(__name__)

# load data

df = pd.read_csv('./data/data.csv')
print(df.head())
# index webpage displays  visuals
@app.route('/')
def index():
    """Website index.
    Returns:
        html: Webpage with plot.
    """
    
    # extract data needed for visuals
    category_returns = df.groupby('category').mean()['return_net_5y']
    category_names = list(category_returns.index)

    
         # create visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=category_names,
                    y=category_returns
                )
            ],

            'layout': {
                'title': 'AVG 5Y RETURN BY ASSET CATEGORY',
                'yaxis': {
                    'title': "AVG 5Y NET RETURN"
                },
                'xaxis': {
                    'title': "ASSET CATEGORY"
                }
            }
        }
     ]
    

    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 