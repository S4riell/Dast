import discord
from discord.ui import Select, View
from discord.ext import commands

# Open token :

token = open("../cred/Dast.txt", "r")


# Intents

intents = discord.Intents.default()
intents.members = True  # Activer l'intention des membres
intents.message_content = True
intents.integrations = True
intents.guilds = True 
intents.guild_messages = True
intents.guild_reactions = True
intents.voice_states = True

if __name__ == "__main__":
    
    client = commands.Bot(command_prefix='#', intents=intents)
    
    @client.tree.command(name="purge_vocaux", description="Purge tout les vocaux !")
    async def purge_voc(interaction:discord.Interaction):
        await interaction.response.send_message("C'est un test")


    @client.tree.command(name="setup", description="Mise en place du bot.")
    async def setup(interaction:discord.Interaction):
        await interaction.response.send_message("Début de la mise en service.")


    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print ("Token : ", token)
        print('------')
        
        await client.tree.sync()
        
        await client.change_presence(activity=discord.CustomActivity(name="Surveille le bureau de Achi..."))
        
client.run(token)