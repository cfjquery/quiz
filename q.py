import unittest

series = [100, 300, 100, 50, 50, 50, 50, 50, 500, 200, 100]
threshold = 500

def subSeries(series,threshold):
	currentTotal = 0
	counter = 0
	tempSeries = []
	longestSeries = []
	while len(series) > 0:
		currentTotal += series[counter]
		if currentTotal > threshold:
			if len(tempSeries) > len(longestSeries):
				longestSeries = tempSeries
			series.pop(0)
			tempSeries = []
			counter = 0
			currentTotal = 0
		else:
			tempSeries.append(series[counter])
			counter += 1
		if counter >= len(series):
			if len(tempSeries) > len(longestSeries):
				longestSeries = tempSeries
			break
	return longestSeries

class subSeriesTest(unittest.TestCase):
    def test(self):
    	threshold = 500
    	
    	emptyArray = []
    	singleValueArrayLessThanOrEqualToThreshold = [500]
    	singleValueArrayGreaterThanThreshold = [501]
    	mutipleValueArray1 = [100, 300, 100, 50, 50, 50, 50, 500, 200, 100]
    	mutipleValueArray2 = [100, 300, 100, 50, 50, 50, 50, 50, 500, 200, 100]
    	mutipleValueArray3 = [100, 300, 100, 50, 50, 50, 50, 50, 500, 200, 100, 1, 2, 3, 4, 5, 6, 7]
    	mutipleValueArrayWhereAllElementsAreGreaterThanTheThreshold = [501 , 501 ,502 ,600 ,700 ,502 ,501]

        self.assertEqual(subSeries(emptyArray,500), [])
        self.assertEqual(subSeries(singleValueArrayLessThanOrEqualToThreshold,500), [500])
        self.assertEqual(subSeries(singleValueArrayGreaterThanThreshold,500), [])
        self.assertEqual(subSeries(mutipleValueArray1,500), [100, 50, 50, 50, 50])
        self.assertEqual(subSeries(mutipleValueArray2,500), [100, 50, 50, 50, 50, 50])
        self.assertEqual(subSeries(mutipleValueArray3,500), [200, 100, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(subSeries(mutipleValueArrayWhereAllElementsAreGreaterThanTheThreshold,500), [])

print(subSeries(series,threshold))

subSeriesTest(unittest.main())

