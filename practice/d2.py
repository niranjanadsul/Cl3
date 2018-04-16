def lcg():
	a=100078
	seed=18920
	c=1435
	m=pow(2,20)
	seed=(a*seed+c)%m
	return seed

fp=open("lcg.txt","w")
fp.write(str(lcg()))
fp.close()
