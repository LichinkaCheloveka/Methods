class InitReport:
    def __init__(self, filename):
        self.filename = filename
        self.handle = open(filename, "w")

    def write_title_for_method(self):
        self.handle.write("\t{}\t{}\t""{}\t{}\t""{}\t{}\t""{}\t{}\n".format
                          ("X1", "X2", "F1", "F2", "Current A", "Current B", "Current lenght",
                           "Previous lenght  / (Current lenght"))

    def write_title_for_search(self):
        self.handle.write("\t{}\t{}\n".format("X", "F"))

    def get_handle(self):
        return self.handle

    def close_handle(self):
        self.handle.close()
