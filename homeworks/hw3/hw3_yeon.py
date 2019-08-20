import tweepy
import imp
import csv
import time

twitter = imp.load_source('twit', '/Users/yonni/Desktop/Secret/start_twitter.py')
api = twitter.client

##### ONE DEGREE SEPARATION #####

### Define a function that creates .csv file of all followers' information  	
def get_followers_info(user): 
	with open('Followers_Info.csv', 'w') as f:  ## write .csv file named 'Followers_Info'
		w = csv.DictWriter(f, fieldnames = ("ID", "Screen_Name", "No_Tweets", "No_Followers", "Type"))
		w.writeheader()

		followers_info = {}
		for follower_id in tweepy.Cursor(api.followers_ids, user).items():  
			try:
				wustl_follower = api.get_user(follower_id) ## get each follower's infomation
				followers_info["ID"] = wustl_follower.id ## ID of the follower
				followers_info["Screen_Name"] = wustl_follower.screen_name ## Screen name of the follower
				followers_info["No_Tweets"] = wustl_follower.statuses_count ## the number of tweets that the follower has made
				followers_info["No_Followers"] = wustl_follower.followers_count ## the number of followers of the follower

				if followers_info["No_Followers"] < 100: 
					followers_info["Type"] = "Layman"
				elif followers_info["No_Followers"] > 1000:
					followers_info["Type"] = "Celebrity"
				else: 
					followers_info["Type"] = "Expert" ## classify the follower based on the number of his/her followers
				
				w.writerow(followers_info) ## Save each follower's information to the .csv file
				print(f"Getting information of follower {follower_id}")
			except tweepy.TweepError as e:
				print(e)
				time.sleep(60*15)
				pass 
	f.close()


### Define a function that creates .csv file of all friends' information 
def get_friends_info(user):
	with open('Friends_Info.csv', 'w') as f: ## write .csv file named 'Friends_Info'
		w = csv.DictWriter(f, fieldnames = ("ID", "Screen_Name", "No_Tweets", "No_Followers", "Type"))
		w.writeheader()

		friends_info = {}
		for friend_id in tweepy.Cursor(api.friends_ids, user).items():
			try:
				wustl_friend = api.get_user(friend_id)  ## get each friend(following)'s information 
				friends_info["ID"] = wustl_friend.id  ## ID of the friend
				friends_info["Screen_Name"] = wustl_friend.screen_name  ## Screen name of the friend
				friends_info["No_Tweets"] = wustl_friend.statuses_count  ## the number of tweets that the friend has made
				friends_info["No_Followers"] = wustl_friend.followers_count ## the number of followers of the friend


				if friends_info["No_Followers"] < 100:
					friends_info["Type"] = "Layman"
				elif friends_info["No_Followers"] > 1000:
					friends_info["Type"] = "Celebrity"
				else: 
					friends_info["Type"] = "Expert" ## classify the friend based on the number of his/her followers

				w.writerow(friends_info)
				print(f"Getting information of friend {friend_id}")
			except tweepy.TweepError as e:
				print(e)
				time.sleep(60*15)
				pass 

		f.close()
        	

get_followers_info('WUSTL')
get_friends_info('WUSTL')
