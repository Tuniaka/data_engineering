import json
import numpy as np	
		
def matrix_calculation(source_path):
	matrix = np.load(source_path)
	
	norm_matrix = (matrix - np.mean(matrix)) / np.std(matrix)
	np.save('result/task1/result.npy', norm_matrix)
	result = {'sum': int(np.sum(matrix)),
		      'avr': float(np.mean(matrix)),
		      'sumMD': int(np.sum(np.diag(matrix))),
		      'avrMD': float(np.mean(np.diag(matrix))),
		      'sumSD': int(np.sum(np.diag(np.fliplr(matrix)))),
		      'avrSD': float(np.mean(np.diag(np.fliplr(matrix)))),
		      'max': int(np.max(matrix)),
		      'min': int(np.min(matrix))}
	
	with open('result/task1/result.json', 'w') as f:
		json.dump(result, f)
        
		

if __name__ == '__main__':
	matrix_calculation('data/matrix_75.npy')