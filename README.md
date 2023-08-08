# DealHunter - bot for sniping on OLX.pl!

---

## What is DealHunter?

DealHunter is a sniping tool for OLX.pl (polish craigslist-like site). \
(at least for now) It takes .csv file as an input, and telegram bot API to send notifications.


#### Requirements

- Python
- Chrome version 115 or newer
- Telegram
- Git (for installation)

---

## Installation and use
```commandline
git clone https://github.com/jakubbak-online/OLXBot
pip install -r requirements.txt
cd src
```
Now, update config.py with your Telegram Bot API key, and Telegram user id; then, fill in example_data.csv, or specify other location of csv file.

You can now, in /src/ use ```python3 main.py```, and it continously will go through list of your offers, sending message to user specified in config.

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
- [ ] Normalize I/O of csv's


- [x] ~~Optimize XPATH~~
- [x] (mostly done) ~~Add comments~~
- [x] ~~Test searches~~
- [x] ~~Figure out how to notify user~~
- [x] ~~Figure out system to check, if user was already notified (probably iterate through id's)~~

</details>
