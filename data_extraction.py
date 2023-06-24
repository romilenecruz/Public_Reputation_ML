import cv2 #importing necessary libraries
import pytesseract #importing necessary libraries
import pandas as pd #importing necessary libraries
import os #importing necessary libraries
from datetime import datetime #importing necessary libraries

tesseract_path = 'C:/Program Files/Tesseract-OCR/tesseract.exe' #hard coding the path to Tesseract-OCR

def data_extraction(image, source_path): #function "image_resize" has 2 arguments. it needs the image and the srouce path
    pytesseract.pytesseract.tesseract_cmd = tesseract_path #setting pytesseract to the tesseract path
    img = cv2.imread(image) #getting the image and setting it to the 'img' variable
    cropped = img[0:520, 540:660] #cropping the 'img' variable to only focus on the column for the streams on that given day 
    text = pytesseract.image_to_string(cropped) #using the OCR to read the text in the cropped image, saves it as a string
    text_to_list = text.split('\n') #splitting the string by the newline seperator into a list called 'text_to_list'

    prefixed_removed = image.removeprefix(source_path) #removing the source path from the 'image' string to leave us with the file name
    suffix_removed = prefixed_removed.removesuffix('.png_new.png') #removing the suffix of the file name to leave us with the core file name

    filename = suffix_removed #saving the core file name in the variable 'filename'

###### REMOVING THE LEADING AND TRAILING CHARACTERS IN THE LIST ######
    index = 0 #setting the index to be 0
    for item in text_to_list: #iterate thorugh the text_to_list list
        text_to_list[index] = item.strip() #going through the list index by index and stripping the leading and trailing characters in the list
        index += 1 #adding 1 to the index

###### REMOVING THE EMPTY INDICES IN THE LIST ######
    while("" in text_to_list): #while there is an empty in the list
        text_to_list.remove("") #remove the empty

###### SETTING THE COLUMN NAME TO BE THE DATE AKA THE FILENAME ######
    try:
        text_to_list[0] = filename #putting 'filename' into the 0 index
        temp = datetime.strptime(filename, '%m.%d.%Y').strftime('%Y/%m/%d') #taking the filename and converting it to the correct datetime format and save it in the 'temp' variable
        text_to_list[0] = temp #put the 'temp' back to the 0 index
    except Exception: #catching the exceptions
        pass

###### TAKING THE $ OUT OF THE STRING IN EACH INDEX OF THE LIST ######
    try:
        for i in range(1, len(text_to_list)): #start iterating at index 1 until the length of the text_to_list
            if '$' in text_to_list[i]: #if there's '$'
                no_dollar = text_to_list[i].replace('$', '') #replace the $ with no space and save the new string in the variable 'no_dollar'
                text_to_list[i] = no_dollar #put the 'no_dollar' varuable back into the index that we found it at
            else: #if there is NO '$'
                pass #do nothing
    except Exception: #catching the exceptions
        pass #do nothing

###### TAKING THE EMPTY SPACES OUT OF THE STRING IN EACH INDEX OF THE LIST ######
    try:
        for i in range(1, len(text_to_list)): #start iterating at index 1 until the length of the text_to_list
            if " " in text_to_list[i]: #if there's an empty space
                no_space = text_to_list[i].replace(" ", "") #replace the empty space with no space and save the new string in the variable 'no_space'
                text_to_list[i] = no_space #put the 'no_space' variable back into the index that we found it at
            else: #if there is NO empty space
                pass #do nothing
    except Exception: #catching the exceptions
        pass #do nothing

###### TAKING THE COMMAS OUT OF THE STRING IN EACH INDEX OF THE LIST ######
    try:
        for i in range(1, len(text_to_list)): #start iterating at index 1 until the length of the text_to_list
            if ',' in text_to_list[i]: #if there's a comma
                new_value = text_to_list[i].replace(',', '') #replace the comma with no space and save the new string in the variable 'new_value'
                text_to_list[i] = new_value #put the 'new_value' variable back into the index that we found it at
            else: #if there's no comma
                text_to_list[i] = 0 #put 0 in the index we are at
    except Exception: #catching the exceptions
        pass #do nothing

###### CONVERTING EACH STRING TO A FLOAT ######
    try:
        for i in range(1, len(text_to_list)): #start iterating at index 1 until the length of the text_to_list
            if isinstance(text_to_list[i],str): #if the item at the index is a string
                new_value = float(text_to_list[i]) #make the string a float and save it in the 'new' variable
                text_to_list[i] = new_value #put the 'new' variable at the index that we found it at
            else: #if it is not a string
                text_to_list[i] = 0 #put 0 in the index we are at
    except Exception: #catching the exceptions
        pass #do nothing

    df = pd.DataFrame(text_to_list, columns=[text_to_list[0]]) #putting the list into a data frame and setting the column name to be the item at index 0

    df2 = df.drop(0) #dropping the item at index 0

    if df2.shape[0] == 16: #if the number of rows is 16
        df2 = df2.drop(16) #drop the 16th row

    df2.reset_index(inplace = True, drop = True) #resetting the index so that it starts at 0

    return df2 #returning the dataframe