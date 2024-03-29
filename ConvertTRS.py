# Convert trace file to arrays; print some of their statistics and values
import trsfile

with trsfile.open('90x500xfloat.trs', 'r') as traces:
	# Show all headers
	for header, value in traces.get_headers().items():
		print(header, '=', value)
  
	# Iterate over the first 25 traces
	for i, trace in enumerate(traces[0:25]):
		print('Trace {0:d} contains {1:d} samples'.format(i, len(trace)))
		print('  - minimum value in trace: {0:f}'.format(min(trace)))
		print('  - maximum value in trace: {0:f}'.format(max(trace)))
	for value in traces[0]: print(value)
  
  