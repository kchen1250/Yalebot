import modules

static_commands = {
    "ping": "Pong!",
    "testing": "Join the Yalebot testing server: https://groupme.com/join_group/49940116/f2x20kxx",
    "add": "Add me to your own group here: https://yalebot.herokuapp.com",

    "sam": "❗❗❗N O 💪 F L E X 💪 Z O N E ❗❗❗",
    "social": "https://docs.google.com/spreadsheets/d/10m_0glWVUncKCxERsNf6uOJhfeYU96mOK0KvgNURIBk/edit?fbclid=IwAR35OaPO6czQxZv26A6DEgEH-Qef0kCSe4nXxl8wcIfDml-BfLx4ksVtp6Y#gid=0",
    "meetup": ("", "https://i.groupme.com/750x1200.jpeg.b0ca5f6e660a4356be2925222e6f8246.large"),
    "test": "https://erikboesen.com/yalepuritytest",
    "dislike": "👎😬👎\n 🦵🦵",
    "shrug": r"¯\_(ツ)_/¯",
    "oh": ("", "https://i.groupme.com/766x750.jpeg.9209520c57e848369444ca498e31f90a.large"),
    "jah": ("", "https://i.groupme.com/766x750.jpeg.3eb07fe422db4b81947b634a1b309d48.large"),
    "bulldog": "Bulldog!  Bulldog!\nBow, wow, wow\nEli Yale\nBulldog!  Bulldog!\nBow, wow, wow\nOur team can never fail\n\nWhen the sons of Eli\nBreak through the line\nThat is the sign we hail\nBulldog!  Bulldog!\nBow, wow, wow\nEli Yale!",
    "popcorn": "https://www.youtube.com/watch?v=9nwOm4AAXwc",
    "yyle": "https://www.youtube.com/watch?v=SsZDxL-YMYc",
    "discord": "If you must: https://discord.gg/5EScef4",
    "bang": ("", "https://i.groupme.com/720x1440.png.c76127a21867451093edd11bbb09d75d.large"),
    "chike": ("", "https://i.groupme.com/1021x1400.jpeg.70192657c76745ab809357d0512d4951.large"),
    "pressed": ("", "https://i.groupme.com/540x719.jpeg.2229bdb9f15247a7a112ac0be95e065a.large"),
    "flex": "👮🏽🚨🚔 PULL OVER 👮🏽🚨🚔\n\n😤Put your hands behind your back😤\n\n🗣I'm taking you into custody🗣\n\n📝And registering you as a📝\n\n🔥😩FLEX OFFENDER😩🔥",
    "ohno": ("", "https://i.groupme.com/1280x720.jpeg.f7c11a529a3b4a7195f71fa6be5ebfef.large"),
    "defuse": ("", "https://i.groupme.com/500x500.jpeg.26cbc006bcbf47048ade8a896b1e3d5a.large"),
    "cah": "Cards Against Humanity was recently removed from Yalebot and the game can now be run through Bot Against Humanity, a new separate bot which can be added at https://botagainsthumanitygroupme.herokuapp.com."
}

commands = {
    "about": modules.About(),
    "countdown": modules.Countdown(),
    "verify": modules.Verify(),
    "yalenews": modules.YaleNews(),
    "record": modules.Record(),
    "groups": modules.Groups(),
    "weather": modules.Weather(),

    "conversationstarter": modules.ConversationStarter(),
    "funfact": modules.FunFact(),
    "lyrics": modules.Lyrics(),
    "nasa": modules.NASA(),
    "sad": modules.Sad(),
    "xkcd": modules.XKCD(),
    "elizabeth": modules.Elizabeth(),
    "dania": modules.Dania(),
    "jake": modules.Jake(),
    "carlos": modules.Carlos(),
    "crista": modules.Crista(),
    "maria": modules.Maria(),
    "annie": modules.Annie(),
    "chat": modules.Chat(),
    "shakespeare": modules.Shakespeare(),
    "eightball": modules.EightBall(),
    "analytics": modules.Analytics(),
    "youtube": modules.YouTube(),
    "pick": modules.Pick(),
    "chose": modules.Chose(),
    "meme": modules.Meme(),
    "love": modules.Love(),
    "price": modules.Price(),
    "minion": modules.Minion(),
    "house": modules.House(),
    "location": modules.Location(),
    "twitter": modules.Twitter(),
    "tea": modules.Tea(),
    "amber": modules.Amber(),
    "uwu": modules.UWU(),
    "quote": modules.Quote(),
    "dog": modules.Dog(),
    "funny": modules.Funny(),
    "kelbo": modules.Kelbo(),
    "boink": modules.Boink(),
    "conversationstarter": modules.ConversationStarter(),
    "funfact": modules.FunFact(),
    "ship": modules.Ship(),
    "hema": modules.Hema(),
    "victor": modules.Victor(),
    "truman": modules.Truman(),
    "nato": modules.NATO(),
    "tiya": modules.Tiya(),
    "crist": modules.Crist(),
    "power": modules.Power(),
    "colleges": modules.Colleges(),
    "tictactoe": modules.TicTacToe(),
    "zalgo": modules.Zalgo(),
    "flip": modules.Flip(),
    "mccarthy": modules.McCarthy(),
    "circle": modules.Circle(),
    "jpeg": modules.JPEG(),
    "deepfry": modules.DeepFry(),
    "anna": modules.Anna(),
    "damn": modules.Damn(),
    "handshake": modules.Handshake(),
    "dining": modules.Dining(),
    "building": modules.Building(),
    "course": modules.Course(),
    "iam": modules.IAm(),
    "people": modules.People(),
    "compliment": modules.Compliment(),
    "poem": modules.Poem(),
    "lmgtfy": modules.LMGTFY(),
    "randomcollege": modules.RandomCollege(),
    "morse": modules.Morse(),
    "shield": modules.Shield(),
    "organizations": modules.Organizations(),
    "roomnumber": modules.RoomNumber(),
    "smol": modules.Smol(),
    "laundry": modules.Laundry(),
    "admit": modules.Admit(),
    "anagram": modules.Anagram(),
}
commands["courses"] = commands["course"]
system_commands = {
    "welcome": modules.Welcome(),
    "mourn": modules.Mourn(),
    "introduce": modules.Introduce(),
}
