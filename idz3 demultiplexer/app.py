from flask import Flask
from flask import  render_template, request, jsonify

from decoder import demultiplexer

app = Flask(__name__)

dedemu = demultiplexer()
inlines = [0,0,0]
Din = [0]

@app.route("/")
def main_page():
    return render_template("main.html")

@app.route('/update_toggle', methods=['POST'])
def update_toggle():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("No JSON data received")
        slider_id = data.get('id')
        slider_state = data.get('state')

        if slider_id is None or slider_state is None:
            raise ValueError("Invalid JSON data received")
        
        if data.get('id')[3]=="0":
            Din[0] = int(data.get('state'))
            print(data)
        else:
            print(Din[0])
            inlines[2-int(data.get('id')[-1])] = int(data.get('state'))
            print(inlines)
        
        dedemu.outline = dedemu.demultiplex(Din[0], inlines)

        return jsonify({
            'status': 'success',
            'message': 'Slider states updated',
            'rightSliders': dedemu.outline
        })
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 400
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)
