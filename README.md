# Sports-Reference


My solution to the engineering problem was to use the Python json library to read json file data and then create an array of arrays that functions as a matrix. In the solution the code will read the json file using json.load() which creates a Python dictionary with keys that allow the data to be accesible later in the code. Then using a nested loop we can iterate over every team row by row and column by column which creates the matrix as for every team a row will be created of their wins against another team which builds columns. Each team will get a 0 when they have themselevs as no self matchups are allowed. As such this will create a matrix that will display all head-to-head win-loss records. With each row and column corresponding to a different team. 
