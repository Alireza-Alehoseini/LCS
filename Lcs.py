class DnaMatcher:
    def __init__(self, body_dna, parent_dna):
        self.body_dna = body_dna
        self.parent_dna = parent_dna

    def lcs_length(self):
        body_length = len(self.body_dna)
        parent_length = len(self.parent_dna)

        c = [[0] * (parent_length + 1) for _ in range(body_length + 1)]
        b = [[""] * (parent_length + 1) for _ in range(body_length + 1)]
            
        """
        for i in range(1, body_length + 1):           
            c[i][0] = 0
    
        for j in range(parent_length + 1):
            c[0][j] = 0
        """

        for i in range(1, body_length + 1):
            for j in range(1, parent_length + 1):
                if self.body_dna[i - 1] == self.parent_dna[j - 1]:
                    c[i][j] = c[i - 1][j - 1] + 1
                    b[i][j] = "↖"
                elif c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = "↑"
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = "←"

        return self.print_lcs(b, body_length, parent_length)

    def print_lcs(self, b, i, j):
        result = ""
        if i == 0 or j == 0:
            return result

        if b[i][j] == "↖":
            result += self.print_lcs(b, i - 1, j - 1)
            result += self.body_dna[i - 1]
        elif b[i][j] == "↑":
            result += self.print_lcs(b, i - 1, j)
        else:
            result += self.print_lcs(b, i, j - 1)

        return result


class DnaFileHandler:
    def __init__(self, body_filename, parents_filename, result_filename):
        self.body_filename = body_filename
        self.parents_filename = parents_filename
        self.result_filename = result_filename

    def read_body_dna(self):
        with open(self.body_filename, 'r') as f:
            return f.readline().strip()

    def read_parents_dna(self):
        parents_dna = []
        with open(self.parents_filename, 'r') as f:
            for line in f:
                parents_dna.append(line.strip())
        return parents_dna

    def write_results(self, results):
        with open(self.result_filename, 'w') as f:
            f.write('\n'.join(results))


def compare_dna(body_dna, parent_dna):
    dna_matcher = DnaMatcher(body_dna, parent_dna)
    return dna_matcher.lcs_length()


def run_dna_comparison():
    body_filename = "C:/Users/Admin/Desktop/body_dna.txt"   # input.txt
    parents_filename = "C:/Users/Admin/Desktop/parents_dna.txt"   # input.txt
    result_filename = "C:/Users/Admin/Desktop/result.txt"   #output.txt        

    dna_file_handler = DnaFileHandler(body_filename, parents_filename, result_filename)

    body_dna = dna_file_handler.read_body_dna()
    parents_dna = dna_file_handler.read_parents_dna()

    results = []
    for parent_dna in parents_dna:
        result = compare_dna(body_dna, parent_dna)
        results.append(body_dna+"    "+parent_dna+"    "+result)

    dna_file_handler.write_results(results)


if __name__ == "__main__":
    run_dna_comparison()
