#Event numbers for neutrinos and antineutrinos
import sys
sys.path.append("..")
from SterileDar import constants as ct
from SterileDar import Oscspec
from SterileDar import crosssections
from SterileDar import expdata as exp
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


osc = Oscspec.Oscspec()
cs = crosssections.crosssections()

Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.5) #zero to half of muon energy

n = float(exp.hidrogeniototal) #number of protons at the detector

def dNdEvebar(Enu):
    return ((n*exp.estimatedflux)*osc.Oscspecvebar(exp.Ljsns2,Enu)*cs.sigmatot(Enu))/(4*np.pi*exp.Ljsns2**2)

x = [integrate.quad(lambda Enu: dNdEvebar(Enu), ct.energythresholdIBD, ct.muonmass/2)] #total number of neutrinos


plt.plot(Enu,dNdEvebar(Enu),'r',linewidth=1.0)
plt.title(u'dNdEvebar para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(u"Energia dos neutrinos [MeV]")
plt.ylabel(u"dN/dE [MeV⁻¹]")
plt.show()

print("Número total de Anineutrinos do elétron em um ano:{0}".format(x))


