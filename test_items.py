from analyzer import item_analysis


player = {

"item_0": 939,
"item_1": 116,
"item_2": 172,
"item_3": 0,
"item_4": 0,
"item_5": 0

}


item_map = {

"939": "Daedalus",
"116": "Black King Bar",
"172": "Satanic"

}


result = item_analysis(
    player,
    item_map
)


print(result)