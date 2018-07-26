from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import getUsernameFromSiteDB
config = Configuration()

config.section_('General')
config.General.workArea = 'crab_multi_hcaltuple_badCapIDruns_cmslpc'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pfg_new2_Global_RAW_cfg.py'
config.JobType.pyCfgParams = ['outputFile=hcalTupleTree.root']

config.section_('Data')
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5
config.Data.lumiMask = ''
config.Data.outLFNDirBase = '/store/user/bchiari1/noreplica/hcal/task9/multirun_allbadcapid/'
config.Data.publication = False

config.section_('User')

config.section_('Site')
config.Site.storageSite = "T3_US_FNALLPC"


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    config.General.requestName = 'hcaltuple_run316110'
    config.Data.outputDatasetTag = "hcaltuple_run316110"
    config.Data.inputDataset = '/ZeroBias/Run2018A-v1/RAW'
    config.Data.runRange = '316110'
    submit(config)

    config.General.requestName = 'hcaltuple_run316972'
    config.Data.outputDatasetTag = "hcaltuple_run316972"
    config.Data.inputDataset = '/ZeroBias/Run2018A-v1/RAW'
    config.Data.runRange = '316972'
    submit(config)

    config.General.requestName = 'hcaltuple_run317738'
    config.Data.outputDatasetTag = "hcaltuple_run317738"
    config.Data.inputDataset = '/ZeroBias/Run2018B-v1/RAW'
    config.Data.runRange = '317738'
    submit(config)

    config.General.requestName = 'hcaltuple_run318983'
    config.Data.outputDatasetTag = "hcaltuple_run318983"
    config.Data.inputDataset = '/ZeroBias/Run2018B-v1/RAW'
    config.Data.runRange = '318983'
    submit(config)

    config.General.requestName = 'hcaltuple_run319629'
    config.Data.outputDatasetTag = "hcaltuple_run319629"
    config.Data.inputDataset = '/ZeroBias/Run2018C-v1/RAW'
    config.Data.runRange = '319629'
    submit(config)

    config.General.requestName = 'hcaltuple_run320062'
    config.Data.outputDatasetTag = "hcaltuple_run320062"
    config.Data.inputDataset = '/ZeroBias/Run2018C-v1/RAW'
    config.Data.runRange = '320062'
    submit(config)
