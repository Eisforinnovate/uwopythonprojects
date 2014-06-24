# -*- coding: utf-8 -*-
#myself: Eric Dolan 250580207
#worked with Brad Pawson and Michael Kaptanknc
#Part 1: File I/O

def loaddata(filename) :
    
    #open CSV file with name filename & read contents
    #of file into a list of lists
    
    import csv
    
    reader = csv.reader(open(filename, 'r'))
    test_lists = []
    
    for r in reader:
        test_lists.append( [r[0],r[1],r[2],r[3],r[4],r[5]])
    return test_lists
    
def dat2arr(datalist) :

    #takes a list of lists and turns part of it into NumPy array
    #file in format [name, height(cm), weight(kg), 
    #stake aversion, garlic aversion, reflectance, shiny, IS_VAMPIRE?]
    
    import numpy 
    import scipy.io
    
    a = numpy.array(datalist)
    test_lists1 = a[:,1:5]
    b = test_lists1.astype(float)
    return b

    #When we convert to an array, we’ll drop the subject name,
    #and just convert the remaining entries. You should return a 
    #2D NumPy array where each row corresponds to one subject, 
    #and each column one measure.
  
    
def save_array(arr,fname) :

    #saves a 2D NumPy array arr to MATLABfile fname
    #with Python array arr stored as MATLAV array named vampire_array
    #First create a dictionary. Then add arr to the dictionary with 
    #the key vampire_array. Then use scipy.io.savemat to save the dictionary 
    #to a file.
    #First create a dictionary. Then add arr to the dictionary with the key 
    #vampire_array. Then use scipy.io.savemat to save the dictionary to a file.
    
    import numpy, scipy.io
    dict_arr = {}
    dict_arr["vampire_array"] = arr
    scipy.io.savemat('', mdict={'arr':arr})
    
    

#Part 2: Analysis and Visualization 
###analyze it to see if we can find measures that are repeatably 
###(across the whole population) different for vampires and non-vampires.
###Are vampires taller than non-vampires? More averse to garlic? etc

def column_stats(arr,col):
    import numpy 
    import pylab
   
    #will return a list of summary statistics 
    #(mean, min and max) for a particular column (col) in the array arr
    
    col_vampire = []
    col_normal= []
   
    #Creates two empty lists Vamp and Normal#
   
    for index, subject in enumerate(arr):
        if arr([index][7]) == 0.0:
            col_normal += [arr[index,col]]
            #Takes the numbers from the colum you choose and stores it in the normal list#
        else:
            col_vampire += [arr[index,col]]
            
            #Takes everything else and puts it in the Vamp list#
   
    vampires = numpy.array(col_vampire)
    normals = numpy.array(col_normal) 
   
   #Turns the columns into arrays#
  
    vamps_mean = vampires.mean()
    vamps_min = vampires.min()
    vamps_max = vampires.max()
    norms_mean = normals.mean()
    norms_min = normals.min()
    norms_max = normals.max()
    
    #Calculates the mean, min and maxes of both lists#
    
    compare_cols = [[vamps_mean, vamps_min, vamps_max], [norms_mean, norms_min, norms_max]]
    
    return compare_cols
    #Creates a new list with the seperated mean min and maxes for both vamps and normal#

def hist_compare(arr,col):
    import pylab
    
    #plot the histogram of values for a particular column"
    first = column_stats(arr, col)[0]
    second = column_stats(arr, col)[1]
    pylab.hist(first)
    pylab.hist(second)
    #Creates a histogram from the array and column#

def corr_columns(arr, column1, column2):
    "computes the Pearson Correlation between columns column1 and column2 in arr"
    import scipy.stats
    
    column_1 = arr[:,column1]
    column_2 = arr[:,column2]
    #Turns the columns into arrays#
    
    r_value = scipy.stats.pearsonr(column_1, column_2)
    #calcukates the pearson relation between the two columns#
    
    return r_value
    
    
def scatter_columns(arr, column1, column2):
    import pylab
   
    "that will produce a scatterplot of column1 of arr against column2"
   
    first_c = arr[:,][column1]
    second_c = arr[:,][column2]
    
    pylab.scatter(first_c, second_c)
    
    #truns the columns into arrays and thenturns them into a scater plot#

def is_vampire(row):
    
    #takes a 1-D array (row) of 6 measurements and returns a probability that the person with these measurements is a vampire"
    probability = 0
    
    if row[4] >= 0.9 or row[2] <= 0.08999 or row [3] <= 0.39:
        probability = 0.001
        return probability
        
        #if row 4 is so or row 2 is so or row 3 is so the probablity is 0.001#
        
    if row[4] <= 0.7199 or row[2] >= 1.09 or row[3] >= 0.76:
        probability = 0.999
        return probability
         
         #if row 4 is so or row 2 is so or row 3 is so the probablity is 0.999#
   
    if 0.71999 < row[4] <0.9 and 0.39 < row[3] <= 0.57:
        probability = 0.001
        return probability
        
         #if row 4 is so or row 2 is so or row 3 is so the probablity is 0.001#
         
    if 0.71999 < row[4] < 0.9 and 0.08999 < row[2] <= 0.40:
        probability = 0.001
        return probability
        # if row 4 is so or row 2 is so or row 3 is so the probablity is 0.001#
        
    if 0.7199 < row[4] < 0.9:
        probability = 0.07
        return probability
        # if row 4 is so or row 2 is so or row 3 is so the probablity is 0.07#
        
def is_vampire2(row):
    
    probability = 0
    
    if row[4] >= 0.9 or row[2] <= 0.08999 or row[3] <= 0.39 or 1.48 <= row[5] <= 1.63:
        probability = 0.001
        return probability
         
         #if row 4 is so or row 2 is so or row 3 is so the probablity is 0.001#
        
    if row[4] <= 0.71999 or row [2] >= 1.09 or row[3] >= 0.76 or -0.66 <= row[5] <= -0.54:
        probability = 0.999
        return probability
        
         #if row 4 is so or row 2 is so or row 3 is so the probablity is 0.999
        
    if 0.71999 < row[4] < 0.9 and 0.39 < row[3] <= 0.57:
        probability = 0.001
        return probability
        
    if 0.71999 < row[4] < 0.9 and 0.08999 < row[2] <= 0.40:
        probability = 0.001
        return probability
        # if row 4 is so or row 2 is so or row 3 is so the probablity is 0.001
        
    if 0.71999 < row[4] <0.9:
        probability = 0.07
        return probability
        #if row 4 is so or row 2 is so or row 3 is so the probablity is 0.07
        
def log_likelihood(arr, vamp_function):
    import numpy 
    "compare the is_vampire() functions"
    log_1 = 0
    #Initiates a counter#
    
    for row in arr:
        result = vamp_function(row)
        if row[6] == 1.0:
            log_1 += numpy.log(result)
            #logs the results if the person was a vampire and your results from your is_Vamp function to compare#
            
        else:
            log_1 += numpy.log(1-result)
            #If they are not a vampire it logs they were not does the opposite of the above line#
   
    return log_1