from crawler import Crawler
from args import get_args
import requests
from datetime import datetime

if __name__ == '__main__':
    args = get_args()
    crawler = Crawler()
    contents = crawler.crawl(args.start_date, args.end_date)
    # TODO: write content to file according to spec
    with open(args.output, "w",encoding = "UTF-8") as f:
    	for date, title, content in contents:
    		title = title.replace('\n',' ').replace('\r','')
    		title = title.replace('\"','\"\"')
    		content = content.replace('\n',' ').replace('\r','')
    		content = content.replace('\"','\"\"')
    		out_str = f'{str(date)}, "{title}","{content}"\n'
    		f.write(out_str)
