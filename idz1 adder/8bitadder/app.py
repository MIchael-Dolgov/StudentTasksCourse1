from flask import Flask
from flask import  render_template, request

from twos_complement import twos_complement_to_decimal, to_decimal

from circuts import eight_bit_full_adder

app = Flask(__name__)

nums = [[False for _ in range(8)], [False for _ in range(8)]]

@app.route("/")
def main_page():
    nums = [[False for _ in range(8)], [False for _ in range(8)]]
    return render_template("main.html")

@app.route('/update_toggle', methods=['POST'])
def update_toggle():
    #num1/2 = [3] indx = [-1]
    id = request.form['id']
    status = request.form['status']
    isminus = True if request.form['sign'] == "true" else False
    if (len(id)!=1):
        nums[int(id[3])][(int(id[-1]))] = True if status == "true" else False
    if (isminus):
        return [eight_bit_full_adder(0, nums[0], nums[1]), (twos_complement_to_decimal(''.join(str(int(v)) for v in nums[0]))), (twos_complement_to_decimal(''.join(str(int(v)) for v in nums[1]))), 
                (twos_complement_to_decimal(''.join(str(int(v)) for v in eight_bit_full_adder(0, nums[0], nums[1])[1])))]
    else: 
        return [eight_bit_full_adder(0, nums[0], nums[1]), (to_decimal(''.join(str(int(v)) for v in nums[0]))), (to_decimal(''.join(str(int(v)) for v in nums[1]))), 
                (to_decimal(''.join(str(int(v)) for v in eight_bit_full_adder(0, nums[0], nums[1])[1])))]

if __name__ == "__main__":
    app.run(debug=True, port=5001)
