class DnaMatcher:
    def __init__(self, body_dna, parent_dna):
        self.body_dna = body_dna
        self.parent_dna = parent_dna

    def lcs_length(self):
        body_length = len(self.body_dna)
        parent_length = len(self.parent_dna)

        c = [[0] * (parent_length + 1) for _ in range(body_length + 1)]
        b = [[""] * (parent_length + 1) for _ in range(body_length + 1)]

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
