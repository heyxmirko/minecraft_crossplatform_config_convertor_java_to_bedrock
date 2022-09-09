import json

java_menus_config = """  """ #your java-config.yml converted to JSON by https://www.json2yaml.com/


file = json.loads(java_menus_config)

menu_list = "help" #menu name

for button_number in file["menus"][menu_list]["buttons"]:

    command_list = []
    for c in file["menus"][menu_list]["buttons"][button_number]["left-click"]["commands"]:
        command_list.append(c)

    temp_buttons = {
            "text": f'{file["menus"][menu_list]["buttons"][button_number]["display-name"]}',
            "image": f'https://www.digminecraft.com/block_recipes/images/{file["menus"][menu_list]["buttons"][button_number]["material"].lower()}.png',
            "actions": {
            "commands": command_list
            }
    }

    print(str(temp_buttons))
    #copy output into Step2_Python_to_Json.py
