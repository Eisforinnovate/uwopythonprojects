# -*- coding: utf-8 -*-
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
    
    #will return a list of summary statistics 
    #(mean, min and max) for a particular column (col) in the array arr
    
    #summary stats for vampires and non-vampires should be returned 
    #separately (so you can compare them). 
    
    #Are there particular measures (columns) for which the values really 
    #look different for vampires and non-vampires?