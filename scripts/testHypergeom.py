


universeList = allLINCS
pertubList = pertubDOWN
sampleList = sampleUP

M = len(universeList)
n = len(list(set(covertListToUpper(perturbList)) & set(covertListToUpper(universeList))))
N = len(set(sampleList))
x = len(list(set(covertListToUpper(perturbList)) & set(covertListToUpper(sampleList))))
rv = hypergeom(M, n, N)
print (1 - rv.cdf(x))

print (len(set(sampleUP)))
print (len(set(perturbDOWN)))
print (len(set(allLINCS)))
pval = getHyperGeomPvalue(perturbDOWN,sampleUP,allLINCS)
print (pval)

