import statistics
def calc(numbers):
	average = statistics.mean(numbers)
	med = statistics.median(numbers)
	max_number = max(numbers)
	return (average, med, max_number)
