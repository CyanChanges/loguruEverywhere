import logging

import ever_loguru

# ever_loguru.install()  # Replace logging logger default Handler
ever_loguru.install_force()  # will overwrite manager.getLogger, manager.loggerClass
ever_loguru.update_exist()

logger = logging.getLogger("test")  # call Overwritten manager.getLogger
logger.info("test")
