from data_extraction import * #importing everything from the function file function
from resize_images import * #importing everything from the resize_images file function
from numpy import inner #importing necessary libraries
import warnings #importing necessary libraries

warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning) #ignoring the warning I get

data_source = "F:/Romilene/Main/2023 Projects/Machine Learning/Taylor Swift/Reputation/Data/Pictures/PNG/" #setting the data_source path

final_destination = "F:/Romilene/Main/2023 Projects/Machine Learning/Taylor Swift/Reputation/Data/Pictures/RESIZED/" #setting the final_destination path

image_resize(data_source, final_destination) #resizing the imaged in the data_source path and putting them into the final_destination path

#creating a data frame with the song_names
song_names = pd.DataFrame({'Song Name': ['... Ready For It?', 'End Game', 'I Did Something Bad', 'Dont Blame Me',
                                         'Delicate', 'Look WhatYou Made Me Do', 'So It Goes...', 'Gorgeous', 'Getaway Car',
                                         'King of My Heart', 'Dancing With Our Hands Tied', 'Dress', 'This Is Why We Cant Have Nice Things',
                                         'Call It What You Want', 'New Years Day']})

empty_df = pd.DataFrame() #creating an empty data frame

for filename in os.listdir(final_destination): #iterate through the final_destination file path
    f = os.path.join(final_destination, filename) #joining the source file path and the file name /final_destination/filename and saving in variable 'f'

    if f.endswith('.png'): #if 'f' ends with '.png'
        index = 0 #setting the index to be 0
        data = data_extraction(f, final_destination) #passing the 'f' variable into the data_extraction function
        empty_df.insert(index, data.columns[0], data) #inserting the data into the empty data frame at the index
        index += 1 #add 1 to the index

result_df = empty_df.sort_index(axis=1) #sorting the "empty_df" by the columns and saving it in the 'result_df' variable

final_df = pd.concat([song_names, result_df], axis=1, join='inner') #combining the song_names and result_df to make the final data frame

final_df.to_excel(r'F:/Romilene/Main/2023 Projects/Machine Learning/Taylor Swift/Reputation/Data/DF_EXCEL/all_data_8.xlsx', index=False) # exporting the final_df to an excel file