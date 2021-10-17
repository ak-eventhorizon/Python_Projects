class User:
    """
    Docstring for a User class
    """

    def __init__(self, rank=-8):
        self.rank = rank
        self.progress = 0

    def inc_progress(self, task_rank):
        # выбрасывание ошибки при получении не валидного ранга задачи
        if task_rank < -8 or task_rank > 8 or task_rank == 0:
            raise ValueError("task_rank should be -8 <= rank <= 8 except 0")

        # если ранг уже максимальный - расчетов не проводить
        if self.rank == 8:
            return

        # если текущий ранг пользователя отрицательный, а ранг решенной задачи положительный - учесть отсутствие нуля
        if task_rank > 0 > self.rank:
            rank_delta = task_rank - self.rank - 1
        # если текущий ранг пользователя положительный, а ранг решенной задачи отрицательный - учесть отсутствие нуля
        elif task_rank < 0 < self.rank:
            rank_delta = task_rank - self.rank + 1
        else:
            rank_delta = task_rank - self.rank

        earned_progress = 0

        if rank_delta > 0:
            earned_progress = 10 * rank_delta * rank_delta
        elif rank_delta == 0:
            earned_progress = 3
        elif rank_delta == -1:
            earned_progress = 1
        elif rank_delta < -1:
            pass

        self.progress += earned_progress

        if self.progress >= 100:
            # распределение полученного прогресса в новые ранги, если ранг не максимальный
            while self.progress >= 100:
                self.set_next_rank()
                if self.rank == 8:
                    self.progress = 0
                else:
                    self.progress -= 100

    def set_next_rank(self):
        next_rank_for = {-8: -7,
                         -7: -6,
                         -6: -5,
                         -5: -4,
                         -4: -3,
                         -3: -2,
                         -2: -1,
                         -1: 1,
                         1: 2,
                         2: 3,
                         3: 4,
                         4: 5,
                         5: 6,
                         6: 7,
                         7: 8,
                         8: 8,
                         }
        self.rank = next_rank_for[self.rank]


if __name__ == '__main__':
    user = User()

    print(user.rank)  # => -8
    print(user.progress)  # => 0
    user.inc_progress(-7)
    print(user.progress)  # => 10
    user.inc_progress(-5)  # will add 90 progress
    print(user.progress)  # => 0 # progress is now zero
    print(user.rank)  # => -7 # rank was upgraded to -7
