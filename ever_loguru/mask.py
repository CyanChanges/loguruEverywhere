import logging


class FakeLogger:
    def __instancecheck__(self, instance):
        if instance == getattr(logging.Logger.manager, "_loggerClass"):
            return True
        else:
            return issubclass(self.__class__, FakeLogger)
