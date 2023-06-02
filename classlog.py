from abc import abstractmethod


class Log:
    @abstractmethod
    def debug(self, text: str):
        print("crit" + text)

    @abstractmethod
    def info(self, text: str):
        print("crit" + text)

    @abstractmethod
    def warn(self, text: str):
        print("crit" + text)

    @abstractmethod
    def error(self, text: str):
        print("crit" + text)

    @abstractmethod
    def crit(self, text: str):
        print("crit" + text)
class ConsoleLog(Log):
    def debug(self, text: str):
        print("\033[37m{}" .format(text))

    def info(self, text: str):
        print("\033[4m\033[32m{}\033[0m".format(text))

    def warn(self, text: str):
        print("\033[34m{}".format(text))

    def error(self, text: str):
        print("\033[31m\033[1m{}".format(text))

    def crit(self, text: str):
        print("\033[33m\033[4m{}".format(text))


run = ConsoleLog()
run.debug("Дебаг")
run.info("Полезная информация")
run.warn("Предупреждение")
run.error("Ошибка!")
run.crit("Критическая ошибка!")