# deal-hunter - bot for sniping on OLX.pl!

---

## What is deal-hunter?

DealHunter is a sniping tool for OLX.pl (polish craigslist-like site). \
(at least for now) It takes .csv file as an input about searches information, and telegram bot API to send notifications.


#### Requirements

- Python
- Chrome ver 115 or newer (alternatively ChromeDriver ver. 114)
- Telegram
- Git (for installation)

---

## Installation and use
```commandline
git clone https://github.com/jakubbak-online/deal-hunter
pip install -r requirements.txt
cd src
```
Now, update config.py with your Telegram Bot API key, and Telegram user id. \
You can use this guide to go through generating Bot API key: [**Link**](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)

Then, fill in example_data.csv, or specify other location of csv file with info about search specifications.

You can now, in /src/ use ```python3 main.py```, and it continuously will go through list of your offers, sending message to user specified in config. 
Or you can run it in PyCharm, or IDE of your choice.

\
It's still an early version, so
**I'd much appreciate if you'd report all bugs you encounter!**
Suggestion are also welcome!

---

## To-Do's

<details>
<summary>High Priority</summary>

- [ ] Write good Readme, and step-by-step setup guide


- [x] ~~Add sorting by condition~~
- [x] ~~Ensure searches work properly~~

</details>


<details>
<summary>Low Priority</summary>

- [ ] Clean up variable names
- [ ] Normalize I/O of csv's, or figure better way to handle input


- [x] ~~Optimize XPATH~~
- [x] (mostly done) ~~Add comments~~
- [x] ~~Test searches~~
- [x] ~~Figure out how to notify user~~
- [x] ~~Figure out system to check, if user was already notified (probably iterate through id's)~~

</details>
