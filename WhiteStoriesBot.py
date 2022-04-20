# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 動作中に必要なオブジェクトの生成

num_reac_list = ["1⃣","2⃣","3⃣","4⃣","5⃣","6⃣"]
num_emoji_list = [":one:",":two:",":three:",":four:",":five:",":six:"]
player_info = [["Unknown"]*6,[4]*6,["Normal"]*6,["S"]*6,[[]]*6]
mode_flg = []
msg_list = [] 

#0:board_msg 1:history_msg 2:pre_msg
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    mode_flg.append(False)
    print('ログインしました')
    

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    ch = message.channel
    
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        if bool(message.embeds):
            msg_list.append(message)
        return
    elif ".ws n" == message.content and not mode_flg[0] :
        mode_flg[0] = True
        await message.delete()
        embed = discord.Embed(title = "白物語", description = "百話目の怪談を語り終えたとき、私たちは霊障に見舞われるだろう。\n怪談を面白く「訂正」して、霊障を回避しよう", color=0xffffff)
        for i in range(6):
            embed.add_field(name="Unknown",value="NG Role:" + num_reac_list[i] +"\nHP:4\nStatus:Normal\nS→")
        embeded_msg = await ch.send(embed=embed)
            
        for i in range(6):
            await embeded_msg.add_reaction(num_reac_list[i])
        history_msg = await ch.send("history:\n")
        pre_bot_msg = await ch.send("START!!")
        
        msg_list.append(history_msg)
        msg_list.append(pre_bot_msg)
    elif '.ws d' == message.content and mode_flg[0]:
        if player_info[2][player_info[0].index(message.author.name)] == "Mad":
            await message.delete()
        else:
            delete_msg = msg_list[2]

            emb = msg_list[0].embeds[0]
            num = random.randint(1,6)
            reply = f'{message.author.mention}:' + str(num)
            msg_list[2] = await ch.send(reply)
            await delete_msg.delete()
            player_index = player_info[0].index(message.author.name)
            player_info[4][player_index].append(num)
            if len(player_info[4][player_index]) % 5 == 0:
                player_info[3][player_index] = player_info[3][player_index] + "→" + str(num) + "\n"
            else:
                player_info[3][player_index] = player_info[3][player_index] + "→" + str(num) 
            if player_index == num - 1:
                player_info[1][player_index] -= 1
            if player_info[1][player_index] == 0:
                player_info[2][player_index] = "Mad"
            emb.set_field_at(player_index,name = player_info[0][player_index],value= "NG Role:" + str(num_reac_list[player_index]) +"\nHP:" + str(player_info[1][player_index]) + "\nStatus:" + player_info[2][player_index] + "\n" + player_info[3][player_index])
            await msg_list[0].edit(embed=emb)
            await msg_list[1].edit(content = msg_list[1].content + reply + "→")

            await message.delete()
    elif '.ws r' == message.content and mode_flg[0] :
        await message.delete()
        await msg_list[2].delete()
        await msg_list[1].delete()

        player_info[1] = [4]*6
        player_info[2] = ["Normal"]*6
        player_info[3] = ["S"]*6
        player_info[4] = [[]]*6

    elif '.ws e' == message.content and mode_flg[0] :
        await message.delete()
        await msg_list[2].delete()
        await msg_list[1].delete()

        await msg_list[0].clear_reactions()
        await msg_list[0].delete()

        player_info[0] = ["Unknown"]*6
        player_info[1] = [4]*6
        player_info[2] = ["Normal"]*6
        player_info[3] = ["S"]*6
        player_info[4] = [[]]*6
        mode_flg.clear()
        msg_list.clear() 
        mode_flg.append(False)
    else:
        
        return


#リアクションがついたときの処理
@client.event
async def on_reaction_add(reaction,user):
    msg_reac_added = reaction.message
    embed_on_addedmsg = msg_reac_added.embeds[0]
    if user.bot:
        return
    elif mode_flg[0]:
        
        user_index = num_reac_list.index(str(reaction.emoji))
        player_info[0][user_index] = user.name
        embed_on_addedmsg.set_field_at(user_index, name=user.name,value= "NG Role:" + str(reaction) +"\nHP:4\nStatus:Normal\nS→")
        await msg_reac_added.edit(embed=embed_on_addedmsg)
        await msg_reac_added.remove_reaction(reaction,user)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
