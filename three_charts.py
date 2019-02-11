# three_charts.py

#
# CHART 1 (PIE)
#

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

import plotly
import plotly.graph_objs as go

print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data

#labels = ["Company X", "Company Y", "Company Z"]
#values = [0.55, 0.30, 0.15]

labels = []
values = []
for i in range(0,len(pie_data)): #in the list of dictionaries, with the range 0-end 
    labels.append(pie_data[i]['company'])
    values.append(pie_data[i]['market_share'])


layout = {'title': 'Industry market share'}
trace = go.Pie(labels=labels, values=values, title='Industry market share')


plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)



#
# CHART 2 (LINE)
#

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data) # TODO: create a line graph based on the line_data

x = []
y = []
for i in range(0, len(line_data)):
    x.append(line_data[i]['date']) #TODO help interpret this
    y.append(line_data[i]['stock_price_usd'])


plotly.offline.plot({
    "data": [go.Scatter(x=x, y=y)],  #adapted from the plotly package example on github
    "layout": go.Layout(title="Stock Prices Over Time")
}, auto_open=True)


#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

x = []
y = []
for i in range(0, len(bar_data)):
    y.append(bar_data[i]['genre']) 
    x.append(bar_data[i]['viewers'])

#import plotly.plotly as py     > do we not need to do this each time as long as we do so at the top?
#import plotly.graph_objs as go

data = [go.Bar(
            x=x,
            y=y,
            orientation = 'h'
)]

layout = go.Layout(title='Viewers Per Genre')
figure = go.Figure(data = data,layout=layout)
plotly.offline.plot(figure, filename='horizontal-bar.html', auto_open = True)