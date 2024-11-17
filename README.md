# Broadcast messages from your telegram client account

## Rationale

People get hacked all the time - no matter how much you tell them not to send the 2FA codes to anyone, they still manage to do it.
While recovering stolen account is relatively easy, what comes next can only be described as drudgery full of guilt and shame - explaining everyone who received the fishing messages from your
behalf that the person who sent them was actually not you and surprisingly not even a real person.
This script can be used to minimise the time that a victim will spend on explanations.

Also you can broadcast funny messages and wake people up at 3am if you wish.

## Usage

### Set up Telegram API keys

Follow the official tutorial on [https://core.telegram.org/api/obtaining_api_id](), this time don't send anyone the login code, though!
Once you received the values, leave the page open, you will need them in a minute.

### Come up with an explanation



### Get the script up and running

```bash
pip install -r requirements.txt
python tg-broadcast.py
```
