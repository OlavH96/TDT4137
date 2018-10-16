from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import TanhLayer
from pybrain.datasets import SupervisedDataSet as DS
import math

ds = DS(1, 1)
for i in range(1, 9):
    ds.addSample(i, i)

print(ds)

for i in range(1, 9):

    net = buildNetwork(1, i, 1, hiddenclass=TanhLayer)

    trainer = BackpropTrainer(net, ds)
    trainer.trainUntilConvergence(verbose=False, validationProportion=0.15, maxEpochs=1000, continueEpochs=10)

    print("Hidden nodes", i)
    error = 0
    for j in range(1, 9):
        res = net.activate([j])
        print("Expected", j, "got", res)
        error += math.sqrt((j - res[0]) ** 2)
    print("Sum errors is", error)
    print("avg error is", error / 8)

    if i == 2: # 8 hiden nodes
        print("15",net.activate([15]))
        print("-5",net.activate([-5]))
        print("5.5",net.activate([5.5]))
        print(net.params)




    net = None # Not sure if you need to do this
    trainer = None # Not sure if you need to do this as well
