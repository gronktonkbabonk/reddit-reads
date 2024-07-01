import requests,json,os
from time import gmtime, strftime
from dataclasses import dataclass
from dotenv import load_dotenv

#😫
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
#😫😫😫

###########################
### START PREPROCESSING ###
###########################

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("SECRET")
AUTH_TOKEN =  requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET)

data = {
	"grant_type": os.getenv("GRANT_TYPE"),
	"username": os.getenv("USERNAME"),
	"password": os.getenv("PASSWORD")
}

headers = {"User-Agent": "MyAPI/0.0.1"}
res = requests.post("https://www.reddit.com/api/v1/access_token?limit=500", auth=AUTH_TOKEN, data=data, headers=headers)
TOKEN = res.json()["access_token"]
headers["Authorization"] = f"bearer {TOKEN}"

def apiReq(link, pretty=False):
	raw = requests.get(f"https://oauth.reddit.com/{link}",headers=headers)
	if pretty: 
		return json.dumps(json.loads(raw.content), indent=3) 
	else:
		return raw.json()

hot_posts = apiReq("r/askreddit/hot")

# i hate to interrupt the variable flow but this is necessary
with open("../.datafiles/oldposts.txt", "a+") as f:
	f.seek(0)
	post = hot_posts["data"]["children"][0]["data"]
	
	i = 1
	while post["title"] in f.read():
		f.seek(0)
		if i >= len(hot_posts["data"]["children"]):
		    print("No new unique posts available. Please wait for a while and try again")
		    exit(0)
		post = hot_posts["data"]["children"][i]["data"]
		i += 1

	f.seek(2)
	f.write(f"{strftime('%Y-%m-%d %H:%M:%S', gmtime())} \n {post['title']}\n\n")

comments = apiReq(f"/comments/{post['id']}")[1:]

avg = ("#"*round((len(post["url"])+len(post["title"]))/2))
print()
#^this is dumb
print("[",avg,"]")
print(f"[ Title: {post['title']} ]\n[ Author: {post['author']} ]\n[ Score: {post['score']} ]\n[ URL: {post['url']} ]\n[ Total Comment Count: {post['num_comments']} ]\n[ All primary comments saved to \x1B[4mcomments.txt\x1B[0m ]")


def decodeChars(text):
    try:
        return text.encode().decode('unicode_escape')
    except Exception as e:
        print(f"Error decoding text: {e}")
        return text

with open("../.datafiles/comments.txt", "w+", encoding="utf-8") as f:
	for comment_thread in comments:	
		for comment in comment_thread["data"]["children"]:
			try:
				body = comment["data"]["body"]
				decodedBody = decodeChars(body)
				if (decodedBody != "[deleted]" + decodedBody != "[removed]"):
					f.write(f"{json.dumps(decodedBody, indent=3, ensure_ascii=False)}\n\n")
			except:
				pass
	f.seek(0)


with open("../.datafiles/comments.json", "w") as f:
    json.dump(comments, f, ensure_ascii=False, indent=4)

#############################
##### END PREPROCESSING #####
### START POST PROCESSING ###
#############################
from gtts import gTTS

#this is dumb but it's not worth the if statements
try:
	os.remove("output.mp3")
	os.remove("temp.mp3")
except:
	pass

def voice(audio):
	try:
		gTTS(audio).save("temp.mp3")
		with open("temp.mp3","rb") as temp:
			with open("output.mp3", "ab") as output:
				output.write(temp.read())
		os.remove("temp.mp3")
	except KeyboardInterrupt:
		exit(0)


with open("../.datafiles/comments.txt", "r+") as f:
	commentCount = 0
	commentLensFull = 0
	longestComment = 0
	shortestComment = 99999
	commentsOverNum = 0
	commentsUnder = 0
	commentsOver = []
	for line in f:
		if len(line) > 1: commentLensFull += (len(line)) 
		else: continue

		if len(line) < shortestComment: shortestComment = len(line)
		if len(line) > longestComment: longestComment = len(line)
		commentCount += 1

	commentAvg = round(commentLensFull/commentCount)

	f.seek(0)
	for line in f:
		if len(line) > commentAvg: commentsOverNum += 1
		if len(line) < commentAvg: commentsUnder += 1

	print(f"[ Total Comment Count: {commentCount} ]\n[ Average Length Of Comment: {commentAvg} ]\n[ Shortest Comment Length: {shortestComment} ]\n[ Longest Comment Length: {longestComment} ]\n[ Comments over average length: {commentsOverNum} ]\n[ Comments under average length: {commentsUnder} ]")	
	print("[",avg,"]\n")

	i = 0
	f.seek(0)
	for line in f:
		print(f"Voicing large comments: {i}/{commentsOverNum}", end="\r")
		if len(line) > commentAvg:
			voice(line)
			print(f"Voicing large comments: {i+1}/{commentsOverNum}", end="\r")
			i += 1
		if(i == commentsOverNum):
			print("\nAll large comments voiced.")
			break
