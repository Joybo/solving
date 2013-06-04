# http://projecteuler.net/problem=54
# Answer: 376
# Time: 0.0405051708221
# Python: sort, sort_key, sort_reverse, lambda

from common import cal_time

card_map_value = {
  '2' : 200,
  '3' : 300,
  '4' : 400,
  '5' : 500,
  '6' : 600,
  '7' : 700,
  '8' : 800,
  '9' : 900,
  'T' : 1000,
  'J' : 1100,
  'Q' : 1200,
  'K' : 1300,
  'A' : 1400,
}

color_map_value = {
  'C' : 1,
  'D' : 2,
  'H' : 3,
  'S' : 4,
}

get_card_value = lambda card : card_map_value[card[0]] + color_map_value[card[1]]

is_pair           = lambda u : len(u) == 4
is_two_pairs      = lambda c : [c.count(val) for val in c].count(2) == 4
is_three          = lambda c : 3 in [c.count(val) for val in c]
is_straight       = lambda c : ''.join(c) in ['23456789TJQKA'[i:i+5] for i in xrange(9)]
is_flush          = lambda uc : len(uc) == 1
is_full_house     = lambda c: is_three(c) and is_pair(c)
is_four           = lambda c : 4 in [c.count(val) for val in c]
is_straight_flush = lambda c, uc : is_straight(c) and is_flush(uc)
is_royal_flush    = lambda c, uc : ''.join(c)=='TJQKA' and is_flush(uc)

def get_poker_value(cards):
  card_value   = [card[0] for card in cards]
  card_color   = [card[1] for card in cards]
  unique_value = set(card_value)
  unique_color = set(card_color)

  if is_royal_flush(card_value, card_color):
    return (9, color_map_value[cards[4][1]])

  elif is_straight_flush(card_value, card_color):
    return (8, card_map_value[cards[4][0]] + color_map_value[cards[4][1]])

  elif is_four(card_value):
    for card in cards[::-1]:
      if card_value.count(card[0]) != 4: continue
      return (7, card[0])

  elif is_full_house(card_value):
    for card in cards[::-1]:
      if card_value.count(card[0]) != 3: continue
      return (6, card[0])

  elif is_flush(card_color):
    return (5, card_map_value[cards[4][0]] + color_map_value[cards[4][1]])

  elif is_straight(card_value):
    return (4, card_map_value[cards[4][0]] + color_map_value[cards[4][1]])

  elif is_three(card_value):
    for card in cards[::-1]:
      if card_value.count(card[0]) != 3: continue
      return (3, card[0])

  elif is_two_pairs(card_value):
    for card in cards[::-1]:
      if card_value.count(card[0]) != 2: continue
      return (2, card_map_value[card[0]] + color_map_value[card[1]])

  elif is_pair(unique_value):
    for card in cards[::-1]:
      if card_value.count(card[0]) != 2: continue
      return (1, card_map_value[card[0]] + color_map_value[card[1]])

  return (0, card_map_value[cards[4][0]] + color_map_value[cards[4][1]])

@cal_time
def get_ans():
  with open('54_poker.txt', 'rb') as fr:
    lines = fr.read().splitlines()

  p1_win = 0
  for line in lines:
    p1_cards = line.split()[:5]
    p2_cards = line.split()[5:]

    p1_cards.sort(key = get_card_value, reverse = False)
    p2_cards.sort(key = get_card_value, reverse = False)

    p1_score1, p1_score2 = get_poker_value(p1_cards)
    p2_score1, p2_score2 = get_poker_value(p2_cards)

    if p1_score1 < p2_score1:
      continue

    if p1_score1 > p2_score1 or p1_score2 > p2_score2:
      p1_win +=1

  return p1_win

get_ans()

