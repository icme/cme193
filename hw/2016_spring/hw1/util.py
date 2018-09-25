class _register:
	n_pass = 0
	n_fail = 0

def test(statement, name):
	if statement:
		print '{}: PASS'.format(name)
		_register.n_pass += 1
	else:
		print '{}: FAIL'.format(name)
		_register.n_fail += 1

def summary():
	print '{} / {} tests passed.'.format(
		_register.n_pass, _register.n_pass + _register.n_fail)