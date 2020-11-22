#!/usr/bin/env python

from __future__ import unicode_literals
import openpyxl
import youtube_dl

START_COL = 'N'
START_ROW = 10


def get_youtube_links(workbook_name, start_row, start_col):
    base_col = openpyxl.utils.column_index_from_string(start_col)
    workbook = openpyxl.load_workbook(workbook_name)
    worksheet = workbook[workbook.sheetnames[0]]
    for row in range(start_row, worksheet.max_row):
        ytb_link = worksheet.cell(column=base_col, row=row).value
        if ytb_link is not None:
            yield ytb_link


links = get_youtube_links('test.xlsx', START_ROW, START_COL)


class SilentLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print(f'downloaded song={d["filename"]}, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': SilentLogger(),
    'progress_hooks': [my_hook],
    'outtmpl': '%(autonumber)02d-%(title)s.%(ext)s',
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(list(links))
