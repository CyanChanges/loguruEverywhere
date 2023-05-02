import logging


class FakeLogger:
    def __instancecheck__(self, instance):
        if instance == logging.Logger:
            return True
        else:
            return issubclass(self.__class__, FakeLogger)
