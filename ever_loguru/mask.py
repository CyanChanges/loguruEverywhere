import logging


class FakeLogger:
    def __instancecheck__(self, instance):
        if instance == logging.Logger:
            return True
        else:
            return False
