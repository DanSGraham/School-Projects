from pybrain.datasets    import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer




#there is an error in the pybrain split data so we have to do it the hard way.
def splitData(ds,percentage):
    
    #ds._convertToOneOfMany()
   #shift through data
    tstdata_temp, trndata_temp = ds.splitWithProportion(percentage )

    #split returns the wrong type :(, have to move data over)
    tstdata = ClassificationDataSet(ds.indim, ds.outdim,ds.nClasses)#,nb_classes=ds.nb_classes)
    for n in xrange(0, tstdata_temp.getLength()):
        tstdata.addSample( tstdata_temp.getSample(n)[0], tstdata_temp.getSample(n)[1] )

    trndata = ClassificationDataSet(ds.indim, ds.outdim,ds.nClasses)#,nb_classes=ds.nb_classes)
    for n in xrange(0, trndata_temp.getLength()):
        trndata.addSample( trndata_temp.getSample(n)[0], trndata_temp.getSample(n)[1] )

    print type(tstdata),type(trndata)
    trndata._convertToOneOfMany( )
    tstdata._convertToOneOfMany( )    
    return trndata,tstdata


def measuredLearning(ds):

    trndata,tstdata = splitData(ds,.025)

    #build network


    ###
    # This network has no hidden layters, you might need to add some
    ###
    fnn = buildNetwork( trndata.indim, 22, trndata.outdim, outclass=SoftmaxLayer )
    trainer = BackpropTrainer( fnn, verbose=True,dataset=trndata)
                               
    ####
    #   Alter this to figure out how many runs you want.  Best to start small and be sure that you see learning.
    #   Before you ramp it up.
    ###
    for i in range(150):
        trainer.trainEpochs(5)
   
        
        trnresult = percentError(trainer.testOnClassData(),trndata['class'] )

        
        tstresult = percentError( trainer.testOnClassData(
           dataset=tstdata ), tstdata['class'] )

        print "epoch: %4d" % trainer.totalepochs, \
            "  train error: %5.2f%%" % trnresult, \
            "  test error: %5.2f%%" % tstresult
        if(trnresult<.5): 
            return

def main():
    DS = ClassificationDataSet.loadFromFile("ClassifierDataSet")
    print DS.calculateStatistics()

    print type(DS)
    rates = measuredLearning(DS)
main()
