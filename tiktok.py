from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import re
import pyktokOverride as pyk
import concurrent.futures
import asyncio


pyk.specify_browser("chrome")

def init_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def scroll_down(driver, scroll_pause_time=2):
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    i = 200
    while i>0:
        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
        # Wait to load the page
        time.sleep(scroll_pause_time)
            
        # Calculate new scroll height and compare with the last height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            return  # If the scroll height hasn't changed, we've reached the bottom of the page
        last_height = new_height
        
        i-=1

    
# Function to scrape TikTok profile and extract video links with durations
def get_tiktok_videosOLD(profile_url):
    driver = init_driver()
    driver.get(profile_url)
    
    time.sleep(20)
    
    scroll_down(driver)
    video_links = []
    video_elements = driver.find_elements(By.XPATH, '//div[@data-e2e]//a')
    
    for video_element in video_elements:
        video_url = video_element.get_attribute('href')
        if video_url and '/video/' in video_url:
            video_links.append(video_url)
    
    driver.quit()
    return video_links

def get_tiktok_videos(user_name):
    pyk.specify_browser("chrome")
    videos = asyncio.run(pyk.get_video_urls(user_name, ent_type="user", video_ct=500)) # change user name here!
    return videos

def get_duration_from_link(url):
    result = pyk.save_tiktok(url,False, 'video_data.csv', 'chrome')
    print (result)
    return result

    

def get_longest_videos_(profile_url):
    videos = get_tiktok_videos(profile_url)
    
    print(f"{len(videos)} videos were found")
    videos = sorted(videos, key=lambda x: get_duration_from_link(x), reverse=True)
    for i, video in enumerate(videos[:10], 1):
        print(f"{i}. Video URL: {video}")


def get_longest_videos(profile_url, fast, videos_=[]):
    if videos_ == []:
        if fast:
            videos = get_tiktok_videos(profile_url)
        else:
            videos = get_tiktok_videosOLD("https://www.tiktok.com/@" + profile_url)

    else:
        videos = videos_
    print(f"{len(videos)} videos were found")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        duration_futures = {executor.submit(get_duration_from_link, video): video for video in videos}
        
        # collect results and map each video URL to its duration
        video_durations = {}
        for future in concurrent.futures.as_completed(duration_futures):
            video = duration_futures[future]
            try:
                video_durations[video] = future.result()
            except Exception as e:
                print(f"Error retrieving duration for {video}: {e}")
                video_durations[video] = 0  

    # Sort videos by duration in descending order
    sorted_videos = sorted(videos, key=lambda x: video_durations.get(x, 0), reverse=True)

    numToPrint = 50
    for i, video in enumerate(sorted_videos[:numToPrint], 1):
        print(f"{i}. Video URL: {video} - Duration: {video_durations[video]} seconds")
        
        

get_longest_videos(input("Enter TikTok username: "), False, videos_=[])
