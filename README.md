# Letterboxd-Movie-Runtimes

> Find out exactly how many hours of your life you have spent watching films logged on Letterboxd.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)
![Stars](https://img.shields.io/github/stars/HighnessAtharva/Letterboxd-Movie-Runtimes?style=flat-square)

## Overview

Letterboxd shows your watched films but not the total runtime unless you pay for Pro. This CLI script reads your exported Letterboxd data, looks up each film's runtime from TMDB, and gives you the grand total. It works on your watched list or your watchlist.

## Features

- Computes total runtime across every film you have logged
- Works on both your watched list and your watchlist
- Real-time progress in the terminal as the CSV is processed
- Writes a new CSV with the name and runtime of every film

## Tech Stack

- Python 3
- The Movie Database (TMDB) API

## Getting Started

### Prerequisites

- Python 3 installed
- A free TMDB API key from [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)

### Get your Letterboxd data

Go to [letterboxd.com/settings/data](https://letterboxd.com/settings/data/), open the **Import and Export** tab, and export your data. Unzip it and place `watched.csv` in the same folder as the script.

To run it on your watchlist instead, copy `watchlist.csv` into the script folder and rename it to `watched.csv`.

### Set your API key

```bash
# bash / zsh
export TMDB_KEY="your_api_key"

# Windows CMD
setx TMDB_KEY "your_api_key"

# PowerShell
$env:TMDB_KEY = "your_api_key"
```

### Run it

```bash
python3 letterboxd_runtimes.py
```

A new CSV is generated with two columns, `Name` and `Runtime`, for every film in your account, plus the total printed to the terminal.

## License

MIT.

<!-- social-footer -->
---

<div align="center">

**Atharva Shah** — Python & AI Engineer · Developer Advocate · Technical Writer

[![Website](https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://atharvashah.com)
[![Blog](https://img.shields.io/badge/Blog-FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://blog.atharvashah.com)
[![Twitter](https://img.shields.io/badge/Twitter-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/cultist_dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atharva-shah-tech/)

</div>
