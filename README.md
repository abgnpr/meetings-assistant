# Meetings assistant

A service that notifies about, and assists in attending, your daily online meetings.

Platform: Linux _(graphical ones)_

![Overview](images/overview.svg)

## Installation

- python (a distribution that supports `tkinter`)

  ```bash
  sudo apt-get install python3-tk
  ```

- scripts

  ```bash
  git clone ---
  cd meetings-assistant
  pip3 install -r requirements.txt
  ```

- service

  ```bash
  ./installer.sh --install
  ```

- check status

  ```bash
  systemctl status meetings-assistant
  ```

## Schedule your meetings

**`data.yaml`**

A dictionary of meetings keyed by meeting time.

```yaml
attendee-name: John Doe

meetings:

	09:00:
		name: Sample meeting 1
		id: 2813176975
		pswd: xxxxxx
		days:
			- Monday
			- Wednesday
			- Friday

	10:30:
		name: Sample meeting 2
		id: 7709185120
		pswd: yyyyyyy
		days: everyday


	# ... and more
```

**Notes**

- Meeting times must be 4 digit representations `HH:MM`.
  Preceding 0s for single digit hours and minutes are necessary.

- Valid values for `days`
  - list<br>
    `- Monday`<br>
    `- Tuesday`<br>
    `...`<br>
    `- Sunday`<br>
  - array
    `[ Monday, Tuesday, ..., Sunday ]`
  - string
    `everyday` or `Everyday`
