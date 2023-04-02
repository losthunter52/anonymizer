class Log:
    def __init__(self):
        self.warnings = []
        self.keys = []

    def add_key(self, key):
        self.keys.append(key)

    def add_warning(self, warning):
        self.warnings.append(warning)

    def get_log(self):
        log = []
        if len(self.keys) > 0:
            log.append("Keys:")
            for key in self.keys:
                log.append(str(key))
        if len(self.warnings) > 0:
            log.append("Warnings:")
            for warning in self.warnings:
                log.append(str(warning))
        if len(log) > 0:
            return log
        else:
            return False
