# my new module

def get_tech_specs(computer):
	(memory, mem_units), (hd, hd_units) = computer['memory'], computer['storage']
	print '{} {} of memory, with a hard drive capacity of {} {}'.format(
		memory, mem_units, hd, hd_units
	)