from abc import abstractmethod


class Log:
    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def warn(self):
        pass

    @abstractmethod
    def error(self):
        pass

    @abstractmethod
    def crit(self):
        pass

class ConsoleLog(Log):
    def debug(self):
        print("\033[37m{}" .format("Debug"))

    def info(self):
        print("\033[4m\033[32m{}\033[0m".format("Info"))

    def warn(self):
        print("\033[34m{}".format("Warn"))

    def error(self):
        print("\033[31m\033[1m{}".format("Error"))

    def crit(self):
        print("\033[33m\033[4m{}".format("Crit"))


run = ConsoleLog()
run.debug()
run.info()
run.warn()
run.error()
run.crit()