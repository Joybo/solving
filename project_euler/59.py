# http://projecteuler.net/project/cipher1.txt
# Answer: 107359
# Time: 0.00413179397583
# Plain text:
# (The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father.

from common import cal_time, read_file

@cal_time
def get_ans():
  cont = read_file('59_cipher1.txt')
  secret = map(int, cont.split(','))

  space_ascii = ord(' ')
  space_xor_secret = secret[:]
  for i in xrange(len(space_xor_secret)):
    space_xor_secret[i] = secret[i] ^ space_ascii

  i = 0
  for ascii in set(sorted(space_xor_secret)):
    find_counts = space_xor_secret.count(ascii)
    if find_counts < 50: continue
    print ascii, find_counts
    # Ascii  Times
    # 100    77
    # 103    70
    # 111    86

  # key = [111, 111, 111] => prefix message: " Tcm ", so we can guess key[1] = 111
  # key = [103, 111, 103] => prefix message: "?Tke ", we found Tke, we can guess Tke is The. 
  #                                                   And e's position is 3, 3 % 3 = 0.
  #                                                   So, key[0] = 103 maybe right.
  # key = [103, 111, 100] => prefix message: "?The "
  key_map = [103, 111, 100]
  test = []
  for i in xrange(len(secret)):
    ascii = secret[i]
    ch = chr(ascii ^ key_map[i%3])
    #if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z') or (ch>='0' and ch<='9') or ch==' ' or ch=='.':
    #  test += [ch]
    #else:
    #  test += ['?']

    test += [ch]

  print ''.join(test)

  ascii_plain = []
  for ch in test:
    ascii_plain += [ord(ch)]

  return sum(ascii_plain)

get_ans()

