import numpy as np
from sklearn import preprocessing

input_labels = ['red','black','red','green','black','yellow','white']

# creating label encoder
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)
print(list(encoder.classes_))

# encoding set of labels - no text in preprocessed data
test_labels = ['green','red','black','yellow']
encoded_values = encoder.transform(test_labels)
print("Labels =",test_labels)
print("Encoded Labels =",encoded_values)

# decoding encoded values
encoded_values = [1,2,3,0]
decoded_list = encoder.inverse_transform(encoded_values)
print("Decoded values = ",decoded_list)