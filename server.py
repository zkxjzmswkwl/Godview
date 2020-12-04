from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

def geo_ip(ip):
    r = requests.get(f'https://ipinfo.io/{ip}')

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
def ip_to_coords(inc_ips):
    inc_ips = inc_ips.split(',')
    coords = {'results': []}

    for ip in inc_ips:
        coords['results'].append(geo_ip(ip))


    return jsonify(coords)

@app.route('/')
def godview():
    return render_template('godview.html')

