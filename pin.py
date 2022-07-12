import requests as re
import shutil

username = input("User name: ")
url = re.get("https://www.pinterest.com/"+username)

headers = {"Host": "www.pinterest.com",
"Cookie": "_pinterest_sess=TWc9PSZ0SlJRb3QrWEhjUUZxUDFYaVQvRHQ3SUkzZTFhSktkcmJyRDdjVjJEUEZBb0gyS2l4SndMTWEyNmw3S1dlRjNVZ2V4R1JyeEJvcE45K2lCVkYwUkVuUFVvcVU4OU9pVExRdFZFaGR0dU56Yz0mMllGamFocjFyU29YUnpZTTJTTFM5YkNrVUlRPQ==;",
"csrftoken":"957a2c797ecb315f149d14983e3d6140;",
'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="100"',
"Sec-Ch-Ua-Platform": "Windows",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9",
"Connection": "close"}



#print(res.text)
#print(url.text)
if 'tBJ dyH iFc sAJ O2T zDA IZT swG' in url.text:
    tag = url.text
    tag=tag.split('span')
    tag=str(tag[1])
    tag=tag.split('@')
    tag = str(tag[1])
    tag=tag.split('/')
    tag = str(tag[0])
    tag=tag.split('<')
    print("Profile's Username:", tag[0])
    print('==========================================================================')
else:
    print("Sorry")

if 'div class="tBJ dyH iFc sAJ O2T zDA IZT mWe"' in url.text:
    follower = url.text
    follower = follower.split('div class="tBJ dyH iFc sAJ O2T zDA IZT mWe')
    follower = str(follower[1])
    follower = follower.split('">')
    follower = str(follower[1])
    follower = follower.split('<')
    print("Profile's follower: ", follower[0])
    print('==========================================================================')
else:
    print("Sorry")

if 'data-test-id="follower-count"' in url.text:
    follow = url.text
    follow = follow.split('follower-count')
    follow = str(follow[1])
    follow = follow.split('tBJ dyH iFc sAJ O2T zDA IZT mWe')
    follow = str(follow[1])
    follow = follow.split('">')
    follow = str(follow[1])
    follow = follow.split('<')
    print("Profile's follower: ", follow[0])
    print('==========================================================================') 
else:
    print("Sorry")
    
if 'h1 class="lH1 dyH iFc mWe R-d O2T tg7' in url.text:
    name = url.text
    name = name.split('FNs zI7 iyn Hsu')
    name = str(name[1])
    name = name.split('style="')
    name = str(name[1])
    name = name.split('>')
    name = str(name[1])
    name = name.split('<')
    print("Profile's Name: ", name[0])
    print('==========================================================================')
else:
    print("Sorry")

if 'img alt="User Avatar" class="hCL kVc L4E MIw"' in url.text:
    dp = url.text
    dp = dp.split('hCL kVc L4E MIw')
    dp = str(dp[1])
    dp = dp.split('src="')
    dp = str(dp[1])
    dp = dp.split('"/')
    print("Profile's DP: ", dp[0])
    print('==========================================================================')
    image_url = dp[0]
    filename = (username+".jpg")

    r = re.get(image_url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True
        img_path = "F:\Semester-8\OWNUX\Task-29 Pinterest"
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
else:
    print("Sorry, this user doesn't have any Profile picture")

