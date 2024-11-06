import json

filepath = "bruecken_alt.json"

with open(filepath, "r") as f:
    bridges = json.load(f)

    i = 0
    for first_word in bridges:
        # if len(bridges[first_word]) < 0: continue
        for second_word in bridges[first_word]:
            if second_word in ["der", "dem", "des"]:
                continue
            if second_word in bridges:
                third_word = bridges[second_word][0]
                i += 1
                print(first_word, second_word, third_word)

    print(f"Found {i} brücken!")