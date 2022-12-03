OUTCOME_VALUES = [3, 6, 0]
PLAY_VALUES = [1, 2, 3]
MY_OFFSET = ord('X')
ENEMY_OFFSET = ord('A')

class Strategy_1():


    def __init__(self, key):
        self.key = ord(key) - MY_OFFSET

    def compete_against(self, enemy_key):
        enemy_key = ord(enemy_key) - ENEMY_OFFSET
        diff = (self.key - enemy_key) % 3
        return OUTCOME_VALUES[diff] + PLAY_VALUES[self.key]

class Strategy_2():

    def __init__(self, key):
        self.key = ord(key) - MY_OFFSET - 1

    def compete_against(self, enemy_key):
        enemy_play = ord(enemy_key) - ENEMY_OFFSET
        my_play = ((enemy_play + (self.key))) % 3
        victory_value = OUTCOME_VALUES[self.key]
        play_value = PLAY_VALUES[my_play]
        return victory_value + play_value




if __name__ == "__main__":
    score_1 = 0
    score_2 = 0
    with open('input/day02_input.txt') as f:
        for line in f.readlines():
            parts = line.strip().split()
            me = parts[1]
            enemy = parts[0]
            score_1 = score_1 + Strategy_1(me).compete_against(enemy)
            score_2 = score_2 + Strategy_2(me).compete_against(enemy)
    print(score_1)
    print(score_2)

