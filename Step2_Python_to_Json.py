import json
x = [
    {'text': '§6§l[$] §e§l§nZEPOLLO SKYBLOCK WEBSTORE§8 - §7[CLICK § VISIT]', 'image': 'https://www.digminecraft.com/block_recipes/images/ender_chest.png', 'actions': {'commands': ['console; tell %player_name% §6§l§nWEBSTORE§6§l » §7You can visit our §6webstore §7here: §e§nhttps://store.zepollo.com']}},
    {'text': '§1§l[✪] §9§l§nZEPOLLO SKYBLOCK DISCORD§8 - §7[CLICK § JOIN]', 'image': 'https://www.digminecraft.com/block_recipes/images/beacon.png', 'actions': {'commands': ['console; tell %player_name% §9§l§nDISCORD§9§l » §7You can join our §9discord §7here: §9§nhttps://discord.gg/Q7En8NThTX']}},
    {'text': '§5§l[✰] §d§l§nZEPOLLO SKYBLOCK VOTE§8 - §7[CLICK § VOTE]', 'image': 'https://www.digminecraft.com/block_recipes/images/writable_book.png', 'actions': {'commands': ['player; vote']}},
    {'text': '§e§l[$] §6§l§nZEPOLLO SKYBLOCK BALANCE§8 - §7[VIEW]', 'image': 'https://www.digminecraft.com/block_recipes/images/gold_ingot.png', 'actions': {'commands': ['console; tell %player_name% §6§l§nBALANCE§6§l » §7Current Balance: §6$§e%vault_eco_balance_commas%']}},
    {'text': '§2§l[✔] §a§l§nISLAND CREATION§8 - §7[CLICK § CREATE]', 'image': 'https://www.digminecraft.com/block_recipes/images/grass_block.png', 'actions': {'commands': ['console; tell %player_name% §2§l§oSUCCESS! §7§oYou have successfully created an §a§oisland§7§o!']}},
    {'text': '§4§l[✦] §c§l§nMINES INFORMATION§8 - §7[VIEW]', 'image': 'https://www.digminecraft.com/block_recipes/images/netherite_pickaxe.png', 'actions': {'commands': ['[openguimenu] ZepolloMines']}},
    {'text': '§5§l[✦] §d§l§nENCHANTMENT INFORMATION§8 - §7[VIEW]', 'image': 'https://www.digminecraft.com/block_recipes/images/enchanted_book.png', 'actions': {'commands': ['player; enchanter']}},
    {'text': '§4§l[✘] §c§l§nISLAND CREATION§8 - §7[CLICK § CREATE]', 'image': 'https://www.digminecraft.com/block_recipes/images/oak_door.png', 'actions': {'commands': ['console; tell %player_name% §2§l§oSUCCESS! §7§oYou have successfully created an §a§oisland§7§o!']}},
    {'text': '§4§l[✘] §c§l§nISLAND CREATION§8 - §7[CLICK § CREATE]', 'image': 'https://www.digminecraft.com/block_recipes/images/repeater.png', 'actions': {'commands': ['console; tell %player_name% §2§l§oSUCCESS! §7§oYou have successfully created an §a§oisland§7§o!']}},
    {'text': '§4§l[✘] §c§l§nISLAND ERROR§8 - §7[CLICK § TELEPORT]', 'image': 'https://www.digminecraft.com/block_recipes/images/gold_block.png', 'actions': {'commands': ['player; island go']}},
    {'text': '§4§l[✘] §c§l§nISLAND CREATION§8 - §7[CLICK § CREATE]', 'image': 'https://www.digminecraft.com/block_recipes/images/red_bed.png', 'actions': {'commands': ['console; tell %player_name% §2§l§oSUCCESS! §7§oYou have successfully created an §a§oisland§7§o!']}},
    {'text': '§4§l[✘] §c§l§nISLAND ERROR§8 - §7[CLICK § TELEPORT]', 'image': 'https://www.digminecraft.com/block_recipes/images/diamond.png', 'actions': {'commands': ['player; island go']}},
    {'text': '§4§l[✘] §c§l§nISLAND CREATION§8 - §7[CLICK § CREATE]', 'image': 'https://www.digminecraft.com/block_recipes/images/diamond_block.png', 'actions': {'commands': ['console; tell %player_name% §2§l§oSUCCESS! §7§oYou have successfully created an §a§oisland§7§o!']}},
    {'text': '§4§l[✘] §c§l§nISLAND CREATION§8 - §7[CLICK § CREATE]', 'image': 'https://www.digminecraft.com/block_recipes/images/emerald_block.png', 'actions': {'commands': ['console; tell %player_name% §2§l§oSUCCESS! §7§oYou have successfully created an §a§oisland§7§o!']}},
    {'text': '§4§l[✘] §c§l§nISLAND ERROR§8 - §7[CLICK § TELEPORT]', 'image': 'https://www.digminecraft.com/block_recipes/images/red_sand.png', 'actions': {'commands': ['player; island go']}},
    {'text': '§4§l[✘] §c§l§nISLAND CREATION§8 - §7[CLICK § CREATE]', 'image': 'https://www.digminecraft.com/block_recipes/images/cobblestone.png', 'actions': {'commands': ['console; tell %player_name% §2§l§oSUCCESS! §7§oYou have successfully created an §a§oisland§7§o!']}},
    {'text': '§4§l[✘] §c§l§nISLAND ERROR§8 - §7[CLICK § TELEPORT]', 'image': 'https://www.digminecraft.com/block_recipes/images/gold_nugget.png', 'actions': {'commands': ['player; island go']}},
    {'text': '§3§l[✦] §b§l§nMINIONS INFORMATION§8 - §7[VIEW]', 'image': 'https://www.digminecraft.com/block_recipes/images/dragon_egg.png', 'actions': {'commands': ['player; minions store']}},
    {'text': '§2§l[✔] §a§l§nSKYBLOCK SPAWN§8 - §7[CLICK § TELEPORT]', 'image': 'https://www.digminecraft.com/block_recipes/images/ender_pearl.png', 'actions': {'commands': ['player; spawn']}},
    {'text': '§2§l[✔] §a§l§nSKYBLOCK PAYOUTS§8 - §7[CLICK § VIEW]', 'image': 'https://www.digminecraft.com/block_recipes/images/paper.png', 'actions': {'commands': ['[openguimenu] ZepolloPayouts']}}
]

json = json.dumps(x, ensure_ascii=False).encode('utf8')
print(json.decode())