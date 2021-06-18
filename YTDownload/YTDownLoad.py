from pytube import YouTube

def DownloadYouTube(Url,LocalPath):
    # normal
    # 參考網址:
    YouTube(Url).streams.first().download(output_path=LocalPath)
    return 0

def DownloadYouTube2(Url,LocalPath):
    try:
        # 指定畫質
        # 指定畫質會有的問題:  從YouTube下載的高畫質（1080p或更高）影片通常不包含音軌
        # 參考網址:  https://swf.com.tw/?p=1357
        YouTube(Url).streams.filter(type="video", resolution='720p').first().download(output_path=LocalPath)
    except:
        print('下載影片時發生錯誤，請確認網路連線和YouTube網址無誤。')
        return 1
    return 0

def LoopDownload(LocalPath):
    import validators  # 檢查是否有效網址
    # 套件使用參考網址:  https://miguendes.me/how-to-check-if-a-string-is-a-valid-url-in-python

    while True:
        url = input('請輸入網址:').strip()
        if validators.url(url):
            break
        DownloadYouTube2(url, LocalPath)
        token = input('繼續下一筆下載嗎? Y or N').strip().lower()
        if token != 'y':
            break
    return 0
if __name__ == '__main__':
    import os
    file_path = input('請輸入存放目錄:').strip()

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    LoopDownload(file_path)










