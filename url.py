import webbrowser
VIDEO_URL = 'https://www.youtube.com/watch?v=XeJ2kqfAq4Q'
emotions = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear']

def youtube_url(emotion):
    if emotion==emotions[0]: #ふつう
        webbrowser.open(VIDEO_URL)
    elif emotion==emotions[1]: #幸せ
        webbrowser.open(VIDEO_URL)
    elif emotion==emotions[2]: #驚き
        webbrowser.open(VIDEO_URL)
    elif emotion==emotions[3]: #悲しい
        webbrowser.open(VIDEO_URL)
    elif emotion==emotions[4]: #怒り
        webbrowser.open(VIDEO_URL)
    elif emotion==emotions[5]: #嫌気
        webbrowser.open(VIDEO_URL)
    elif emotion==emotions[6]: #悲しい
        webbrowser.open(VIDEO_URL)
