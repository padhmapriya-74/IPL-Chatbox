import json
from ip_qn import keyword_identifier
from get_ord import get_ordinal_number
from tabulate import tabulate

def parsing(qn):
    l1, l2, l3, l4, l5, l6,l7 = keyword_identifier(qn)
    print(l4)
    import queue

    from collections import deque

    class Node:
        def __init__(self, name):
            self.name = name
            self.children = []

        def add_child(self, child):
            self.children.append(child)

    def bfs_search(root, target_name):
        if root is None:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.name == target_name:
                return node

            for child in node.children:
                queue.append(child)

        return None

    # Create the tree
    matches = Node("matches")
    csk = Node("csk")
    rcb = Node("rcb")
    lsg = Node("lsg")
    kkr = Node("kkr")
    mi = Node("mi")
    gt = Node("gt")
    dc = Node("dc")
    pbks = Node("pbks")
    rr = Node("rr")
    srh = Node("srh")

    matches.add_child(csk)
    matches.add_child(rcb)
    csk.add_child(lsg)
    csk.add_child(kkr)
    rcb.add_child(mi)
    rcb.add_child(gt)
    lsg.add_child(dc)
    kkr.add_child(pbks)
    mi.add_child(rr)
    gt.add_child(srh)




    # Perform BFS search and return the name of the node if found
    


    #result = None  # Initialize result with a default value
    answers = []

    with open('matches.json') as user_file:
        matches_parsed_json = json.load(user_file)

    sd = {
        "0": ["teams"],
        "2": ["when", "day", "date", "days", "date"],
        "3": ["where", "location", "locations", "venue", "venues", "place", "places", "stadium", "stadiums"],
        "5": ["won", "win", "victorious", "victory", "victor", "winning", "winner", "triumph", "triumphed", "successful"],
        "key": ["ordinal", "order", "position", "sequence", "number", "rank", "index"],
        "4": [["player", "of", "the", "match"], ["man", "of", "the", "match"], ["most", "valuable", "player"], ["game", "changer"]],
        "5c": ["lose", "lost", "losing", "defeat", "defeated", "loser", "fail", "failed"]
    }

    sd1 = {
        "0": ["role", "job", "position", "job", "responsibility", "contribute", "contribution"],
        "1": ["place", "where", "country", "nation", "nationality", "hometown"],
        "3": ["runs", "run", "score", "scored"],
        "4": ["wicket", "wickets"],
        "captain": ["captain", "skipper", "lead", "led", "leader", "leadership", "leading"],
        "coach": ["coach", "coached", "coaching", "mentor"],
        "years": ["years"],
        "players": ["players"]
    }

    def specific_qn(key, val):
        flag = True
        for i in l6:
            for k, v in sd.items():
                if i in v:
                    if i == "stadium":
                        end_stadium_list = [['wankhede', 'stadium'], ['brabourne', 'stadium'], ['maharashtra', 'cricket', 'association', 'stadium'], ['narendra', 'modi', 'stadium']]
                        for j in end_stadium_list:
                            if all(element in l6 for element in j):
                                answers.append(print_all_details(key, val))
                                flag = False
                    if k == "key":
                        k = int(key)
                        match_pos = get_ordinal_number(k)
                        answers.append(match_pos + " match")
                        flag = False
                    if k == "5c":
                        if val[5] != val[0]:
                            answers.append(val[0])
                            flag = False
                        else:
                            answers.append(val[1])
                            flag = False

                    if k == "0":
                        answers.append(val[0])
                        answers.append(val[1])
                        flag = False
                    if flag:
                        if i == "place":
                            for j in range(len(l6)):
                                if flag:
                                    if l6[j] == i and (l6[j - 1] == "take" or l6[j - 1] == "took"):
                                        answers.append(print_all_details(key, val))
                                    else:
                                        answers.append(val[3])
                                        flag = False
                        else:
                            answers.append(val[int(k)])
                            flag = False
                for j in sd["4"]:
                    if all(element in l6 for element in j):
                        answers.append(val[4])
                        flag = False
                    if not flag:
                        break
                if not flag:
                    break
            if not flag:
                break
        return flag

    # Rest of the code...

    def print_all_details(key, value):
        k = int(key)
        match_pos = get_ordinal_number(k)
        return f"The {match_pos} match of IPL 2022 took place between {value[0]} and {value[1]}. It happened on {value[2]} in {value[3]}. {value[5]} won the match. The player of the match was {value[4]}"

    def display_table(data):
        headings = ['Player Name', 'Role', 'Country', 'Matches Played', 'Total Runs', 'Total Wickets']
        rows = []
        for player, details in data.items():
            role = ', '.join(details[0]) if isinstance(details[0], list) else details[0]
            row = [player, role] + details[1:]
            rows.append(row)

        table = tabulate(rows, headers=headings, tablefmt="plain")
        return table

    if l1 != []:
        for key, val in (matches_parsed_json["matches"]).items():
            if val[2] == l1[0]:
                flag = specific_qn(key, val)
                if flag:
                    answers.append(print_all_details(key, val))

    if l2 != []:
        if len(l2) == 1:
            for key, val in (matches_parsed_json["matches"]).items():
                if (val[0]).lower() == l2[0] or (val[1]).lower() == l2[0]:
                    flag = specific_qn(key, val)
            if flag:
                result = bfs_search(matches,l2[0])
                result=result.name
                result_file=result.upper()+".json"
                with open(result_file) as team_file:
                    teams_json = json.load(team_file)
                    for j in l6:
                        for k, v in sd1.items():
                            if j in v:
                                if k == "captain":
                                    answers.append("The Captain is " + teams_json["Captain"])
                                    flag = False
                                if k == "coach":
                                    answers.append("The Coach is " + teams_json["Coach"])
                                    flag = False
                                if k == "years":
                                    if teams_json["Won years"]!=[]:
                                        won_yrs_str=""
                                        comma=","
                                        for i in range(len(teams_json["Won years"])):
                                            if i!=(len(teams_json["Won years"])-1):
                                                won_yrs_str+=str(teams_json["Won years"][i])+comma
                                            else:
                                                won_yrs_str+=str(teams_json["Won years"][i])

                                        answers.append("The team became the title winner in the years " + won_yrs_str)
                                    else:
                                        answers.append("The team hasn't won an IPL tropy till 2022")
                                    flag = False
                                if k == "players":
                                    answers.append("The players of the team are:")
                                    for keys, values in teams_json["Players"].items():
                                        answers.append(keys)
                                    flag = False
                                if k == "3":
                                    zipped_values = list(zip(*[teams_json["Players"][key] for key in teams_json["Players"]]))[3]
                                    answers.append("The total runs scored by the team is " + str(sum(zipped_values)))
                                    flag = False
                                if k == "4":
                                    zipped_values = list(zip(*[teams_json["Players"][key] for key in teams_json["Players"]]))[4]
                                    answers.append("The total wickets taken by the team is " + str(sum(zipped_values)))
                                    flag = False
                                if not flag:
                                    break
                        if not flag:
                            break

                    for i in l6:
                        if i == "matches":
                            for key, val in matches_parsed_json["matches"].items():
                                if (val[0]).lower() == l2[0] or (val[1]).lower() == l2[0]:
                                    answers.append(print_all_details(key, val))
                                    flag = False
                    if flag:
                        answers.append(f"The Captain of the team is " + teams_json["Captain"]+".")
                        answers.append("The Coach is " + teams_json["Coach"]+".")
                        if teams_json["Won years"]!=[]:
                            won_yrs_str=""
                            comma=","
                            for i in range(len(teams_json["Won years"])):
                                if i!=(len(teams_json["Won years"])-1):
                                    won_yrs_str+=str(teams_json["Won years"][i])+comma
                                else:
                                    won_yrs_str+=str(teams_json["Won years"][i])

                            answers.append("The team became the title winner in the years " + won_yrs_str+".")
                        else:
                            answers.append("The team hasn't won an IPL tropy till 2022.")
                        answers.append("The players of the team are:")
                        for keys, values in teams_json["Players"].items():
                            answers.append(keys)
                            answers.append(";")


        if len(l2) == 2:
            for key, val in matches_parsed_json["matches"].items():
                if ((val[0]).lower() == l2[0] and (val[1]).lower() == l2[1]) or ((val[0]).lower() == l2[1] and (val[1]).lower() == l2[0]):
                    flag = specific_qn(key, val)
                    if flag:
                        answers.append(print_all_details(key, val))

    if l3 != []:
        for key, val in matches_parsed_json["matches"].items():
            if (val[3]).lower() == l3[0] or (val[3]).lower() == l3[0]:
                flag = specific_qn(key, val)
                if flag:
                    answers.append(print_all_details(key, val))

    if l4 != []:
        nodes_lst=["csk","rcb","lsg","kkr","mi","gt","dc","pbks","rr","srh"]
        for i in nodes_lst:
            result = bfs_search(matches,i)
            print(result)
            result=result.name
            result_file=result.upper()+".json"
            with open(result_file) as team_file:
                teams_json = json.load(team_file)
                print(teams_json)
                flag = True
                for key, value in teams_json["Players"].items():
                    if key == l4[0]:
                        for j in l6:
                            if j == "team":
                                teamname = i.split(".")
                                answers.append(teamname[0])
                                flag = False
                            else:
                                for k, v in sd1.items():
                                    if j in v:
                                        if k == "captain":
                                            answers.append(teams_json["Captain"])
                                            flag = False
                                        if k == "coach":
                                            answers.append(teams_json["Coach"])
                                            flag = False
                                        if flag:
                                            answers.append(str(value[int(k)]))
                                            flag = False
                                if not flag:
                                    break
                        if flag:
                            teamname = i.split(".")
                            if isinstance(value[0], str):
                                role = value[0]
                            elif len(value[0]) == 2:
                                role = value[0][0] + " and " + value[0][1]
                            answers.append(f"{key} belongs to {teamname[0]}. His role is {role}. He comes from {value[1]}. Having played in a total of {value[2]} matches in IPL 2022, he has secured {value[3]} runs and taken {value[4]} wickets.")
                            flag = False

    if l5 != []:
        for i in range(len(l6)):
            if l6[i] == get_ordinal_number(int(l5[0])):
                if l6[i+1] == "match":
                    for key, val in matches_parsed_json["matches"].items():
                        if key == str(l5[0]):
                            flag = specific_qn(key, val)
                            if flag:
                                answers.append(print_all_details(key, val))

    if l7!=[]:
        for k in range(len(l7)):
            sugg_str=""
            space=" "
            for i in range(len(l7[k])):
                sugg_str+=l7[k][i]+space

            answers.append(f"Did you mean {sugg_str}?")

    if l1 == l2 == l3 == l4 == l5 == []:
        sd2 = {
            "Purple cap Holder": [["purple", "cap"], ["most", "wickets"]],
            "Orange Cap Holder": [["orange", "cap"], ["most", "runs"]],
            "Total Matches": [["total", "matches"], ["many", "matches"]]
        }
        flag = True
        for i in l6:
            if i == "teams":
                teams_list_ff = [['chennai', 'super', 'kings'], ['delhi', 'capitals'], ['gujarat', 'titans'], ['kolkata', 'knight', 'riders'], ['lucknow', 'super', 'giants'], ['mumbai', 'indians'], ['punjab', 'kings'], ['royal', 'challengers', 'bangalore'], ['rajasthan', 'royals'], ['sunrisers', 'hyderabad']]
                for sublist in teams_list_ff:
                    capitalized_words = [word.capitalize() for word in sublist]
                    capitalized_string = ' '.join(capitalized_words)
                    answers.append(capitalized_string)
                    flag = False
            if i == "six" or i == "sixes":
                answers.append(str(matches_parsed_json["Total Sixes"]))
                flag = False
            if i == "four" or i == "fours":
                answers.append(str(matches_parsed_json["Total Fours"]))
                flag = False
            if i == "100" or i == "100s" or i == "hundreds" or i == "centuries" or i == "hundred":
                answers.append(str(matches_parsed_json["Total Centuries"]))
                flag = False
            if i == "50" or i == "50s" or i == "fifties" or i == "fifty":
                answers.append(str(matches_parsed_json["Total Fifties"]))
                flag = False
            if i in ["won", "win", "victorious", "victory", "victor", "winning", "winner", "triumph", "triumphed", "successful", "champion", "trophy"]:
                answers.append(matches_parsed_json["Title winner"])
                flag = False
            for k, v in sd2.items():
                for j in v:
                    if all(element in l6 for element in j):
                        answers.append(matches_parsed_json[k])
                        flag = False
                    if not flag:
                        break
                if not flag:
                    break
            if not flag:
                break

    return answers

print(parsing("Tell me about the match that happened on 26th march"))













              


   



