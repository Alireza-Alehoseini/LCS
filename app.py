from flask import Flask, render_template, request, jsonify
from dna_comparison import DnaMatcher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare_dna', methods=['POST'])
def compare_dna():
    data = request.get_json()
    body_dna = data['body_dna']
    parents_dna = data['parents_dna']

    results = []
    for parent_dna in parents_dna.split('\n'):
        dna_matcher = DnaMatcher(body_dna, parent_dna)
        result = dna_matcher.lcs_length()
        results.append(f'{body_dna}    {parent_dna}    {result}')

    return jsonify(results)

if __name__ == '__main__':
    app.run()
