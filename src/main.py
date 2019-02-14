import sys
import pandas as pd
from mw import database


def read_filters(filepath):
    df = pd.read_csv(filepath, sep='\t')
    print(df.columns)
    actions = df['Actions ']
    print (df.head())

def sort_actions(filepath):
    df = pd.read_csv(filepath, sep='\t')
    actions = df['Actions ']
    df_by_actions = df.sort_values(by='Actions ')
    print (df[0:3])


def get_filters_actions(in_file, out_file):
    df = pd.read_csv(in_file, sep=',')
    df_update = df[['af_id', 'af_hidden', 'af_global', 'af_enabled', 'af_deleted', 'af_throttled', 'af_group', 'af_timestamp', 'af_actions', 'af_hit_count', 'af_public_comments']]
    df_update.to_csv(out_file, sep='\t')
    #print(df[['af_id', 'af_hidden', 'af_actions', 'af_hit_count', 'af_public_comments']])


def download_db_table():
    db = database.DB.from_params(
        host="analytics-store.eqiad.wmnet",
        read_default_file="~/.my.cnf",
        user="research",
        db="enwiki"
    )

    users = db.users.query(
        registered_after="20140101000000",
        direction="newer",
        limit=10
    )

for user in users:
print("{user_id}:{user_name} -- {user_editcount} edits".format(**user))


'''
main
'''
def main():
    #sort_actions('../filter-lists/20181215-en-enabled-and-disabled')
    get_filters_actions('../quarries/quarry-32518-all-filters-sorted-num-hits.csv', '../filter-lists/20190106115600_filters-sorted-by-hits')

if __name__ == '__main__':
    status = main()
    sys.exit(status)
