class script(object):
    START_TXT = """<b>HELLO {},
MY NAME IS <a href=https://t.me/{}>{}</a>, I PROVIDE SERIES. JUST ADD ME TO YOUR GROUP AND ENJOY!π
OR JUST PM THE SERIES NAME</b>

<B><U>NOTE</U></B>
Messages will disappear after 30 Minutes
"""
    START_grp_TXT = """
    Hai..,
I can provide movies in group as well as the personal. ADD me to your group as admin or just send movie name to me personally
    
    
    """
    START_gp_TXT = """π·π΄π»πΎ {}  ππ»ππ»ββοΈ
I can provide movies/ series, just send movie name to me or you can add me to your group
I delete all messgaes in groups for restrict group from coppyrights issues ( 5min default delete time)
"""
    HELP_TXT = """π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    ABOUT_TXT = """<b>β οΈ MY NAME: {}</b>
<b>β£οΈ OWNED BY:</b> <a href=https://t.me/JiC54_SERIES_Bot>Click Here!</a>
<b>β£οΈ LANGUAGE:</b> πΏπππ·πΎπ½ πΉ
<b>β£οΈ DATABASE:</b> πΌπΎπ½πΆπΎ
<b>β£οΈ BOT SERVER:</b> π·π΄ππΎπΊπ
<b>β£οΈ π±OT VERSION:</b> <code>12.2.1</code>"""
    SOURCE_TXT = """<b>JiC54 CHANNELS:</b> 
    
<a href=https://t.me/+H_6j47erCp44YjY0>Movies and Series 2022</a>
<a href=https://t.me/+uQBJ5JaaLpgyMWI0>House of Movies</a>
<a href=https://t.me/+EHBqUrMHnglmZWY8>Dax songs</a>
<a href=https://t.me/+8eC2YwzHZtUwZDg0>DC Series</a>
<a href=https://t.me/+GvVfP9p-YAsyMTY0>Marvel Movies</a>
<a href=https://t.me/+6QrMOpOVtKAxOGQ0>African Movies</a>
<a href=https://t.me/+LhZuWiqE21NiYzY0>WWE wrestling</a>

<b>JiC54 GROUPS:</b>
<a href=https://t.me/+dFGzJDTQWow2ZGY8>Request Movies</a>
<a href=https://t.me/+bCTNQn4-5TtkZmZk>Request Series</a>
<a href=https://t.me/+gTYFpj1ZBIIxZTQ0>Request Dax Songs</a>
<b>JiC54 BOTS:</b>
<a href=http://t.me/JiC54_MOVIES_Bot>Movies Bot</a>
<a href=http://t.me/JiC54SeriesBot>Series Bot</a>
<a href=http://t.me/filestolinks1_bot>File to Links Bot</a>"""
    MANUELFILTER_TXT = """<b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and this bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>"""

    BUTTON_TXT = """<b>Buttons</b>
- <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allow you to send buttons without any content, so content is mandatory.
2. <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/JiC54_MOVIES_Bot)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> the admin of your channel if it's private.
2. make sure that your channel does not contains CAMRips, porn and fake files.
3. Forward the last message to <a href=https://t.me/JiC54_MOVIES_Bot>me</a> with quotes.
 I'll add all the files in that channel to my database."""
    
    
    BATCHMODE1_TXT = """<b>FILE STORE</b>
  With this feature a user generates special sharable links of files.

<b><u>How to generate links? π</u></b>
1. For a single file use <code>/link command as reply to file</code>
2. For creating batch files , use <code>/batch <starting message link> <ending message link></code>
Example: <code>/batch https://t.me/JiC54_dax/10 https://t.me/JiC54_dax/20</code>

<b><u>NOTE</u></b>
1. Works in both Private and Public channel
 β€ Make the bot admin in private channel
 β€ Admin Privilege not required for public channel
2. Only videos, audios and documents are supported for now."""
    
    
    CONNECTION_TXT = """<b>CONNECTIONS</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>COMMANDS & USAGE</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>
β’ /settings - <code>customise your group's settings</code>

<b><u>NOTE</u></b>
1. Only admins can add a connection.
2. Send <code>/connect</code> to connect <a href=https://t.me/JiC54_MOVIES_Bot>me</a> to ur PM"""
    EXTRAMOD_TXT = """<b>EXTRA MODULES</b>

These are the extra features of <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 MOVIES Bot</a>

<b>COMMANDS & USAGE</b>
β’ /id  - get id of a specified user.
β’ /info  - get information about a user.
β’ /imdb  - get the film information from IMDb source.
β’ /search  - get the film information from various sources."""
    ADMIN_TXT = """<b>Admin mods</b>

This module only works for my admins

<b>Commands and Usage:</b>
β’ <code>/logs</code> - to get the rescent errors
β’ <code>/stats</code> - to get status of files in db.
β’ <code>/delete</code> - to delete a specific file from db.
β’ <code>/users</code> - to get list of my users and ids.
β’ <code>/chats</code> - to get list of the my chats and ids.
β’ <code>/leave</code>  - to leave from a chat.
β’ <code>/disable</code>  -  do disable a chat.
β’ <code>/ban</code>  - to ban a user.
β’ <code>/unban</code>  - to unban a user.
β’ <code>/channel</code> - to get list of total connected channels.
β’ <code>/broadcast</code> - to broadcast a message to all users.
"""
    STATUS_TXT = """<b>β TOTAL USERS:</b> <code>{}</code>
<b>β TOTAL CHATS:</b> <code>{}</code>
<b>β TOTAL FILES:</b> <code>{}</code>
<b>β USED RAM:</b> <code>{}</code> 
<b>β FREE RAM:</b> <code>{}</code>
<b>β TOTAL RAM:</b> <code>512MB</code>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
(@JiC54SeriesBot)
"""
    LOG_TEXT_P = """#NewUser
User ID = {}(<code>{}</code>)
Username = <code>{}</code>
(@JiC54SeriesBot)
"""
    MAIL_ID_TXT = """
    <b>Currently you are using this mail for heroku account</b>\n
ID - <code>{}</code>
"""