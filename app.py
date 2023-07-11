from flask import Flask, request, jsonify
from dna_matcher import DnaMatcher, DnaFileHandler

app = Flask(__name__)

@app.route('/compare-dna', methods=['POST'])
def compare_dna():
    body_dna = request.json['body_dna']
    parents_dna = request.json['parents_dna']

    dna_matcher = DnaMatcher(body_dna, parents_dna)
    dna_file_handler = DnaFileHandler("body_dna.txt", "parents_dna.txt", "result.txt")

    results = []
    for parent_dna in parents_dna:
        result = dna_matcher.compare_dna(body_dna, parent_dna)
        results.append(body_dna + "    " + parent_dna + "    " + result)

    dna_file_handler.write_results(results)

    return jsonify({'results': results})


if __name__ == "__main__":
    app.run()
