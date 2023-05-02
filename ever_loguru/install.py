import functools
import sys
from .handler import LoguruLoggingHandler
from .mask import FakeLogger
from .wrapper import AsyncLoggingLoguruWrapper, LoggingLoguruWrapper

callHandlers_func = sys.modules['logging'].Logger.callHandlers


def _callHandlers_wrapper(original, record):
    """

    :param original: self as logging.Logger
    :param record: record dict
    :return: None at all
    """
    if hasattr(original, "handlers"):
        if getattr(original, "handlers"):
            setattr(original, "handlers", [LoguruLoggingHandler()])

    if callable(callHandlers_func):
        callHandlers_func(original, record)


def update_exist():
    import logging
    for logger_name in logging.Logger.manager.loggerDict.keys():
        logging.Logger.manager.loggerDict.update(
            {logger_name: LoggingLoguruWrapper()}
        )


def update_exist_instancecheck():
    import logging
    for logger_name in logging.Logger.manager.loggerDict.keys():
        logging_logger = logging.Logger.manager.loggerDict[
            logger_name
        ]
        setattr(
            logging_logger,
            "__instancecheck__",
            functools.partial(FakeLogger.__instancecheck__, logging_logger)
        )

# noinspection PyPep8Naming
def install():
    sys.modules['logging'].Logger.callHandlers = _callHandlers_wrapper

# noinspection PyPep8Naming
def install_force(replace_exist: bool = False):
    """
    Install which replace Logger class that may often break something during instancecheck
    :param replace_exist: replace_exist
    :return:
    """
    _Logger = getattr(sys.modules['logging'], "Logger")
    setattr(sys.modules['logging'], "Logger", LoggingLoguruWrapper)
    setattr(sys.modules['logging'].Logger, "manager", _Logger.manager)
    setattr(sys.modules['logging'].Logger.manager, "loggerClass", LoggingLoguruWrapper)

    if replace_exist:
        update_exist()
    else:
        update_exist_instancecheck()

# noinspection PyPep8Naming
def install_class(replace_exist: bool = False):
    """
    Install for manager.getLogger, manager.loggerClass that may break some modules
    :param replace_exist: Replace exist logger
    :return:
    """
    install()
    sys.modules['logging'].Logger.manager.getLogger = LoggingLoguruWrapper
    sys.modules['logging'].Logger.manager.loggerClass = LoggingLoguruWrapper
    setattr(sys.modules['logging'].Logger.manager, "loggerClass", LoggingLoguruWrapper)

    if replace_exist:
        update_exist()
    else:
        update_exist_instancecheck()

# noinspection PyPep8Naming
def remove():
    sys.modules['logging'].Logger.callHandlers = callHandlers_func
