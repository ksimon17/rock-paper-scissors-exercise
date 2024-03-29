# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

Run the rock paper scissors game:

```sh
python game.py
```
## Configure Personal Username
To customize the user's name during run time: 

```sh
PLAYER_NAME="User's Name" python game.py
```

Otherwise, the user's name will default to "Player One"

## Testing

To run automated tests:

```sh
pytest
```
