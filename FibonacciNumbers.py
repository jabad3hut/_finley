import locale


def fibonacciNumbersReturn(endPoint) :
	"""Print a Fibonacci series up to n."""
	locale.setlocale(locale.LC_ALL, 'en_US')
	a, b = 0, 1 
	result = []
	while b < endPoint:
		forma = locale.format("%d", b, grouping=True)
		result.append(forma)
		a , b = b , b+a
	return result
