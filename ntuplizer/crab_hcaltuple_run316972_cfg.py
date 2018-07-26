from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'hcaltuple_run316972'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pfg_new2_Global_RAW_cfg.py'
config.JobType.pyCfgParams = ['outputFile=hcalTupleTree.root']

config.Data.inputDataset = '/ZeroBias/Run2018A-v1/RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.lumiMask = ''
config.Data.runRange = '316972'
config.Data.outLFNDirBase = '/store/user/%s/cms_area/hcal/task9/run316972/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = "hcaltuple_run316972"

config.Site.storageSite = "T3_US_Rutgers"
