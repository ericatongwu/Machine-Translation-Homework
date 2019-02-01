from embedding import samples
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
import numpy as np

data_matrix = vectorizer.fit_transform()

feat_num = 20

# LSA
lsa = TruncatedSVD(feat_num, algorithm= 'arpack')
matrix_lsa = lsa.fit_transform(data_matrix)
matrix_lsa = Normalizer(copy=False).fit_transform(matrix_lsa)

if __name__ == "__main__":
	# print stop_words
	# print data_matrix.shape
	# plt.xlim([0, 100])
	# plt.plot(range(1, len(s)+1), s)	
	samples = list(matrix_lsa)
	for i in range(len(samples)):
		print samples[i]