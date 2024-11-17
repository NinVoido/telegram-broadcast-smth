import asyncio
from pyrogram import Client
from dotenv import dotenv_values
import glob
from pathlib import Path

def read_api_vals():
    api_id = -1
    while True:
        try:
            api_id = int(input("Enter your API ID> "))
            break
        except ValueError:
            print("Please only enter the number")

    api_hash = input("Enter your API hash> ")

    return api_id, api_hash


config = dotenv_values(".creds")

api_id = config["API_ID"]
api_hash = config["API_HASH"]

if api_id is None:
    api_id, api_hash = read_api_vals()



templ_list = glob.glob(str(Path("explanations") / Path("*")))
name_list = list(map(lambda x: Path(x).name, templ_list))
tmpl_text = ""

while True:
    tmpl = input(f"Choose the message to broadcast: {', '.join(name_list)}\n> ")

    if tmpl == "exit":
        exit(0)

    if (tmpl_path := (Path("explanations") / Path(tmpl))).exists:
        print("Will broadcast this message:")
        print(open(tmpl_path).read())
        yn = input("Ok? yes/no> ")
        if yn == "yes":
            tmpl_text = open(tmpl_path).read()
            break
        else:
            print("Choose again or type 'exit' to exit")
    else:
        print("Template not found! Choose again or type 'exit' to exit")

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        contacts = await app.get_contacts()
        for contact in contacts:

            print(f"Sending to {contact.first_name} @{contact.username}")
            yn = input("Send? Hit enter to send, input anything else to skip")
            if yn == "":
                await app.send_message(contact.id, tmpl_text)

asyncio.run(main())
