
class ScoreRecord(object):

    def __init__(self):
        self._scores = []
        # self._data_sheet_view = None
        self._min_max_view = None

    # @property
    # def data_sheet_view(self):
    #     return self._data_sheet_view
    #
    # @data_sheet_view.setter
    # def data_sheet_view(self, data_sheet_view):
    #     self._data_sheet_view = data_sheet_view

    @property
    def min_max_view(self):
        return self._min_max_view

    @min_max_view.setter
    def min_max_view(self, min_max_view):
        self._min_max_view = min_max_view

    @property
    def scores(self):
        return self._scores

    def add_score(self, score):
        self._scores.append(score)
        # self._data_sheet_view.update()
        self._min_max_view.update()

class DataSheetView(object):

    def __init__(self, score_record, view_count):
        self._score_record = score_record
        self._view_count = view_count

    def update(self):
        record = self._score_record.scores
        self.display_scores(record, self._view_count)


    def display_scores(self, record, view_count):
        print("List of {} entries".format(view_count))
        for i in range(min(len(record), view_count)):
            print(record[i], end=" ", flush=True)
        print("")

class MinMaxView(object):

    def __init__(self, score_record):
        self._score_record = score_record

    def update(self):
        record = self._score_record.scores
        self.display_min_max(record)


    def display_min_max(self, record):
        minimum = min(record)
        maximum = max(record)

        print("Min : {}, Max : {}".format(minimum, maximum))

if __name__ == "__main__":
    score_record = ScoreRecord()
    # data_sheet_view = DataSheetView(score_record, 3)
    # score_record.data_sheet_view = data_sheet_view

    min_max_view = MinMaxView(score_record)

    score_record.min_max_view = min_max_view

    for n in range(1, 6):
        print("Adding score : ", n * 10)
        score_record.add_score(n * 10)