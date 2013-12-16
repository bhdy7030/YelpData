
import json


'''
load dataset file to a list of json objects
'''
def load_file(filename):
    data=[]
    with open(filename) as f:
        for line in f:
            data.append(json.loads(line))
    return data

'''
    load all three categories of dataset
'''
def load_all_data(review_file,user_file,business_file):
    return load_file(review_file),load_file(user_file),load_file(business_file)



'''
filter users and business, return the users and business that make/have more than user_threshold/business_threshold reviews.
'''
def data_filter(reviews, user_threshold, business_threshold):

    user_count = {}
    business_count = {}
    for item in reviews:
        user_id = item['user_id']
        b_id = item['business_id']
        if not user_count.__contains__(user_id):
            user_count[user_id] = 1
        else:
            user_count[user_id] += 1
        if not business_count.__contains__(b_id):
            business_count[b_id] = 1
        else:
            business_count[b_id] += 1
    return [k for k, v in user_count.iteritems() if v > user_threshold], [k for k, v in business_count.iteritems() if v > business_threshold]



'''
return filtered users and business
'''
def data_filtered(user_threshold,business_threshold,reviews,users,stores):
    uid,bid= data_filter(reviews,user_threshold,business_threshold)
    if uid and bid:
        filtered_users = [x for x in users if uid.__contains__(x['user_id'])]
        filtered_stores = [x for x in stores if bid.__contains__(x['business_id'])]
        return filtered_users,filtered_stores
    else:
        print "** No user or business found. Please check threshold."
        return [],[]


'''
Write json to file
'''
def write_file(jdata,filename):
    with open(filename,'w') as outfile:
        for d in jdata:
            outfile.write(json.dumps(d)+'\n')
    return 0




def get_review_by_uid(reviews,uid):
    return [x for x in reviews if x['user_id'] == uid]

def get_review_by_bid(reviews,bid):
    return [x for x in reviews if x['business_id'] == bid]



'''

'Pre-process orignal dataset files. (*Only need to run once to produce filtered dataset file.)
'Set filter: user review >10 and business review > 10
'write filtered data to user.json and business.json

reviews, users, stores = load_all_data('Data/yelp_academic_dataset_review.json','Data/yelp_academic_dataset_user.json','Data/yelp_academic_dataset_business.json')
filtered_users, filtered_stores = data_filtered(10,10,reviews, users, stores)
write_file(filtered_users,'Data/user.json')
write_file(filtered_stores,'Data/business.json')

'''

'''
'Load filtered dataset.
'test get review by a given business id or user id
'''
reviews, users, stores = load_all_data('Data/yelp_academic_dataset_review.json','Data/user.json','Data/business.json')
reviews_by_bid= get_review_by_bid(reviews,'Dsvx2LEC8jk9nuGsg1Kqhg')
reviews_by_uid= get_review_by_uid(reviews,'qrdkZvmXPd4Ts20SmUBRQQ')
for x in reviews_by_uid:
    print x







