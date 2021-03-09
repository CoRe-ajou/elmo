# #csv2txt
# import csv

# csv_file = '/content/drive/Shareddrives/2020융합/악플 데이터/youtube/labelling_result_test.csv'
# txt_file = '/content/drive/Shareddrives/2020융합/악플 데이터/youtube/labelling_result_test.txt'
# #'/content/drive/Shareddrives/2020융합/악플 데이터/youtube/labelling_result.csv'
# #'/content/drive/Shareddrives/2020융합/악플 데이터/youtube/labelling_result.txt'

# with open(txt_file, "w") as my_output_file:
#     with open(csv_file, "r") as my_input_file:
#         [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
#     my_output_file.close()

#########

import csv


test_path = 'elmo/data_test.csv'
train_path = 'elmo/data_train.csv'
f_test = open(test_path, 'r')
r_test = csv.reader(f_test)
f_train = open(train_path, 'r')
r_train = csv.reader(f_train)

vd_test_path = 'elmo/vec_data_test.csv'
vd_test = open(vd_test_path, 'a',newline='')
wrd_test = csv.writer(vd_test)

vl_test_path = 'elmo/vec_label_test.csv'
vl_test = open(vl_test_path, 'a',newline='')
wrl_test = csv.writer(vl_test)


vd_train_path = 'elmo/vec_data_train.csv'
vd_train = open(vd_train_path, 'a',newline='')
wrd_train = csv.writer(vd_train)

vl_train_path = 'elmo/vec_label_train.csv'
vl_train = open(vl_train_path, 'a',newline='')
wrl_train = csv.writer(vl_train)

for line in r_test:
    #wrd_test.writerow([line[0]])
    wrl_test.writerow([line[1]])
  
for line in r_train:
    #wrd_test.writerow([line[0]])
    wrl_test.writerow([line[1]])


