import pandas as pd
import os


dir_path = '/Users/yukinan/Documents/Coronavirus/Codes/TS_Rolling/20200928/Python_Code/Dataset/2020/'
include_list = ['Data1_tight.csv', 'Data2_Bounds.csv', 'Labels.csv']

df_temp = pd.DataFrame()
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file in include_list and not file.startswith('.'):
            df = pd.read_csv(dir_path+file)
            df_temp = pd.concat([df_temp,df], axis=0, join='outer')
    ID_set = set(df_temp.ID.tolist())
    for id in ID_set:
        new_df = df_temp[df_temp['ID']==id]
        new_df.sort_values(by='Date_time', ascending=True, inplace=True)
        dir_name = str(id)
        dir_save_path = dir_path + str('sum') + '/'
        if not os.path.exists(dir_save_path):
            os.makedirs(dir_save_path)
        new_filename = dir_save_path +str(id) + '.csv'
        new_df.to_csv(new_filename, index = False)
        print(new_filename)
            # dir_name = file.split('.')[0]
            # dir_path = root + '/' + dir_name +'.csv'
            # if not os.path.exists(dir_path):
            #         os.makedirs(dir_path)
            # file_path = root + '/' + file
            # print(file_path)
