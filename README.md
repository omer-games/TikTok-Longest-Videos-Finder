# TikTok Longest Videos Finder

TikTok Longest Videos Finder is a Python program that retrieves videos from a specified TikTok user and lists them sorted by duration, helping you quickly find the longest videos on a profile. The program uses a customized version of the `pyktok` library and other Python libraries to scrape and analyze TikTok content.

## Features

- Retrieves up to 500 videos from a TikTok user.
- Supports both fast API-based retrieval and full Selenium-based scraping.
- Sorts videos by duration and displays the top videos.
- Uses multithreading for faster duration analysis.

## Credit for Libraries

This project is built using a modified version of the `pyktok` library:

```
BSD 3-Clause License

Copyright (c) 2022, Deen Freelon
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## How it Works

The program can retrieve videos in two ways:

1. **Fast mode:** Uses the overridden `pyktok` library to quickly retrieve up to 500 videos from the specified TikTok user.
2. **Full scraping mode:** Uses Selenium to scroll through a TikTok profile and extract video links, useful for more complete data collection.

After retrieving the videos, the program calculates the duration of each video and sorts them in descending order.

## How to Use

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/omer-games/TikTok-Longest-Videos-Finder.git
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Program:**
    ```bash
    python longest_videos.py
    ```

4. **Follow the Prompt:**
    - Enter the TikTok username of the profile you want to analyze.
    - The program will display the top 50 longest videos with their durations.

## Dependencies

- Python 3.x
- `selenium`
- `webdriver-manager`
- `requests`
- `pyktok` (custom overridden version)
- `concurrent.futures`
- `asyncio`

You can install the dependencies using:
```bash
pip install selenium webdriver-manager requests pyktok
```

## Developer

Omer-Games

## Note

- This project uses a customized version of `pyktok` to work specifically for this application.
- Video durations are retrieved programmatically and may vary slightly from TikTok's displayed duration.

## License

The original `pyktok` library used in this project is licensed under the BSD 3-Clause License (see above). The modifications and project code are by Omer-Games.
