import os



api_id = int(os.environ.get("API_ID"))

api_hash = os.environ.get("API_HASH")

bot_token = os.environ.get("BOT_TOKEN")





OWNER = int(os.environ.get("OWNER", 5850397219))



try:

    ADMINS=[]

    for x in (os.environ.get("ADMINS", "5850397219").split()):

        ADMINS.append(int(x))

except ValueError:

        raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER)

