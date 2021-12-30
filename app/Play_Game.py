import curses
import curses.textpad
import textwrap
from nltk.corpus import words, wordnet
import string
import random

menu = ["PLAY GAME",
        "INSTRUCTIONS", "LEADER-BOARD", "EXIT GAME"]
navigation = ["BACK", "NEXT"]
last_page = ["BACK", "MENU"]

  
def center_coordinate(string, h, w):
    x = w // 2 - len(string)//2
    y = h // 2
    return y, x


def print_menu(m_screen, selected_row_idx):

    m_screen.clear()
    h, w = m_screen.getmaxyx()

    screen_title = "Start Menu"
    game_title = "Scramble!"
    # author = "by Juju_Beans94"
    author = "by Jadesola Alade-Fa"

    gt_coord = center_coordinate(game_title, h, w)
    s_coord = center_coordinate(screen_title, h, w)
    a_coord = center_coordinate(author, h, w)

    m_screen.attron(curses.color_pair(2))
    m_screen.addstr(0, gt_coord[1], game_title)
    m_screen.attroff(curses.color_pair(2))
    m_screen.attron(curses.color_pair(3))
    m_screen.addstr(1, s_coord[1], screen_title)
    m_screen.attroff(curses.color_pair(3))
    m_screen.addstr(a_coord[0]*2 - 1, a_coord[1], author)

    for idx, row in enumerate(menu):  # row highlighting
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            m_screen.attron(curses.color_pair(1))
            m_screen.addstr(y, x, row)
            m_screen.attroff(curses.color_pair(1))
        else:
            m_screen.addstr(y, x, row)

    m_screen.refresh()


def print_instructions(m_screen, selected_row_idx, window_idx):

    m_screen.clear()
    curses.curs_set(0)
    m_screen.immedok(True)
    m_screen.border(0)

    h, w = m_screen.getmaxyx()

    box1 = curses.newwin(0, 0)
    box2 = box1.derwin(5, 2)

    box2.border(0)
    # box1.immedok(True)
    box2.immedok(True)

    screen_title = "Instructions"
    game_title = "Scramble!"
    text1 = "Welcome to Scramble!"
    text2 = "Your goal is to use random letters to spell out as many words as you can in 5 or 10 turns.@ During game-play a key will define how many points each letter is worth.@ You may use your enter and arrow keys to navigate the menus.@ Before you play the game you must choose your DIFFICULTY-LEVEL."
    text3 = "The more difficult the level, the more points each letter will be worth - but the less turns you will have.@ The NOVICE level limits you to 10 turns. The ADVANCED level limits you to 5 turns.@ Every entry you make takes a turn, so do your best :)@ During game play, you can buy vowels and discard letters."
    text4 = "To buy a vowel, first type it, then  enter the key-code '-b'.@ To discard a letter choose from YOUR LETTERS and use the '-d' key-code.@ Press ENTER to submit.@ The value of the bought vowel(s), or the discarded letter(s), is subtracted from your TOTAL POINTS.@ If you don't have enough points, you cannot buy a vowel - but you can discard as many letters as you wish.@ Thank you for reading!@ Enjoy the game!!!!"

    box1.box()
    curses.curs_set(0)

    gt_coord = center_coordinate(game_title, h, w)
    s_coord = center_coordinate(screen_title, h, w)

    b2h, b2w = box2.getmaxyx()
    y = b2h // 2
    x = b2w // 2
    box2.addstr(1, x - len(text1) // 2, textwrap.fill(text1, 38))
    box2.addstr(3, 0, textwrap.fill("\n", 38))

    page1 = text2
    page2 = text3
    page3 = text4

    page_coord = center_coordinate(page1, h, w)

    page_num = [page1, page1, page2, page2, page3, page3]

    m_screen.attron(curses.color_pair(2))
    m_screen.addstr(0, gt_coord[1], game_title)
    m_screen.attroff(curses.color_pair(2))
    m_screen.attron(curses.color_pair(3))
    m_screen.addstr(1, s_coord[1], screen_title)
    m_screen.attroff(curses.color_pair(3))
    m_screen.addstr(2, s_coord[1], "")

    if selected_row_idx in [0, 1]:
        sentences = text2.split("@")
        for index, sentence in enumerate(sentences):
            sentence_w = textwrap.wrap(
                sentence, x*2 - 4, break_long_words=False)
            for wrapped_sentence in sentence_w:
                sentence_c = wrapped_sentence.center(x*2 - 4)
                box2.addstr(4+index*2, 1, sentence_c)
                box2.addstr(19, x, "Page 1")
    elif selected_row_idx in [2, 3]:
        sentences = text3.split("@")
        for index, sentence in enumerate(sentences):
            sentence_w = textwrap.wrap(
                sentence, x*2 - 4, break_long_words=False)
            for wrapped_sentence in sentence_w:
                sentence_c = wrapped_sentence.center(x*2 - 4)
                box2.addstr(4+index*2, 1, sentence_c)
                box2.addstr(19, x, "Page 2")
                break
    elif selected_row_idx in [4, 5]:
        sentences = text4.split("@")
        for index, sentence in enumerate(sentences):
            sentence_w = textwrap.wrap(
                sentence, x*2 - 4, break_long_words=False)
            for wrapped_sentence in sentence_w:
                sentence_c = wrapped_sentence.center(x*2 - 4)
                box2.addstr(4+index*2, 1, sentence_c)
                box2.addstr(20, x-2, "Page 3")
                break
    m_screen.refresh()
    curses.curs_set(0)


def random_letter_picker(the_word_list, alphabet, num_of_letters):
    joined_words = "".join(the_word_list)
    list_of_letters = list(joined_words)
    length_of_letter_list = len(list_of_letters)
    # define frequency of each letter in alphabetical order
    probs = []
    for letter in alphabet:
        x = list_of_letters.count(letter)
        y = x / length_of_letter_list
        probs.append(y)
    # rename probs to  variable for readability; w for weight; note type: list
    w = probs

    # change vowels frequencies so all vowels have equal frequency
    # 1) find index of all the vowels/find positions of vowels in the alphabet
    the_vowels_comp = [index for index, freq in enumerate(w)
                       if alphabet[index] in ["a", "e", "i", "o", "u"]]

    # 2) find average of all frequences the reasign new value for each vowel into original
    # list of letter frequencies (w)
    vowel_sum = 0
    for index in the_vowels_comp:
        vowel_sum += w[index]
        vowel_freq = vowel_sum / 5
        if alphabet[index] in ["a", "e", "i", "o", "u"]:
            w[index] = vowel_freq

    # apply weighted random sampling methond from random module
    while 1:
        set_of_letters = random.choices(alphabet, weights=w, k=num_of_letters)
        vowel_count = 0
        for vowel in ["a", "e", "i", "o", "u"]:
            if vowel in set_of_letters:
                vowel_count += 1
        if vowel_count < 2:
            continue
        elif vowel_count == 2:
            return set_of_letters


def process_word(spelled_word, current_hand, current_score, the_word_list, alphabet_dict, alphabet, diff_level):
    rmletts = []
    discletts = []
    current_hand_str = ""
    passed_letters_spelt = ""
    cleaned_text = "".join(spelled_word[:-1].split()).strip()

    for x in current_hand:
        current_hand_str += x

    if "-b" in cleaned_text and len(cleaned_text) > 0:
        cleaned_text[:-2]
        for vowel in cleaned_text:
            if vowel in alphabet_dict and vowel in ["a", "e", "i", "o", "u"]:
                current_score -= alphabet_dict[vowel]*diff_level
                current_hand.append(vowel)

    elif "-d" in cleaned_text and len(cleaned_text) > 0:
        cleaned_text[:-2]
        for discarded_letter in cleaned_text:
            if discarded_letter in current_hand_str:
                # dlindex = current_hand.index(discarded_letter)
                # removed_letter = current_hand[dlindex]
                # discletts.append(removed_letter)
                discletts.append(discarded_letter)
        for dl in discletts:
            if dl in alphabet_dict:
                current_score -= alphabet_dict[dl]*diff_level
                # dlist_index = current_hand.index(dl)
                # current_hand.remove(dlist_index)
                current_hand.remove(dl)
    else:
        for spelled_letter in cleaned_text:
            if spelled_letter in current_hand_str:
                passed_letters_spelt += spelled_letter
            else:
                passed_letters_spelt = ""
                break  # lose a turn because submitted letter not in hand

        if len(passed_letters_spelt) > 1 and passed_letters_spelt in the_word_list:
            for spelt_letter in passed_letters_spelt:
                # rmlindex = current_hand.index(spelt_letter)
                # removed_letter = current_hand[rmlindex]
                # rmletts.append(removed_letter)
                rmletts.append(spelt_letter)

            for rml in rmletts:
                if rml in alphabet_dict and passed_letters_spelt in the_word_list:
                    current_score += alphabet_dict[rml]*diff_level
                    # list_index = current_hand.index(rml)
                    # current_hand.remove(list_index)
                    current_hand.remove(rml)
                else:
                    break  # lose a turn becuase submitted a one letter word and/or word not in word_list  or skipped

    if len(current_hand) <= 3:
        auto_hand = random_letter_picker(
            the_word_list, alphabet, 8 - len(current_hand))
        current_hand += auto_hand

    return current_score, current_hand

    """test to see ouput of function"""
    # if spelled_word and current_hand:
    #     score = 0
    #     print("input from process_word function:")
    #     print(spelled_word)  # in terminal
    #     print(len(spelled_word))  # in terminal
    #     return spelled_word, score


def update_game_screen(game_window, set_of_letters, current_score=0, turns_left=5, diff_level=1):

    curses.curs_set(0)
    game_window.border()
    h, w = game_window.getmaxyx()

    game_window.addstr(7, w // 2 - (len(set_of_letters)*5) //
                       2, f"{set_of_letters}")

    screen_title = "Game Screen"
    game_title = "Scramble!"

    gt_coord = center_coordinate(game_title, h, w)
    s_coord = center_coordinate(screen_title, h, w)

    game_window.attron(curses.color_pair(2))
    game_window.addstr(0, gt_coord[1], game_title)
    game_window.attroff(curses.color_pair(2))
    game_window.attron(curses.color_pair(3))
    game_window.addstr(1, s_coord[1], screen_title)
    game_window.attroff(curses.color_pair(3))
    game_window.addstr(2, s_coord[1], "")

    hand_prompt = "Your Letters:"
    game_window.addstr(6, w//2 - len(hand_prompt) // 2 - 1, hand_prompt)

    input_prompt = "Spell Your Word:"
    game_window.addstr(9, w // 2 - len(input_prompt)//2, input_prompt)

    score_prompt = f"Total Score: {current_score}"
    game_window.addstr(13, w // 2 - len(score_prompt)//2, score_prompt)
    turns_prompt = f"Turns Left: {turns_left}"
    game_window.addstr(15, w // 2 - len(turns_prompt)//2, f"{turns_prompt}")
    point_legend1 = "5: Vowels || 4: v-z || 3: q-t || 2: k-p || 1: b-j"
    point_legend2 = "7.5: Vowels || 6: v-z || 4.5: q-t || 3: k-p || 1.5: b-j"

    if diff_level == 1:
        game_window.addstr(17, w // 2 - len(point_legend1)//2, point_legend1)
    elif diff_level == 1.5:
        game_window.addstr(17, w // 2 - len(point_legend2)//2, point_legend2)

    game_window.addstr(19, w // 2 - 3, "POINTS")

    sub = game_window.subwin(3, 41, 10, w // 2 - 20)
    sub.border()
    sub2 = sub.subwin(1, 39, 11, w // 2 - 20 + 1)
    tb = curses.textpad.Textbox(sub2)
    turns_left -= 1
    game_window.noutrefresh()
    curses.doupdate()
    return turns_left


def enter_is_terminate(x):
    if x == 13:
        x = 7
    return x


def highlight_nav(m_screen, selected_row_idx, sub_menu_list, sub_menu_list2, window_idx):

    m_screen.clear()
    h, w = m_screen.getmaxyx()

    print_instructions(m_screen, selected_row_idx, window_idx)

    for row in sub_menu_list:  # row/option highlighting
        x1 = w // 2 - len(row) // 2 - 10
        x2 = w // 2 + len(row) // 2 + 10
        y = h - 1
        if selected_row_idx % 2 == 0:
            print_instructions(m_screen, selected_row_idx,
                               window_idx)
            m_screen.attron(curses.color_pair(1))
            m_screen.addstr(y, x1, sub_menu_list[0])
            m_screen.attroff(curses.color_pair(1))
            m_screen.addstr(y, x2, sub_menu_list[1])

        elif selected_row_idx % 2 == 1 and selected_row_idx != 5:
            print_instructions(m_screen, selected_row_idx,
                               window_idx)
            m_screen.attron(curses.color_pair(1))
            m_screen.addstr(y, x2, sub_menu_list[1])
            m_screen.attroff(curses.color_pair(1))
            m_screen.addstr(y, x1, sub_menu_list[0])
        elif selected_row_idx % 2 == 1 and selected_row_idx == 5:
            sub_menu_list = sub_menu_list2
            m_screen.attron(curses.color_pair(1))
            m_screen.addstr(y, x2, sub_menu_list[1])
            m_screen.attroff(curses.color_pair(1))
            m_screen.addstr(y, x1, sub_menu_list[0])
    m_screen.refresh()


def difficulty_selection(level_window, option_list, option_index, window_index):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    level_window.clear()
    level_box = level_window.derwin(
        20, 60, curses.LINES//2 - 10, curses.COLS//2 - 30)
    lev_h, lev_w = level_box.getmaxyx()
    level_box.border()
    curses.curs_set(0)
    # level_box.addstr()
    level_box.noutrefresh()
    curses.doupdate()

    screen_title = "Level Select"
    game_title = "Scramble!"
    selection_prompt = "~ Choose Your Level ~"

    gt_coord = center_coordinate(game_title, lev_h, lev_w)
    s_coord = center_coordinate(screen_title, lev_h, lev_w)
    sp_coord = center_coordinate(selection_prompt, lev_h, lev_w)

    level_box.attron(curses.color_pair(2))
    level_box.addstr(0, gt_coord[1], game_title)
    level_box.attroff(curses.color_pair(2))
    level_box.attron(curses.color_pair(3))
    level_box.addstr(1, s_coord[1], screen_title)
    level_box.attroff(curses.color_pair(3))
    level_box.addstr(2, s_coord[1], "")
    level_box.addstr(5, sp_coord[1], selection_prompt)
    level_box.noutrefresh()
    curses.doupdate()

    for _ in option_list:
        x1 = lev_w // 2 - 15
        x2 = lev_w // 2 + 8
        y = lev_h - 10
        if option_index % 2 == 0 and window_index == 0:
            level_box.attron(curses.color_pair(2))
            level_box.addstr(y, x1, option_list[0])
            level_box.attroff(curses.color_pair(2))
            level_box.addstr(y, x2, option_list[1])
        elif option_index % 2 == 1 and window_index == 1:
            level_box.attron(curses.color_pair(3))
            level_box.addstr(y, x2, option_list[1])
            level_box.attroff(curses.color_pair(3))
            level_box.addstr(y, x1, option_list[0])
    level_box.noutrefresh()
    curses.doupdate()


def main(m_screen):

    # set colors
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # set variables
    h, w = m_screen.getmaxyx()  # init height and width
    current_row_idx = 0  # initialize cursor to first row

    # assemble wordlist from nltk imports wornet and words
    wordnet_list = list(wordnet.words())
    wordnet_list2 = []
    for wrd in wordnet_list:
        x = wrd.replace("_", "")
        wordnet_list2.append(x)
    word_list = words.words() + wordnet_list2

    # remove words less than two letters in length
    for x in word_list:
        if len(x) < 2:
            word_list.remove(x)
    # create an alphabet list using ascii encoding
    alphabet_list = list(string.ascii_lowercase)
    alphabet_points = {"a": 5,
                       "b": 1,
                       "c": 1,
                       "d": 1,
                       "e": 5,
                       "f": 1,
                       "g": 1,
                       "h": 1,
                       "i": 5,
                       "j": 1,
                       "k": 2,
                       "l": 2,
                       "m": 2,
                       "n": 2,
                       "o": 5,
                       "p": 2,
                       "q": 3,
                       "r": 3,
                       "s": 3,
                       "t": 3,
                       "u": 5,
                       "v": 4,
                       "w": 3,
                       "x": 4,
                       "y": 4,
                       "z": 4}
    screen_score = 0
    hand = random_letter_picker(word_list, alphabet_list, 8)
    turns = 5

    # format menu options
    print_menu(m_screen, current_row_idx)
    options = ["NOVICE", "ADVANCED"]

    # define main screen behavior
    while 1:
        key = m_screen.getch()  # ask usser input key/character

        m_screen.clear()  # clear window before loop

        if key == curses.KEY_A2 and current_row_idx > 0:  # navigating menue
            current_row_idx -= 1
            m_screen.refresh()
        if key == curses.KEY_C2 and current_row_idx < len(menu)-1:
            current_row_idx += 1
            m_screen.refresh()

        if key == curses.KEY_ENTER or key in [10, 13]:  # presing enter

            # define menu selection acctions
            if current_row_idx == menu.index(menu[0]):
                # empty screen
                m_screen.clear()

                # set variables
                the_current_row_idx = 0
                a_press = 0
                the_screen_row_index = a_press % 2

                # setup window format
                difficulty_selection(
                    m_screen, options, the_current_row_idx, the_screen_row_index)
                m_screen.noutrefresh()
                curses.doupdate()

                while True:
                    a_key_press = m_screen.getch()   # ask usser input key/character

                    if a_key_press == curses.KEY_B1 and the_current_row_idx % 2 == 0:
                        m_screen.clear()
                        print_menu(m_screen, the_current_row_idx)
                        m_screen.noutrefresh()
                        curses.doupdate()
                        break

                    elif a_key_press == curses.KEY_B3 and the_current_row_idx % 2 == 0:
                        a_press += 1
                        the_screen_row_index = a_press % 2
                        the_current_row_idx += 1
                        difficulty_selection(
                            m_screen, options, the_current_row_idx, the_screen_row_index)
                        m_screen.noutrefresh()
                        curses.doupdate()

                    elif a_key_press == curses.KEY_B1 and the_current_row_idx % 2 == 1:
                        the_current_row_idx -= 1
                        a_press -= 1
                        the_screen_row_index = a_press % 2
                        difficulty_selection(
                            m_screen, options, the_current_row_idx, the_screen_row_index)
                        m_screen.noutrefresh()
                        curses.doupdate()

                    elif a_key_press in [10, 13] and the_screen_row_index == 0:
                        turns = 10
                        multi = 1
                        m_screen.clear()
                        m_screen.noutrefresh()
                        curses.doupdate()
                        break
                    elif a_key_press in [10, 13] and the_screen_row_index == 1:
                        turns = 5
                        multi = 1.5
                        m_screen.clear()
                        m_screen.noutrefresh()
                        curses.doupdate()
                        break
                while turns:
                    turns_left = update_game_screen(
                        m_screen, hand, screen_score, turns, multi)
                    turns = turns_left
                    sub = m_screen.subwin(
                        3, 41, 10, w // 2 - 20)
                    sub.border()
                    sub2 = sub.subwin(1, 39, 11, w // 2 - 20 + 1)
                    tb = curses.textpad.Textbox(sub2)
                    m_screen.noutrefresh()  # show that a new textbox was created
                    curses.doupdate()
                    tb.edit(enter_is_terminate)
                    text = tb.gather()
                    sub2.clear()
                    if len(text) != 0:
                        new_score, new_hand = process_word(
                            text, hand, screen_score, word_list, alphabet_points, alphabet_list, multi)
                        screen_score = new_score
                        m_screen.clear()
                    else:
                        continue
                    update_game_screen(m_screen, new_hand,
                                       screen_score, turns, multi)
                    m_screen.noutrefresh()  # show that a new textbox was created
                    curses.doupdate()
                if turns_left == 0:
                    m_screen.clear()
                    end_game_message = 'Game Over! Good Job!'
                    m_screen.addstr(curses.LINES//2, (curses.COLS -
                                    len(end_game_message))//2, end_game_message)
                    # screen score variable holds value to be added to database
                    final_score_text = f"Your Score is: {screen_score}"
                    m_screen.addstr(curses.LINES//2 + 2, (curses.COLS -
                                    len(final_score_text))//2, final_score_text)
                    m_screen.noutrefresh()
                    curses.doupdate()
                    m_screen.getch()
                    m_screen.erase()
                    current_row_idx = 0
                    screen_score = 0
                    hand = random_letter_picker(word_list, alphabet_list, 8)
                    print_menu(m_screen, the_current_row_idx)
                    m_screen.refresh()

            if current_row_idx == menu.index(menu[1]):
                # m_screen.clear()  # empty screen
                # text = "This is how you play the game"
                # c_coord = center_coordinate(text, h, w)
                # m_screen.addstr(c_coord[0], c_coord[1], text)
                # m_screen.refresh()

                current_row_idx = 0
                press = 0
                screen_row_index = press % 2

                highlight_nav(m_screen, current_row_idx,
                              navigation, last_page, screen_row_index)
                m_screen.refresh()

                while True:
                    key_press = m_screen.getch()   # ask usser input key/character

                    if key_press in [10, 13, curses.KEY_B1] and screen_row_index == 0 and current_row_idx == 0:
                        print_menu(m_screen, current_row_idx)
                        m_screen.refresh()
                        break

                    elif key_press == curses.KEY_B3 and current_row_idx != 5:
                        press += 1
                        screen_row_index = press % 2
                        current_row_idx += 1
                        highlight_nav(m_screen, current_row_idx,
                                      navigation, last_page, screen_row_index)
                        m_screen.refresh()

                    elif key_press == curses.KEY_B1:
                        if current_row_idx % 2 == 0:
                            current_row_idx -= 2
                            highlight_nav(
                                m_screen, current_row_idx, navigation, last_page, screen_row_index)
                            m_screen.refresh()
                        elif current_row_idx % 2 == 1:
                            current_row_idx -= 1
                            press -= 1
                            screen_row_index = press % 2
                            highlight_nav(
                                m_screen, current_row_idx, navigation, last_page, screen_row_index)
                            m_screen.refresh()

                    elif key_press in [10, 13] and current_row_idx not in [0, 5]:
                        if screen_row_index == 0:
                            current_row_idx -= 2
                            highlight_nav(
                                m_screen, current_row_idx, navigation, last_page, screen_row_index)
                            m_screen.refresh()
                        elif screen_row_index == 1:
                            press += 1
                            screen_row_index = press % 2
                            current_row_idx += 1
                            highlight_nav(m_screen, current_row_idx,
                                          navigation, last_page, screen_row_index)
                            m_screen.refresh()

                    elif key_press in [10, 13, curses.KEY_B3] and screen_row_index == 1 and current_row_idx == 5:
                        current_row_idx = 0
                        print_menu(m_screen, current_row_idx)
                        m_screen.refresh()
                        break

            if current_row_idx == menu.index(menu[2]):
                m_screen.clear()  # empty screen
                text = "Check the Stats! Later.... Coming to you soon!"
                c_coord = center_coordinate(text, h, w)
                m_screen.addstr(c_coord[0], c_coord[1], text)
                m_screen.refresh()
                m_screen.getch()

            if current_row_idx == len(menu)-1:
                m_screen.clear()  # empty screen
                text = "Thank you for playing!"
                c_coord = center_coordinate(text, h, w)
                m_screen.addstr(c_coord[0], c_coord[1], text)
                m_screen.refresh()
                m_screen.getch()
                break

        print_menu(m_screen, current_row_idx)
        m_screen.refresh()


curses.wrapper(main)
