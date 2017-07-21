
# A very simple Bottle Hello World app for you to get started with...


from bottle import route, run, template, default_app

import json
import get_stream

@route("/")
@route("/index")
def index():
    data = get_stream.get_stream_data()
    #print(data)
    return template("""
        <b>
        An example weather server.
        </b>
        %for item in data:
            <b>
            {{item}}
            </b>
    """,data=data)

@route("/table")
def temperature():
    data = get_stream.get_stream_data()
    #print(data)
    return template("""
    <table>
    %for item in data:
        <tr>
        <td>
            {{item['kentid']}}
        </td>
        <td>
            {{item['collection_time']}}
        </td>
        <td>
            {{item['lat']}}
        </td>
        <td>
            {{item['lon']}}
        </td>
        <td>
            {{item['temperature']}}
        </td>
        <td>
            {{item['humidity']}}
        </td>
        </tr>
    %end
    </table>
    """, data=data)

@route("/graph")
def graph():
    data = get_stream.get_stream_data()
    return template("scatter_graph", data=data)

@route("/projectgraph")
def graph1():
    data = get_stream.get_stream_data()
    return template("project_graph", data=data)

@route("/map")
def example_map():
    data = get_stream.get_stream_data()
    return template("example_map", data=data)

@route("/map1")
def example_map1():
    data = get_stream.get_stream_data()
    return template("example_map1", data=data)

@route("/calendar_chart")
def calendar_chart():
    data = get_stream.get_stream_data()
    return template("calendar_chart", data=data)

application = default_app()

