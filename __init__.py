import heroku3
from functools import wraps
from config import HEROKU_API_KEY, HEROKU_APP_NAME


HEMROKU_CLi = heroku3.from_key(HEROKU_API_KEY) if HEROKU_API_KEY else None


def check_heroku(func):
    @wraps(func)
    async def HEMROKU_CLi(client, message):
        heroku_app = None
        if not HEmROKU_CLi:
            await message.reply_text(
                "`•Add HEROKU_API_KEY First If You want To Run This!`",
                parse_mode="markdown",
            )
        elif not HEROKU_APP_NAME:
            await message.reply_text(
                "`Add HEROKU_APP_NAME First If You Want To Run This!`",
                parse_mode="markdown",
            )
        if HEROKU_APP_NAME and HEMROKU_CLi:
            try:
                heroku_app = HEMROKU_CLi.app(HEROKU_APP_NAME)
            except:
                await message.reply_text(
                    message,
                    "`API_KEY and APP_NAME Doesn't Match.!`",
                    parse_mode="markdown",
                )
            if heroku_app:
                await func(client, message, heroku_app)

    return heroku_cli
