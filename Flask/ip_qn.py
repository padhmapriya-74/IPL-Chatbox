import datefinder
import json
from df import find_dates_in_sentence
from ordinal_no import extract_ordinals

def keyword_identifier(qn):

    stadium_list=[[['wankhede', 'stadium'], ['brabourne', 'stadium'],['eden', 'gardens']],[ ['narendra', 'modi', 'stadium']],[['dr.dy', 'patil', 'sports', 'academy'], ['maharashtra', 'cricket', 'assosciation', 'stadium']]]
    teams_list_sf= ['csk','dc','gt','kkr','lsg','mi','pbks','rcb','rr','srh']
    teams_list_ff=[[['chennai', 'super', 'kings'], ['kolkata', 'knight', 'riders'],  ['lucknow', 'super', 'giants'],['royal', 'challengers', 'bangalore']],[['delhi', 'capitals'], ['gujarat', 'titans'],  ['mumbai', 'indians'], ['punjab', 'kings'],  ['rajasthan', 'royals'], ['sunrisers', 'hyderabad']]]
    teams_list_sf1=['csk','kkr','lsg','rcb']
    teams_list_sf2=['dc','gt','mi','pbks','rr','srh']
    word_list = qn.split()
    lowercase_list = [word.lower() for word in word_list]

    ord_num_list=extract_ordinals(qn)

    dates_list = find_dates_in_sentence(qn)
    date_str=''
    f_date_list=[]
    for i in dates_list:
        split_list=i.split("-")
        dd,mm,yyyy=split_list[2],split_list[1],split_list[0]
        h="-"
        date_str=dd + h + mm + h+ yyyy
        f_date_list.append(date_str)


    t_matching_words = [word for word in lowercase_list if word in teams_list_sf]

    suggestion_lst=[]
    for i in range(len(lowercase_list)):
        for j in range(len(teams_list_ff[0])):
            if lowercase_list[i]==teams_list_ff[0][j][0]:
                if len(lowercase_list[i:])>=3:
                    if lowercase_list[i+1]==teams_list_ff[0][j][1] and lowercase_list[i+2]==teams_list_ff[0][j][2]:
                        t_matching_words.append(teams_list_sf1[j])
                    else:
                        suggestion_lst.append(teams_list_ff[0][j])
                else:
                    suggestion_lst.append(teams_list_ff[0][j])

            elif lowercase_list[i]==teams_list_ff[0][j][1] or lowercase_list[i]==teams_list_ff[0][j][2]:
                suggestion_lst.append(teams_list_ff[0][j])

        for j in range(len(teams_list_ff[1])):
            if lowercase_list[i]==teams_list_ff[1][j][0]:
                if len(lowercase_list[i:])>=2:
                    if lowercase_list[i+1]==teams_list_ff[1][j][1]:
                        t_matching_words.append(teams_list_sf2[j])
                    else:
                        suggestion_lst.append(teams_list_ff[1][j])
                else:
                    suggestion_lst.append(teams_list_ff[1][j])

            elif lowercase_list[i]==teams_list_ff[1][j][1]:
                suggestion_lst.append(teams_list_ff[1][j])


    sta_matching_words=[]
    for i in range(len(lowercase_list)):
        for j in range(len(stadium_list[0])):
            if lowercase_list[i]==stadium_list[0][j][0]:
                if len(lowercase_list[i:])>=2:
                    if lowercase_list[i+1]==stadium_list[0][j][1] :
                        sta_matching_words.append(stadium_list[0][j])
                    else:
                        suggestion_lst.append(stadium_list[0][j])
                else:
                    suggestion_lst.append(stadium_list[0][j])

            elif lowercase_list[i]==stadium_list[0][j][1]:
                suggestion_lst.append(stadium_list[0][j])

        for j in range(len(stadium_list[1])):
            if lowercase_list[i]==stadium_list[1][j][0]:
                if len(lowercase_list[i:])>=3:
                    if lowercase_list[i+1]==stadium_list[1][j][1] and lowercase_list[i+2]==stadium_list[0][j][2]:
                        sta_matching_words.append(stadium_list[1][j])
                    else:
                        suggestion_lst.append(stadium_list[1][j])
                else:
                    suggestion_lst.append(stadium_list[1][j])

            elif lowercase_list[i]==stadium_list[1][j][1] or lowercase_list[i]==stadium_list[1][j][2]:
                suggestion_lst.append(stadium_list[1][j])

        for j in range(len(stadium_list[2])):
            if lowercase_list[i]==stadium_list[2][j][0]:
                if len(lowercase_list[i:])>=4:
                    if lowercase_list[i+1]==stadium_list[2][j][1] and lowercase_list[i+2]==stadium_list[2][j][2] and lowercase_list[i+3]==stadium_list[2][j][3]:
                        sta_matching_words.append(stadium_list[2][j])
                    else:
                        suggestion_lst.append(stadium_list[2][j])
                else:
                    suggestion_lst.append(stadium_list[2][j])

            elif lowercase_list[i]==stadium_list[2][j][1] or lowercase_list[i]==stadium_list[2][j][2] or lowercase_list[i]==stadium_list[2][j][3]:
                suggestion_lst.append(stadium_list[2][j])
    stadium_str=''
    for i in sta_matching_words:
        for j in range(len(i)):
            stadium_str=stadium_str+i[j]
            if j!=(len(i)-1):
                stadium_str=stadium_str+" "
        sta_matching_words.remove(i)
        sta_matching_words.append(stadium_str)

    player_name_list=[]
    json_teams_list=['CSK.json','DC.json','GT.json','KKR.json','LSG.json','MI.json','PBKS.json','RCB.json','RR.json']
    for i in json_teams_list:
        with open(i) as team_file:
            teams_json = json.load(team_file)
        for key,value in (teams_json["Players"]).items():
            single_player_l=(key.lower()).split()
            for word in lowercase_list:
                if word in single_player_l:
                    player_name_list.append(key)

    return f_date_list,t_matching_words,sta_matching_words,player_name_list,ord_num_list,lowercase_list,suggestion_lst

print(keyword_identifier("Winner of IPL 22"))