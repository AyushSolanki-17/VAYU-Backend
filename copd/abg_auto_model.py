import os
import pickle

from copd.models import AbgAutoTest

modulepath = os.path.dirname(__file__)
abgAutoModelPath = os.path.join(modulepath, 'mlmodels/abg_auto.sav')
file = open(abgAutoModelPath, 'rb')
model = pickle.load(file)


def abg_auto_disorder_predict(abg: AbgAutoTest):
    return model.predict([[abg.ph, abg.pao2, abg.paco2, abg.hco3, abg.o2sat]])