class script(object):
    START_TXT = """Hᴇʟᴏ {},
Mʏ Nᴀᴍᴇ Is <a href='https://t.me/OB_ANYFILTERBOT'>Sᴄᴀʀʟᴇᴛᴛ</a>, I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs, Jᴜsᴛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Eɴᴊᴏʏ 😍"""
    HELP_TXT = """Hᴇʏ {}
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Cᴏᴍᴍᴀɴᴅs."""
    ABOUT_TXT = """✯ Mʏ Nᴀᴍᴇ: Sᴄᴀʀʟᴇᴛᴛ Jᴏʜᴀɴssᴏɴ
✯ Cʀᴇᴀᴛᴏʀ: Oᴡᴅᴠᴇʀ Bᴏᴛ
✯ Lɪʙʀᴀʀʏ: Pʏʀᴏɢʀᴀᴍ
✯ Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3
✯ Dᴀᴛᴀ Bᴀsᴇ: Mᴏɴɢᴏ Dʙ
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: Hᴇʀᴏᴋᴜ
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: ᴠ1.0.1 [ Bᴇᴛᴀ ]"""
    SOURCE_TXT = """<b>Nᴏᴛᴇ:</b>
- Sᴄᴀʀʟᴇᴛᴛ Jᴏʜᴀɴssᴏɴ Is A Cʟᴏɴᴇ Oғ Eᴠᴀ Mᴀʀɪᴀ 
- Sᴏᴜʀᴄᴇ - https://github.com/EvamariaTG/EvaMaria  

<b>Dᴇᴠs:</b>
- <a href=https://t.me/TeamEvamaria>Tᴇᴀᴍ Eᴠᴀ Mᴀʀɪᴀ</a>"""
    MANUELFILTER_TXT = """Hᴇʟᴘ: <b>Fɪʟᴛᴇʀs</b>

- Fɪʟᴛᴇʀ Is Tʜᴇ Fᴜᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ I Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ

<b>Nᴏᴛᴇ:</b>
1. ɪ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs.

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /filter - <code>Aᴅᴅ A Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ</code>
• /filters - <code>Lɪsᴛ Aʟʟ Tʜᴇ Fɪʟᴛᴇʀs Oғ A Cʜᴀᴛ</code>
• /del - <code>Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ</code>
• /delall - <code>Dᴇʟᴇᴛᴇ Tʜᴇ Wʜᴏʟᴇ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ (Cʜᴀᴛ Oᴡɴᴇʀ Oɴʟʏ)</code>"""
    BUTTON_TXT = """Hᴇʟᴘ: <b>Bᴜᴛᴛᴏɴs</b>

- Sᴜᴘᴘᴏʀᴛs Bᴏᴛʜ Uʀʟ Aɴᴅ Aʟᴇʀᴛ Iɴʟɪɴᴇ Bᴜᴛᴛᴏɴs.

<b>Nᴏᴛᴇ:</b>
1. Tᴇʟᴇɢʀᴀᴍ Wɪʟʟ Nᴏᴛ Aʟʟᴏᴡs Yᴏᴜ Tᴏ Sᴇɴᴅ Bᴜᴛᴛᴏɴs Wɪᴛʜᴏᴜᴛ Aɴʏ Cᴏɴᴛᴇɴᴛ, Sᴏ Cᴏɴᴛᴇɴᴛ Is Mᴀɴᴅᴀᴛᴏʀʏ.
2. Sᴜᴘᴘᴏʀᴛs Bᴜᴛᴛᴏɴs Wɪᴛʜ Aɴʏ Tᴇʟᴇɢʀᴀᴍ Mᴇᴅɪᴀ Tʏᴘᴇ.
3. Bᴜᴛᴛᴏɴs Sʜᴏᴜʟᴅ Bᴇ Pʀᴏᴘᴇʀʟʏ Pᴀʀsᴇᴅ Pᴀʀsᴇᴅ As Mᴀʀᴋᴅᴏᴡɴ Fᴏʀᴍᴀᴛ

<b>Uʀʟ Bᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonurl:https://t.me/OB_ANYFILTERBOT)</code>

<b>Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonalert:Tʜɪs Is Aɴ Aʟᴇʀᴛ Mᴇssᴀɢᴇ)</code>"""
    AUTOFILTER_TXT = """Hᴇʟᴘ: <b>Aᴜᴛᴏ Fɪʟᴛᴇʀ</b>

<b>Nᴏᴛᴇ:</b>
1. Mᴀᴋᴇ Mᴇ Tʜᴇ Aᴅᴍɪɴ Oғ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Iғ Iᴛs Pʀɪᴠᴀᴛᴇ.
2. Mᴀᴋᴇ Sᴜʀᴇ Tʜᴀᴛ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Dᴏᴇs Nᴏᴛ Cᴏɴᴛᴀɪɴs Cᴀᴍ Rɪᴘ, Pᴏʀɴ ᴀɴᴅ Fᴀᴋᴇ Fɪʟᴇs.
3. Fᴏʀᴡᴀʀᴅ Tʜᴇ Lᴀsᴛ Mᴇssᴀɢᴇ Tᴏ Mᴇ Wɪᴛʜ Qᴜᴏᴛᴇs.
 I Wɪʟʟ Aᴅᴅ Aʟʟ Tʜᴇ Fɪʟᴇs Iɴ Tʜᴀᴛ Cʜᴀɴɴᴇʟ Tᴏ Mʏ Dʙ."""
    CONNECTION_TXT = """Hᴇʟᴘ: <b>Cᴏɴɴᴇᴄᴛɪᴏɴs</b>

- Usᴇᴅ Tᴏ Cᴏɴɴᴇᴄᴛ Bᴏᴛ Tᴏ Pᴍ Fᴏʀ Mᴀɴᴀɢɪɴɢ Fɪʟᴛᴇʀs 
- Iᴛ Hᴇʟᴘs Tᴏ Aᴠᴏɪᴅ Sᴘᴀᴍᴍɪɴɢ Iɴ Gʀᴏᴜᴘs.

<b>Nᴏᴛᴇ:</b>
1. Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ A Cᴏɴɴᴇᴄᴛɪᴏɴ.
2. Sᴇɴᴅ <code>/connect</code> Fᴏʀ Cᴏɴɴᴇᴄᴛɪɴɢ Mᴇ Tᴏ Uʀ Pᴍ

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /connect  - <code>Cᴏɴɴᴇᴄᴛ A Pᴀʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ Tᴏ Yᴏᴜʀ Pᴍ</code>
• /disconnect  - <code>Dɪsᴄᴏɴɴᴇᴄᴛ Fʀᴏᴍ A Cʜᴀᴛ</code>
• /connections - <code>Lɪsᴛ Aʟʟ Yᴏᴜʀ Cᴏɴɴᴇᴄᴛɪᴏɴs</code>"""
    EXTRAMOD_TXT = """Hᴇʟᴘ: <b>Exᴛʀᴀ Mᴏᴅᴜʟᴇs</b>

<b>Nᴏᴛᴇ:</b>
Tʜᴇsᴇ Aʀᴇ Tʜᴇ Exᴛʀᴀ Fᴜᴛᴜʀᴇs Oғ Mᴇ

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /id - <code>Gᴇᴛ Iᴅ Oғ A Sᴘᴇᴄɪғɪᴇᴅ Usᴇʀ.</code>
• /info  - <code>Gᴇᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴ Aʙᴏᴜᴛ A Usᴇʀ.</code>
• /imdb  - <code>Gᴇᴛ Tʜᴇ Fɪʟᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ Fʀᴏᴍ Iᴍᴅʙ Sᴏᴜʀᴄᴇ.</code>
• /search  - <code>Gᴇᴛ Tʜᴇ Fɪʟᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ Fʀᴏᴍ Vᴀʀɪᴏᴜs Sᴏᴜʀᴄᴇs.</code>"""
    ADMIN_TXT = """Hᴇʟᴘ: <b>Aᴅᴍɪɴ Mᴏᴅs</b>

<b>Nᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋ Fᴏʀ Mʏ Aᴅᴍɪɴs

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /logs - <code>Tᴏ Gᴇᴛ Tʜᴇ Rᴇsᴄᴇɴᴛ Eʀʀᴏʀs</code>
• /stats - <code>Tᴏ Gᴇᴛ Sᴛᴀᴛᴜs Oғ Fɪʟᴇs Iɴ Dʙ.</code>
• /users - <code>Tᴏ Gᴇᴛ Lɪsᴛ Oғ Mʏ Usᴇʀs Aɴᴅ IDs.</code>
• /chats - <code>Tᴏ Gᴇᴛ Lɪsᴛ Oғ Tʜᴇ Mʏ Cʜᴀᴛs Aɴᴅ IDs </code>
• /index  - <code>Tᴏ Aᴅᴅ Fɪʟᴇs Fʀᴏᴍ A Cʜᴀɴɴᴇʟ</code>
• /leave  - <code>Tᴏ Lᴇᴀᴠᴇ Fʀᴏᴍ A Cʜᴀᴛ.</code>
• /disable  -  <code>Dᴏ Dɪsᴀʙʟᴇ A Cʜᴀᴛ.</code>
• /ban  - <code>Tᴏ Bᴀɴ A Usᴇʀ.</code>
• /unban  - <code>Tᴏ Uɴʙᴀɴ A Usᴇʀ.</code>
• /channel - <code>Tᴏ Gᴇᴛ Lɪsᴛ Lɪsᴛ Oғ Tᴏᴛᴀʟ Cᴏɴɴᴇᴄᴛᴇᴅ Cʜᴀɴɴᴇʟs</code>
• /broadcast - <code>Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ A Mᴇssᴀɢᴇ Tᴏ Aʟʟ Mʏ Usᴇʀs</code>"""
    STATUS_TXT = """★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}
"""
