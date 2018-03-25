from random import randint
import dash_core_components as dcc
import dash_html_components as html
import requests

def index():
    ''' '''
    return 'Welcome to index page'


def fig1(id=205):
    ''' '''
    # if id:
    host = 'http://127.0.0.1:8000'
    url = '/api/graph_data/{}?format=json'.format(id)
    data_dict = requests.get(host+url).json()
    graph_url = '/api/graph/details/{}?format=json'.format(id)
    graph_dict = requests.get(host+graph_url).json()
    # print(my_dict)

    plot_data = []
    for obj in data_dict:
        plot_data.append({
            'name': obj['series_name'],
            'mode': 'line',
            'type': 'scatter',
            'x': obj['x'],
            'y': obj['y'],
        })

    x_title = '{} ({})'.format(graph_dict['x_axis_type'],graph_dict['x_axis_unit'])
    y_title = '{} ({})'.format(graph_dict['y_axis_type'],graph_dict['y_axis_unit'])

    return dcc.Graph(
        id='main-graph',
        figure={
            # 'data': [{
            #     'name': 'Some name',
            #     'mode': 'line',
            #     'type': 'scatter',
            #     'x': my_dict[0]['x'],
            #     'y': my_dict[0]['y']
            # }],
            'data': plot_data,
            'layout': {
                'autosize': True,
                'width': 600,
                # 'scene': {
                    # 'bgcolor': 'rgb(255, 255, 255)',
                    'xaxis': {
                        # 'titlefont': {'color': 'rgb(0, 0, 0)'},
                        # 'title': 'X-AXIS',
                        'title': x_title,
                        # 'color': 'rgb(0, 0, 0)'
                    },
                    'yaxis': {
                        # 'titlefont': {'color': 'rgb(0, 0, 0)'},
                        'title': y_title,
                        # 'color': 'rgb(0, 0, 0)'
                    }
                # }
            }
        }
    )


def fig2():
    ''' '''
    return dcc.Graph(
        id='main-graph',
        figure={
            'data': [{
                'name': 'Some name',
                'mode': 'line',
                'line': {
                    'color': 'rgb(0, 0, 0)',
                    'opacity': 1
                },
                'type': 'scatter',
                'x': [randint(1, 100) for x in range(20)],
                'y': [randint(1, 100) for x in range(20)]
            }],
            'layout': {
                'autosize': True,
                'scene': {
                    'bgcolor': 'rgb(255, 255, 255)',
                    'xaxis': {
                        'titlefont': {'color': 'rgb(0, 0, 0)'},
                        'title': 'X-AXIS',
                        'color': 'rgb(0, 0, 0)'
                    },
                    'yaxis': {
                        'titlefont': {'color': 'rgb(0, 0, 0)'},
                        'title': 'Y-AXIS',
                        'color': 'rgb(0, 0, 0)'
                    }
                }
            }
        }
    )
