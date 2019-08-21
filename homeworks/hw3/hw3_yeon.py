import tweepy
import imp
import csv
import time

twitter = imp.load_source('twit', '/Users/yonni/Desktop/Secret/start_twitter.py')
api = twitter.client

##### ONE DEGREE SEPARATION #####

### Define a function that creates .csv file of all followers' information ###
def get_followers_info(user): 

	#### Fetch followers' ids
	list_follower_id=[] 
	try: 
		for follower_id in tweepy.Cursor(api.followers_ids, user).items():
			list_follower_id.append(follower_id)
	except tweepy.TweepError as e:
		print(e)
		time.sleep(60*15)
		pass
	print("Fetched ids of followers.")

	#### Fetch followers' user object
	follower_obj = []
	for follower_id in list_follower_id:
		try: 
			follower_obj.append(api.get_user(follower_id))
			print(f"Fetched user object of follower {follower_id}")
		except tweepy.TweepError as e:
			print(e)
			time.sleep(60*15)
			pass

	#### Save followers' specific information as .csv file 
	with open('Followers_Info.csv', 'w') as f:  ## write .csv file named 'Followers_Info'
		w = csv.DictWriter(f, fieldnames = ("ID", "Screen_Name", "No_Tweets", "No_Followers", "Type"))
		w.writeheader()
	
		followers_info = {}
		err = [] # to check the error occured during the loop
		counter = 0 # to confirm the number of wustl followers successfully saved to the .csv file 
		for i in range(len(follower_obj)): 
			followers_info["ID"] = follower_obj[i].id ## save ID of the i th follower
			followers_info["Screen_Name"] = follower_obj[i].screen_name ## save screen name of the i th follower
			followers_info["No_Tweets"] = follower_obj[i].statuses_count ## save the number of tweets that the i th follower has made
			followers_info["No_Followers"] = follower_obj[i].followers_count ## save the number of followers of the i th follower
			if followers_info["No_Followers"] < 100: 
				followers_info["Type"] = "Layman"
			elif followers_info["No_Followers"] > 1000:
				followers_info["Type"] = "Celebrity"
			else: 
				followers_info["Type"] = "Expert" ## classify the i th follower based on the number of his/her followers
			counter +=1
			w.writerow(followers_info) ## Save the ith follower's information to the .csv file
		print(f"Get information of {counter} followers")
		
		return "Followers_Info.csv" 



### Define a function that creates .csv file of all friends' information ###
def get_friends_info(user):

	#### Fetch friends'(followings') ids
	list_friend_id=[] 
	try: 
		for friend_id in tweepy.Cursor(api.friends_ids, user).items(): 
			list_friend_id.append(friend_id)
	except tweepy.TweepError as e:
		print(e)
		time.sleep(60*15)
		pass
	print("Fetched ids of friends.")

	#### Fetch friends' user object
	friend_obj = []
	for friend_id in list_friend_id:
		try:
			friend_obj.append(api.get_user(friend_id))
			print(f"Fetched user object of friend {friend_id}")
		except tweepy.TweepError as e:
			print(e)
			time.sleep(60*15)
			pass

	#### Save friends' specific information as .csv file 
	with open('Friends_Info.csv', 'w') as f:  ## write .csv file named 'Friends_Info'
		w = csv.DictWriter(f, fieldnames = ("ID", "Screen_Name", "No_Tweets", "No_Followers", "Type"))
		w.writeheader()

		friends_info = {}
		err = [] # to check the error occured during the loop
		counter = 0 # to confirm the number of wustl friends successfully saved to the .csv file 
		for i in range(len(friend_obj)): 
			friends_info["ID"] = friend_obj[i].id ## save ID of the i th friend
			friends_info["Screen_Name"] = friend_obj[i].screen_name ## save screen name of the i th friend
			friends_info["No_Tweets"] = friend_obj[i].statuses_count ## save the number of tweets that the i th friend has made
			friends_info["No_Followers"] = friend_obj[i].followers_count ## save the number of followers of the i th friend
			if friends_info["No_Followers"] < 100: 
				friends_info["Type"] = "Layman"
			elif friends_info["No_Followers"] > 1000:
				friends_info["Type"] = "Celebrity"
			else: 
				friends_info["Type"] = "Expert" ## classify the i th friend based on the number of his/her followers
			counter +=1
			w.writerow(friends_info) ## Save the i th  friend's information to the .csv file
		print(f"Get information of {counter} friends")

		return "Friends_Info.csv" 


### Define a function that finds users with the greatest number of followers or tweets ###
def find_user(file):
	with open(file, 'r') as f:  ## write .csv file named 'Friends_Info'
		r = csv.DictReader(f)
				
		num_followers = []
		name = []
		num_tweets = []
		types = []

		## create lists of variables; values of each row have the same index in every list.  
		for row in r: 
			num_followers.append(int(row["No_Followers"]))
			num_tweets.append(int(row["No_Tweets"]))
			name.append(row["Screen_Name"])
			types.append(row["Type"])
		x = num_followers.index(max(num_followers)) # the index of the highest value(element) in the list of the number of followers
		y = num_tweets.index(max(num_tweets)) # the index of the higest value in the list of the number of tweets 
		
		return f"The greatest number of followers is {x} of {name[x]} and the greatest number of tweets is {y} from {name[y]}."


### Define a function that finds a user with the greatest number of tweets by group ###
def find_user_by_type(file):
	with open(file, 'r') as f:
		r = csv.DictReader(f)

		layman = []
		expert = []
		celeb = []
		for row in r: ## divide into three lists of types 
			if row["Type"] =="Layman":
				layman.append(row)
			elif row["Type"] == "Expert":
				expert.append(row)
			else: 
				celeb.append(row)
		layman_max = max(layman[i]["No_Tweets"] for i in range(len(layman))) ## find the maximum number of tweets in group Layman
		layman_name = [layman[i]["Screen_Name"] for i in range(len(layman)) if layman[i]["No_Tweets"] == layman_max ] ## Laymen's names that have the maximum tweets 
		expert_max = max(expert[i]["No_Tweets"] for i in range(len(expert))) ## find the maximum number of tweets in group Expert
		expert_name = [expert[i]["Screen_Name"] for i in range(len(expert)) if expert[i]["No_Tweets"] == expert_max ] ## Experts' names that have the maximum tweets
		celeb_max = max(celeb[i]["No_Tweets"] for i in range(len(celeb))) ## find the maximum nuber of tweets in group Celebrity
		celeb_name = [celeb[i]["Screen_Name"] for i in range(len(celeb)) if celeb[i]["No_Tweets"] == celeb_max ] ## Celebs' names that have the maximum tweets  
		
		return f"""The greatest number of tweets among Layman is {layman_max} by {' ,'.join(layman_name)}.
The greatest number of tweets among Expert is {expert_max} by {' ,'.join(expert_name)} 
The greatest number of tweets among Celeb is {celeb_max} by {' ,'.join(celeb_name)}."""




##### Two Degree Seperation #####

### Define a function that creates .csv file of information of both Tier-one and Tier-two followers ###
def get_two_followers_info(user):
 
   	#### Fetch ids of all followers 
    total_id_list =[] # will contain ids of Tier-one and Tier-two followers 
    one_id_list = [] # will contain ids of Tier-one followers only
    
    ### ids of Tier-one followers
    try: 
    	for one_id in tweepy.Cursor(api.followers_ids, user).items():
       		one_id_list.append(one_id) 
       		total_id_list.append(one_id)
    except tweepy.TweepError as e:
    	print(e)
    	time.sleep(60*15)
    	pass
    print("Fetched ids of Tier-one followers.")
   
    ### ids of Tier-two followers; append to total_id_list
    for one_id in one_id_list: # for each tier-one follower of the user
        try : 
        	for two_id in tweepy.Cursor(api.followers_ids, one_id).items(): # get id of each tier-two follower of the tier-one follower
        		total_id_list.append(two_id)
        except tweepy.TweepError as e:
            print(e)
            time.sleep(60*15)
            pass
    print("A complete list of Tier-one and Tier-two followers.") 

    #### Fetch user object of all followers in the complete list; includes both tier-one and tier-two
    follower_obj = []
    for follower_id in total_id_list:
    	try:
    		follower_obj.append(api.get_user(follower_id))
    		print(f"Fetched user object of follower {follower_id}")
    	except tweepy.TweepError as e:
    		print(e)
    		time.sleep(60*15)
    		pass

    #### Save specific information of all followers in the complete list as .csv file
    with open('Two_Followers_Info.csv', 'w') as f:  ## write .csv file named 'Two_Followers_Info'
    	w = csv.DictWriter(f, fieldnames = ("ID", "Screen_Name", "No_Tweets", "No_Followers", "Type"))
    	w.writeheader()

    	followers_info = {}
    	counter = 0 # to confirm the number of followers successfully saved to the .csv file
    	for i in range(len(follower_obj)): 
    		followers_info["ID"] = follower_obj[i].id ## save ID of the i th follower
    		followers_info["Screen_Name"] = follower_obj[i].screen_name ## save screen name of the i th follower
    		followers_info["No_Tweets"] = follower_obj[i].statuses_count ## save the number of tweets that the i th follower has made
    		followers_info["No_Followers"] = follower_obj[i].followers_count ## save the number of followers of the i th follower
    		if followers_info["No_Followers"] < 100: 
    			followers_info["Type"] = "Layman"
    		elif followers_info["No_Followers"] > 1000:
    			followers_info["Type"] = "Celebrity"
    		else: 
    			followers_info["Type"] = "Expert" ## classify the i th follower based on the number of his/her followers
    		counter +=1
    		w.writerow(followers_info) ## Save the ith follower's information to the .csv file
    	print(f"Get information of total {counter} followers")

    	return "Two_Followers_Info.csv" 
                

def get_two_friends_info(user):
 
   	#### Fetch ids of all friends

    total_id_list =[] # will contain ids of Tier-one and Tier-two friends
    one_id_list = [] # will contain ids of Tier-one friends only
    
    ### ids of Tier-one friends
    try : 
    	for one_id in tweepy.Cursor(api.followers_ids, user).items():
    		one_id_list.append(one_id) 
    		total_id_list.append(one_id)
    except tweepy.TweepError as e:
    	print(e)
    	time.sleep(60*15)
    	pass
    print("Fetched ids of Tier-one friends.")
   
    ### ids of Tier-two friends; append to total_id_list
    
    for one_id in one_id_list: # for each tier-one friends of the user
        try: 
        	for two_id in tweepy.Cursor(api.followers_ids, one_id).items(): # get id of each tier-two friends of the tier-one friend 
        		total_id_list.append(two_id)
        except tweepy.TweepError as e:
           	print(e)
           	time.sleep(60*15)
           	pass
    print("A complete list of Tier-one and Tier-two friends.") 


    #### Fetch user object of all friends in the complete list; includes both tier-one and tier-two
    friend_obj = []
    for friend_id in total_id_list:
    	try:
    		friend_obj.append(api.get_user(friend_id))
    		print(f"Fetched user object of friend {friend_id}")
    	except tweepy.TweepError as e:
    		print(e)
    		time.sleep(60*15)
    		pass

    #### Save specific information of all friends in the complete list as .csv file
    with open('Two_Friends_Info.csv', 'w') as f:  ## write .csv file named 'Two_Friends_Info'
    	w = csv.DictWriter(f, fieldnames = ("ID", "Screen_Name", "No_Tweets", "No_Followers", "Type"))
    	w.writeheader()

    	friends_info = {}
    	counter = 0 # to confirm the number of friends successfully saved to the .csv file
    	for i in range(len(friend_obj)): 
    		friends_info["ID"] = friend_obj[i].id ## save ID of the i th friend
    		friends_info["Screen_Name"] = friend_obj[i].screen_name ## save screen name of the i th friend
    		friends_info["No_Tweets"] = friend_obj[i].statuses_count ## save the number of tweets that the i th friend has made
    		friends_info["No_Followers"] = friend_obj[i].followers_count ## save the number of friends of the i th friend
    		if friends_info["No_Followers"] < 100: 
    			friends_info["Type"] = "Layman"
    		elif friends_info["No_Followers"] > 1000:
    			friends_info["Type"] = "Celebrity"
    		else: 
    			friends_info["Type"] = "Expert" ## classify the i th follower based on the number of his/her followers
    		counter +=1
    		w.writerow(friends_info) ## Save the ith follower's information to the .csv file
    	print(f"Get information of total {counter} friends")

    	return "Two_Friends_Info.csv" 


#### One Degree of Separation ####


get_followers_info('WUSTL') ### return 'Followers_Info.csv'
get_friends_info('WUSTL') ### return 'Friends_Info.csv'
#find_user('Followers_Info.csv') 
#find_user('Friends_Info.csv')
#find_user_by_type("Friends_Info.csv")


#### Two Degree of Separation ####


get_two_followers_info('WUSTLPolisci') ### return 'Two_Followers_Info.csv'
get_two_friends_info('WUSTLPolisci') ### return 'Two_Friends_Info.csv'
#find_user('Two_Followers_Info.csv') 
#find_user('Two_Friends_Info.csv')


