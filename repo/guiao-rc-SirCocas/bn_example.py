
from bayes_net import *

# Exemplo dos acetatos:

bn = BayesNet()

bn.add('r',[],0.001)
bn.add('t',[],0.002)

bn.add('a',[('r',True ),('t',True )],0.950)
bn.add('a',[('r',True ),('t',False)],0.940)
bn.add('a',[('r',False),('t',True )],0.290)
bn.add('a',[('r',False),('t',False)],0.001)

bn.add('j',[('a',True )],0.900)
bn.add('j',[('a',False)],0.050)

bn.add('m',[('a',True )],0.700)
bn.add('m',[('a',False)],0.100)

conjunction = [('j',True),('m',True),('a',True),('r',False),('t',False)]

print(bn.jointProb(conjunction))

#_____________
practical = BayesNet()


practical.add('sc', [], 0.6)
practical.add('pt', [], 0.05)

practical.add('cp', [('sc', True), ('pa', True)], 0.02)
practical.add('cp' ,[('sc', True), ('pa', False)], 0.01)
practical.add('cp', [('sc', False), ('pa', True)], 0.011)
practical.add('cp', [('sc', False), ('pa', False)], 0.001)

practical.add('cnl', [('sc', True)],0.9)
practical.add('cnl', [('sc', False)], 0.001)

practical.add('pa', [('pt', True)], 0.25)
practical.add('pa', [('pt', False)], 0.004)

practical.add('fr', [('pt',True ), ('pa', True)], 0.9)
practical.add('fr', [('pt', True), ('pa', False)], 0.9)
practical.add('fr', [('pt', False), ('pa', True)], 0.1)
practical.add('fr', [('pt', False), ('pa', False)], 0.01)




allTrue = [('sc', True), ('cp',True),('cnl',True), ('pa',True), ('pt', True), ('fr', True)]
allFalse = [('sc', False), ('cp',False),('cnl',False), ('pa',False), ('pt', False), ('fr', False)]

print(practical.jointProb(allTrue))
print(practical.jointProb(allFalse))