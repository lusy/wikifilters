import sys
import pandas as pd


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
    df_update = df[['af_id', 'af_hidden', 'af_actions', 'af_hit_count', 'af_public_comments']]
    df_update.to_csv(out_file, sep='\t')
    #print(df[['af_id', 'af_hidden', 'af_actions', 'af_hit_count', 'af_public_comments']])

'''
main
'''
def main():
    #sort_actions('../filter-lists/20181215-en-enabled-and-disabled')
    get_filters_actions('../quarries/quarry-32518-all-filters-sorted-num-hits.csv', '../filter-lists/20190106115600_filters-sorted-by-hits-description')

if __name__ == '__main__':
    status = main()
    sys.exit(status)
