def eval_expr(s,d={}):

	cisla= []
	
	for k in ( s.split() ):
		if k=="+":
			a = cisla.pop(0)
			if a in d:
				a=d[a]
			b = cisla.pop(0)
			if b in d:
				b=d[b]
			cisla.append(int(a) + int(b))
			
		elif k=="-":
			a = cisla.pop(0)
			if a in d:
				a=d[a]
			b = cisla.pop(0)
			if b in d:
				b=d[b]
				
			cisla.append(int(a) - int(b))
			
		elif k=="*":
			a = cisla.pop(0)
			if a in d:
				a=d[a]
			b = cisla.pop(0)
			if b in d:
				b=d[b]
			cisla.append(int(a) * int(b))
			
		elif k=="/":
			a = cisla.pop(0)
			if a in d:
				a=d[a]
			b = cisla.pop(0)
			if b in d:
				b=d[b]
			cisla.append(int(a) / int(b))
			
		else:
			cisla.append(k)
	
	return(cisla[0])
	
	
	
	
	
def to_infix(s):
	s = s.replace(' ','')
	to_ret=''
	znaky=[]
	
	for i in s:
		if i == '+':
			znaky.insert(0,"( ")
			znaky.insert(-1," + ")
			znaky.append(" ) ")
					
		elif i == '-':
			znaky.insert(0,"( ")
			znaky.insert(-1," - ")
			znaky.append(" ) ")
			
		elif i == '*':
			znaky.insert(0,"( ")
			znaky.insert(-1," * ")
			znaky.append(" ) ")
			
		elif i == '/':
			znaky.insert(0,"( ")
			znaky.insert(-1," / ")
			znaky.append(" ) ")
			
		else:
			znaky.append(i)
	
	for j in znaky:
		to_ret = to_ret + j
		
	return to_ret


def to_postfix(s):

	znaky=[]
	to_ret=""
	znamienka=[]

	
	for i in ( s.split() ):

		if i == ")":
			znaky.append(znamienka.pop())
		elif i == "(":
			pass	
		elif i == '+' or i == '-' or i == '*' or i == '/':
			znamienka.append(i)
		else:
			znaky.append(i)
	
		
	for j in znaky:
		to_ret = to_ret + j + " "
		
	to_ret = to_ret[:-1]
		
	return to_ret
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		














