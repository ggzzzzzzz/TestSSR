#!/usr/bin/python
# coding=UTF-8
from __future__ import unicode_literals
import youtube_dl
import time
import signal
import os

downloaded_bytes=0

def update_progress(data):
    global downloaded_bytes
    if data["status"] == "downloading":
        if "downloaded_bytes" in data:
            downloaded_bytes=float(data["downloaded_bytes"])

def handler(signum, frame):
    print("\nIt is time to check downloaded filesize!")
    raise Exception("end of time")

def download_video(port=8088):
    ydl_opts = {}
    ydl_opts['proxy'] = '127.0.0.1:'+str(port)

    filepre = 'The Scarecrow-lUtnas5ScSE'
    outputfilename='.'.join([str(port),'mp4'])
    ydl_opts['outtmpl']= outputfilename
    filename='.'.join([str(port),'mp4','part'])
    filename1='.'.join([str(port),'f137','mp4','part'])

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.add_progress_hook(update_progress)
        signal.signal(signal.SIGALRM, handler)
        time_out = 30
        signal.alarm(time_out)
        if os.path.isfile(filename):
            print('removing '+filename)
            os.remove(filename)
        if os.path.isfile(filename1):
            print('removing '+filename1)
            os.remove(filename1)
        try:
            ydl.download(['https://www.youtube.com/watch?v=lUtnas5ScSE'])
            signal.alarm(0)
        except Exception as e:
            signal.alarm(0)
            print(e.args)
            print('Stopping youtube_dl process...')
            ydl = None
            if os.path.isfile(filename):
                print('removing '+filename)
                os.remove(filename)
            if os.path.isfile(filename1):
                print('removing '+filename1)
                os.remove(filename1)
    return downloaded_bytes
