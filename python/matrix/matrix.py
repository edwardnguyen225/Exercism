class Matrix:
    def __init__(self, matrix_string):
        tmp = matrix_string.split('\n')
        self.matrix = []
        for i in range(len(tmp)):
            tmp_row = tmp[i].split(' ')
            for j in range(len(tmp_row)):
                tmp_row[j] = int(tmp_row[j])
            self.matrix.append(tmp_row)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        output = []
        i = index - 1
        for row in self.matrix:
            output.append(row[i])
        return output
