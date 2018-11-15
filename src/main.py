import logging
import AggrConfigurator

logging.config.fileConfig(fname='/data2/python/enhancesys/conf/files.conf',disable_existing_loggers=False)

logger = logging.getLogger(__name__)


configobj = RedAggrConfigurator.loadconfig("/data2/python/enhancesys/conf/inputstreams/Employeeconfig.json")

#RedAggrConfigurator.testoutput(configobj)


