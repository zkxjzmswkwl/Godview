from flask import Flask, render_template, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__, static_url_path='/static', static_folder='templates')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def geo_ip(ip):
    print(ip)
    r = None

    if len(ip) > 1:
        r = requests.get(f'https://ipinfo.io/{ip}/geo')
    else:
        return

    if 'bogon' in r.json():
        return {'bogon': True}

    lat_long = r.json()['loc'].split(',')

    return {
            'city': r.json()['city'],
            'state': r.json()['region'],
            'lat': lat_long[0],
            'long': lat_long[1]
            }

@app.route('/ip_to_coords/<inc_ips>')
@cross_origin()
def ip_to_coords(inc_ips):
    inc_ips = inc_ips.split(',')
    coords = {'results': []}

    for ip in inc_ips:
        coords['results'].append(geo_ip(ip))

    return jsonify(coords)

@app.route('/')
def godview():
    return render_template('index.html')

