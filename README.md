# Sample Tweeter

This is a twitter-like app using Django, Python, HTML, CSS, Bootstrap and etc!

## Cloning the repositories

You can clone or pull the repository:
```bash
git clone https://github.com/iamsahar/tweetme.git
```

## Developing locally

### Prerequisites

You'll need Python 3:

```bash
# On Linux, via apt:
sudo apt-get update
sudo apt-get install python3-pip

# On Mac, via Homebrew:
brew install python@<python_version>
```
This app uses the default Django database (sqlite3) so you don't need install anything for DB.

### Python environment

In order to keep the development process tidy, you should use a virtual environment when installing application-specific packages. There are multiple ways to set up virtual environments (e.g. using Pipenv), but the example below shows how you can do this using the native tools:

```bash
cd tweetme
python3 -m venv venv
```

To activate and deactivate the virtual environment you just need to run the following commands:

```bash
source venv/bin/activate
deactivate
```

**NOTE**: Never commit your virtual environment to git, as this adds a lot of uneccesary files.
