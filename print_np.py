import numpy as np

'''result1 = np.load('elmo/raw_vector_train.npy')
result2 = np.load('elmo/raw_vector_test.npy')


#print(len(result1[0][0]), len(result1[0][1]), len(result2[23][1]))
train_zero = np.zeros((len(result1), 256, 256))
test_zero = np.zeros((len(result2), 256, 256))

index1 = 0
for line in result1:
	index2 = 0
	for i in line:
		train_zero[index1][index2] = i
		index2 += 1

	index1 += 1

index1 = 0
for line in result2:
	index2 = 0
	for i in line:
		test_zero[index1][index2] = i
		index2 += 1
	index1 += 1


np.save('elmo/pad_vector_train',train_zero)
np.save('elmo/pad_vector_test', test_zero)

'''
result1= np.load('elmo/pad_vector_train.npy')
result2= np.load('elmo/pad_vector_test.npy')

print(result1)
