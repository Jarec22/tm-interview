import json
import pandas as pd

data_list = []

df =  pd.read_json("RC_2021-01-22_2021-01-22.jsonl", lines=True)

json_keys = [
    "all_awardings",
    "associated_award",
    "author_flair_background_color",
    "author_flair_css_class",
    "author_flair_richtext",
    "author_flair_template_id",
    "author_flair_type",
    "author_fullname",
    "author_patreon_flair",
    "author_premium",
    "awarders",
    "collapsed_because_crowd_control",
    "comment_type",
    "created_utc",
    "gildings",
    "is_submitter",
    "link_id",
    "locked",
    "no_follow",
    "parent_id",
    "retrieved_on",
    "send_replies",
    "stickied",
    "subreddit_id",
    "top_awarded_type",
    "total_awards_received",
    "treatment_tags",
    "created",
    "distinguished",
    "author_cakeday"
]

df = df.drop(json_keys, axis=1)
for index, row in df.iterrows():
    data_list.append(
        {"model": "api.comment",
         "pk":row["id"],
         "fields": {
             "author":row["author"],
             "author_flair_text":row["author_flair_text"],
             "author_flair_text_color":row["author_flair_text_color"],
             "body":row["body"],
             "permalink":row["permalink"],
             "score":row["score"],
             "subreddit":row["subreddit"]
         }}
    )


with open('clean.json', 'w') as fp:
    fp.write("[")
    fp.write(",\n".join(json.dumps(entry) for entry in data_list))
    fp.write("]")
