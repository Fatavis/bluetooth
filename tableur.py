import csv

class ReadSpreadsheet:
    """
    Class which allows to read the content of the spreadsheet but also to write in it.
    """
    def __init__(self, name):
        """The variable rows contains all of row in the spreadsheet
        The variable name_file contains the name of the file """
        self.rows = []
        #List with the name of th column of the spreadsheet
        self._student = []
        self._good_name = []
        self._index_good_name = []
        self._bad_name1 = []
        self._bad_name2 = []
        self._good_syllable = []
        self._index_good_syllable = []
        self._result_word = []
        self._syllable = []
        self._result_syllable = []
        self.column = {}
        self.name_file = str(name)
        self.open_file()

    def open_file(self):
        """
        Add the row of the spreadsheet in the variable rows.
        :return:
        """
        with open(self.name_file, newline='') as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                print(row)
                self._student.append(row[0])
                self._good_name.append(row[1])
                self._index_good_name.append(row[2])
                self._bad_name1.append(row[3])
                self._bad_name2.append(row[4])
                self._good_syllable.append(row[5])
                self._index_good_syllable.append(row[6])
                self._result_word.append(row[7])
                self._syllable.append(row[8])
                self._result_syllable.append(row[9])
                i += 1

            self._student.pop(0)
            self._good_name.pop(0)
            self._index_good_name.pop(0)
            self._bad_name1.pop(0)
            self._bad_name2.pop(0)
            self._good_syllable.pop(0)
            self._index_good_syllable.pop(0)
            self._result_word.pop(0)
            self._syllable.pop(0)
            self._result_syllable.pop(0)


    @property
    def student(self):
        """Return the number associated with the column student of the spreadsheet"""
        return self._student

    @property
    def good_name(self):
        """Return the number associated with the column good name of the speadsheet"""
        return self._good_name

    @property
    def index_good_name(self):
        """Return the number associated with the column index_good_name of the spreadsheet"""
        return self._index_good_name

    @property
    def bad_name1(self):
        """Return the number associated with the column bad_name1 of the spreadsheet"""
        return self._bad_name1

    @property
    def bad_name2(self):
        """Return the number associated with the column bad_name2 of the spreadsheet"""
        return self._bad_name2

    @property
    def good_syllable(self):
        """Return the number associated with the column good_syllable of the spreadsheet"""
        return self._good_syllable

    @property
    def index_good_syllable(self):
        """Return the number associated with the column index_good_syllable of the spreadsheet"""
        return self._index_good_syllable

    @property
    def result_word(self):
        """Return the number associated with the column result_word of the spreadsheet"""
        return self._result_word

    @property
    def syllable(self):
        """Return the number associated with the column syllable"""
        return self._syllable

    @property
    def result_syllable(self):
        """Return the number associated with the column result_syllable"""
        return self._result_syllable

    @result_syllable.setter
    def result_syllable(self, results):
        """Set the results of syllable"""
        self._result_syllable = results

    @result_word.setter
    def result_word(self, results):
        """Set the results of word"""
        self._result_word = results