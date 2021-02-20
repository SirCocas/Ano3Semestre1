import pytest
from bayes_net import *

@pytest.fixture
def bn():
    
    bn = BayesNet()

    bn.add('sc',[],0.6)
    bn.add('pt',[],0.05)

    bn.add('cp',[('sc',True ),('pa',True )],0.02)
    bn.add('cp',[('sc',True ),('pa',False)],0.01)
    bn.add('cp',[('sc',False),('pa',True )],0.011)
    bn.add('cp',[('sc',False),('pa',False)],0.001)

    bn.add('fr',[('pt',True ),('pa',True )],0.90)
    bn.add('fr',[('pt',True ),('pa',False)],0.90)
    bn.add('fr',[('pt',False),('pa',True )],0.10)
    bn.add('fr',[('pt',False),('pa',False)],0.01)

    bn.add('pa',[('pt',True )],0.25)
    bn.add('pa',[('pt',False)],0.004)

    bn.add('cnl',[('sc',True )],0.90)
    bn.add('cnl',[('sc',False)],0.001)

    return bn

def test_exercicio15(bn):
    assert round(bn.individualProb('pa', True),5) == 0.0163
