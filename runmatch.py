#!/usr/bin/python3

from __future__ import print_function
import os
from os import path
import sys

def application(environ, start_response):
    # Retrieve POST data from the environment
    post_data = environ.get('QUERY_STRING', '')

# Parse the POST data (assuming it is in the format wrestler1=value1&wrestler2=value2&...)
    post_values = dict(kv.split('=') for kv in post_data.split('&'))

    # Access the wrestler variables
    wrestler1 = post_values.get('wrestler1', '')
    wrestler2 = post_values.get('wrestler2', '')
    wrestler3 = post_values.get('wrestler3', '')
    wrestler4 = post_values.get('wrestler4', '')

    print(f'Wrestler 1: {wrestler1}')
    print(f'Wrestler 2: {wrestler2}')
    print(f'Wrestler 3: {wrestler3}')
    print(f'Wrestler 4: {wrestler4}')

    execfile("wrestlers/" + wrestler1file_)
    wrestler1_ = Array({"name": stats_["name"], "hitpoints": stats_["hitpoints"], "offense": stats_["offense"], "defense": stats_["defense"], "pin_range": stats_["pin_range"], "dq_range": stats_["dq_range"], "finisher1": stats_["finisher1"], "finisher2": stats_["finisher2"], "finisher3": stats_["finisher3"]})
    execfile("wrestlers/" + wrestler2file_)
    wrestler2_ = Array({"name": stats_["name"], "hitpoints": stats_["hitpoints"], "offense": stats_["offense"], "defense": stats_["defense"], "pin_range": stats_["pin_range"], "dq_range": stats_["dq_range"], "finisher1": stats_["finisher1"], "finisher2": stats_["finisher2"], "finisher3": stats_["finisher3"]})
    howmany_ = 2
    if wrestler3file_ != "none":
        execfile("wrestlers/" + wrestler3file_)
        wrestler3_ = Array({"name": stats_["name"], "hitpoints": stats_["hitpoints"], "offense": stats_["offense"], "defense": stats_["defense"], "pin_range": stats_["pin_range"], "dq_range": stats_["dq_range"], "finisher1": stats_["finisher1"], "finisher2": stats_["finisher2"], "finisher3": stats_["finisher3"]})
        howmany_ = 3
    else:
        wrestler3_ = ""
    # end if
    if wrestler3file_ != "none" and wrestler4file_ != "none":
        execfile("wrestlers/" + wrestler4file_)
        wrestler4_ = Array({"name": stats_["name"], "hitpoints": stats_["hitpoints"], "offense": stats_["offense"], "defense": stats_["defense"], "pin_range": stats_["pin_range"], "dq_range": stats_["dq_range"], "finisher1": stats_["finisher1"], "finisher2": stats_["finisher2"], "finisher3": stats_["finisher3"]})
        howmany_ = 4
    else:
        wrestler4_ = ""
    # end if
# end if
#// Other initializations
    round_num_ = 0
    damage_ = 0
    r_winner_ = ""
    r_loser_ = ""
    prev_winner_ = ""
    end_match_ = 0
#// Now, let's run the match
    while True:
    
        if not (end_match_ == 0):
            break
    # end if
        round_num_ += 1
        #// Each wrestler rolls the dice
        roll_["wrestler1"] = rand(1, 6)
        roll_["wrestler2"] = rand(1, 6)
        if howmany_ >= 3:
            roll_["wrestler3"] = rand(1, 6)
        # end if
        if howmany_ == 4:
            roll_["wrestler4"] = rand(1, 6)
        # end if
        #// Determine dice roll winners/losers
        arsort(roll_)
        r_winner_ = key(roll_)
        php_end(roll_)
        r_loser_ = key(roll_)
        reset(roll_)
        #// Here's the logic for calculating winners, losers, and damage dealt out.  It's ugly and could probably be done better.
        #// There are cases for losers within the cases for winners, all within a master switch.
        for case in Switch(r_winner_):
            if case("wrestler1"):
                #// Start case where winner is wrestler1
                if prev_winner_ == "wrestler1":
                    damage_ = wrestler1_["offense"]
                else:
                    damage_ = floor(wrestler1_["offense"] / 2)
                # end if
                for case in Switch(r_loser_):
                    if case("wrestler2"):
                        #// Start case wrestler2 loses to wrestler1
                        def_ = wrestler2_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler2_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler2_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                    if case("wrestler3"):
                        #// Start case wrestler3 loses to wrestler1
                        def_ = wrestler3_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler3_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler3_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                    if case("wrestler4"):
                        #// Start case wrestler4 loses to wrestler1
                        def_ = wrestler4_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler4_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler4_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                # end for
                break
            # end if
            if case("wrestler2"):
                #// Start case where winner is wrestler2
                if prev_winner_ == "wrestler2":
                    damage_ = wrestler2_["offense"]
                else:
                    damage_ = floor(wrestler2_["offense"] / 2)
                # end if
                for case in Switch(r_loser_):
                    if case("wrestler1"):
                        #// Start case wrestler1 loses to wrestler2
                        def_ = wrestler1_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler1_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler1_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                    if case("wrestler3"):
                        #// Start case wrestler3 loses to wrestler2
                        def_ = wrestler3_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler3_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler3_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                    if case("wrestler4"):
                        #// Start case wrestler4 loses to wrestler2
                        def_ = wrestler4_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler4_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler4_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                # end for
                break
            # end if
            if case("wrestler3"):
                #// Start case where winner is wrestler3
                if prev_winner_ == "wrestler3":
                    damage_ = wrestler3_["offense"]
                else:
                    damage_ = floor(wrestler3_["offense"] / 2)
                # end if
                for case in Switch(r_loser_):
                    if case("wrestler1"):
                        #// Start case wrestler1 loses to wrestler3
                        def_ = wrestler1_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler1_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler1_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                    if case("wrestler2"):
                        #// Start case wrestler2 loses to wrestler3
                        def_ = wrestler2_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler2_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler2_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                    if case("wrestler4"):
                        #// Start case wrestler4 loses to wrestler3
                        def_ = wrestler4_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler4_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler4_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                # end for
                break
            # end if
            if case("wrestler4"):
                #// Start case where winner is wrestler4
                if prev_winner_ == "wrestler4":
                    damage_ = wrestler4_["offense"]
                else:
                    damage_ = floor(wrestler4_["offense"] / 2)
                # end if
                for case in Switch(r_loser_):
                    if case("wrestler1"):
                        #// Start case wrestler1 loses to wrestler4
                        def_ = wrestler1_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler1_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler1_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                    if case("wrestler2"):
                        #// Start case wrestler2 loses to wrestler4
                        def_ = wrestler2_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler2_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler2_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                    if case("wrestler3"):
                        #// Start case wrestler3 loses to wrestler4
                        def_ = wrestler3_["defense"]
                        #// Minimum damage shouldn't be less than 1
                        if def_ < damage_:
                            wrestler3_["hitpoints"] -= damage_ - def_
                        else:
                            wrestler3_["hitpoints"] -= 1
                        # end if
                        break
                    # end if
                # end for
                break
            # end if
        # end for
        #// End winner switch
        #// Check for end of match
        if r_loser_ == "wrestler1" and wrestler1_["hitpoints"] <= 0 and rand(1, 6) <= wrestler1_["pin_range"] or r_loser_ == "wrestler2" and wrestler2_["hitpoints"] <= 0 and rand(1, 6) <= wrestler2_["pin_range"] or r_loser_ == "wrestler3" and wrestler3_["hitpoints"] <= 0 and rand(1, 6) <= wrestler3_["pin_range"] or r_loser_ == "wrestler4" and wrestler4_["hitpoints"] <= 0 and rand(1, 6) <= wrestler4_["pin_range"]:
            end_match_ = 1
        # end if
        prev_winner_ = r_winner_
    # end while
    #// end while loop
#// Dynamic page header
if howmany_ == 4:
    title_ = wrestler1_["name"] + " vs. " + wrestler2_["name"] + " vs. " + wrestler3_["name"] + " vs. " + wrestler4_["name"]
elif howmany_ == 3:
    title_ = wrestler1_["name"] + " vs. " + wrestler2_["name"] + " vs. " + wrestler3_["name"]
elif howmany_ == 2:
    title_ = wrestler1_["name"] + " vs. " + wrestler2_["name"]
else:
    title_ = "Match Error"
# end if
#// Prepare for output
for case in Switch(r_winner_):
    if case("wrestler1"):
        #// If wrestler1 won the match
        m_winner_ = wrestler1_["name"]
        for case in Switch(rand(1, 6)):
            if case(1):
                pass
            # end if
            if case(2):
                pass
            # end if
            if case(3):
                m_move_ = wrestler1_["finisher1"]
                break
            # end if
            if case(4):
                pass
            # end if
            if case(5):
                m_move_ = wrestler1_["finisher2"]
                break
            # end if
            if case(6):
                m_move_ = wrestler1_["finisher3"]
                break
            # end if
        # end for
        break
    # end if
    if case("wrestler2"):
        #// If wrestler2 won the match
        m_winner_ = wrestler2_["name"]
        for case in Switch(rand(1, 3)):
            if case(1):
                m_move_ = wrestler2_["finisher1"]
                break
            # end if
            if case(2):
                m_move_ = wrestler2_["finisher2"]
                break
            # end if
            if case(3):
                m_move_ = wrestler2_["finisher3"]
                break
            # end if
        # end for
        break
    # end if
    if case("wrestler3"):
        #// If wrestler3 won the match
        m_winner_ = wrestler3_["name"]
        for case in Switch(rand(1, 3)):
            if case(1):
                m_move_ = wrestler3_["finisher1"]
                break
            # end if
            if case(2):
                m_move_ = wrestler3_["finisher2"]
                break
            # end if
            if case(3):
                m_move_ = wrestler3_["finisher3"]
                break
            # end if
        # end for
        break
    # end if
    if case("wrestler4"):
        #// If wrestler4 won the match
        m_winner_ = wrestler4_["name"]
        for case in Switch(rand(1, 3)):
            if case(1):
                m_move_ = wrestler4_["finisher1"]
                break
            # end if
            if case(2):
                m_move_ = wrestler4_["finisher2"]
                break
            # end if
            if case(3):
                m_move_ = wrestler4_["finisher3"]
                break
            # end if
        # end for
        break
    # end if
# end for
for case in Switch(r_loser_):
    if case("wrestler1"):
        m_loser_ = wrestler1_["name"]
        break
    # end if
    if case("wrestler2"):
        m_loser_ = wrestler2_["name"]
        break
    # end if
    if case("wrestler3"):
        m_loser_ = wrestler3_["name"]
        break
    # end if
    if case("wrestler4"):
        m_loser_ = wrestler4_["name"]
        break
    # end if
# end for
#// Calculate match time
m_mins_ = floor(round_num_ / howmany_)
if round_num_ % 2 == 0:
    secs_ = rand(0, 29)
else:
    secs_ = rand(30, 59)
# end if
m_secs_ = php_str_pad(secs_, 2, "0", STR_PAD_LEFT)
pass

    # Output HTML
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>{title_} (Match Result)</title>
    </head>
    <body>
        <center><h1>{title_}</h1></center>
        <p><h2>Debugging</h2><br><br>
        <p>Rounds: {round_num_}</h2>
        <p>Wrestler 1 rolled {roll_["wrestler1"]}
        <p>Wrestler 2 rolled {roll_["wrestler2"]}
        <p>Wrestler 3 rolled {roll_["wrestler3"]}
        <p>Wrestler 4 rolled {roll_["wrestler4"]}
        <br><br>
        <p>Roll Winner: {r_winner_}
        <p>Roll Loser: {r_loser_}
        <p>{r_winner_} struck for {damage_} damage
        <p>{r_loser_} defended for {def_}<br><br>
        <p>Wrestler 1 has {wrestler1_["hitpoints"]} HP remaining
        <p>Wrestler 2 has {wrestler2_["hitpoints"]} HP remaining
        <p>Wrestler 3 has {wrestler3_["hitpoints"]} HP remaining
        <p>Wrestler 4 has {wrestler4_["hitpoints"]} HP remaining
        <p><center><h3>
        {m_winner_} defeated {m_loser_} with a {m_move_} ({m_mins_}:{m_secs_})
        </h3></center>
        <br><br>
        <a href="index.php">Run another match</a><br><br>
        &Copy; 2023 SlamSim
    </body>
    </html>
    """
    return [html_content.encode('utf-8')]
