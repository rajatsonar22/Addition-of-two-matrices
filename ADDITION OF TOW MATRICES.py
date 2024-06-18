# Addithion of two matrices
x = [ [1],[7],[3],
       [4],[5],[6],
       [7],[8],[9] ]
y = [ [2],[5],[7],
      [1],[5],[2],
      [1],[8],[9] ]
result = [[0],[0],[0],
          [0],[0],[0],
          [0],[0],[0]]

for i in range (len(x)):
    for j in range (len(y)):
        result [i][j] = x[i][j] + y[i][j]
for r in result:
    print(r)
