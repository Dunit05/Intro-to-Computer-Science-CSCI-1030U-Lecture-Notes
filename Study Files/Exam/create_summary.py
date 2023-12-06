# Write a function (create_summary) that takes two arguments:

# input_filename (a string)
# output_filename (a string)


# This function will open the file with the name input_filename for reading, and will process the data in that file.  Your program will find the name of the product name that has the minimum price (called cheapest_product in the output file), the product name with the maximum price (called costliest_product in the output file), and the average price (called avg_price in the output file).  The product name is in the 2nd value/column, and the price is in the last value/column.  It will generate a summary JSON file with the filename output_filename, using the json library.


# Note: For this function, you are not allowed to use any library to load the CSV file (including the csv library).


# Sample input file:

# 1,RTX3060,12GB,329.99

# 2,RTX3070,8GB,499.99

# 3,RTX3080,10GB,1499.99

# 4,RTX3090,24GB,1999.99


# Sample output file corresponding to the above sample input file (formatted for readability only):

# >>> create_summary('input_data.txt', 'results.json')

# {

# "cheapest_product": "RTX3060",

# "costliest_product": "RTX3090",

# "average_price": 1082.49

# }
