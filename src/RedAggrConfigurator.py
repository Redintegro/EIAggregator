import json
import logging
import logging.config
from collections import namedtuple

logging.config.fileConfig(fname='conf/files.conf',disable_existing_loggers=False)

logger = logging.getLogger(__name__)


class configuration:

    def kpiconfigurations(mself,id,dimensions,measures):
       mself.id = id
       mself.dimensions = dimensions
       mself.measures = measures


    def __init__(self,inputtypeid,inputfiledescription,inputfilepath,filenamepattern,datastructure,delimiter,header,kpis):
       self.inputtypeid = inputtypeid
       self.inputfiledescription = inputfiledescription
       self.inputfilepath = inputfilepath
       self.filenamepattern = filenamepattern
       self.datastructure = []
       for column in datastructure:
           ncolumn = json.loads(json.dumps(column),object_hook=lambda d:namedtuple("X",d.keys())(*d.values()))
           self.datastructure.append(ncolumn)
       self.delimiter = delimiter
       self.header = header
       self.kpis = []
       nkppi = '{ "id":"K01","dimensions":{"kys":"1,2","seperator":","},"measures":[{"column":3,"function":"sum"},{"column":4,"function":"sum"}]}'
       for kpi in kpis:
           logger.debug("Type kpi   :")
           logger.debug('nkppi      :%s',nkppi)
           logger.debug('kpi        :%s',kpi)
           nkpi = json.loads(json.dumps(kpi),object_hook=lambda d: namedtuple("X",d.keys())(*d.values()))
           self.kpis.append(nkpi)
           

with open('myconfig.json') as jconfig:
  j = json.load(jconfig)
  logger.debug(j)

  pythonobj = configuration(**j)

  logger.debug("Input Type ID          :%s",pythonobj.inputtypeid)
  logger.debug("Input File Description :%s",pythonobj.inputfiledescription)
  logger.debug("Data Structure         :%s",pythonobj.datastructure)
  logger.debug("Kpis                   :%s",pythonobj.kpis)

  for kpi in pythonobj.kpis:
      logger.debug("Id of KPI  :%s",kpi.id)
      logger.debug("Dimensions :%s",kpi.dimensions)
      for dimension in kpi.dimensions:
          logger.debug("kpi.dimensions[X].column      :%s",dimension.column)
          logger.debug("kpi.dimensions[X].transformation  :%d",dimension.transformation)
          if dimension.transformation:
             logger.debug("kpi.dimensions[X].function     :%s",dimension.function)
      logger.debug("Measures   :%s",kpi.measures)
      for measure in kpi.measures:
          logger.debug("measure.column   :%s",measure.column)
          logger.debug("measure.function :%s",measure.function)
  for column in pythonobj.datastructure:
      logger.debug("column.pos         :%s",column.pos)
      logger.debug("column.columnname  :%s",column.columnname)
      logger.debug("column.columndesc  :%s",column.columndesc)
      logger.debug("column.datatype    :%s",column.datatype)
      logger.debug("column.size        :%s",column.size)

