import looter as lt
from concurrent import futures

domain = 'https://xkcd.com'

def crawl(url):
    src = lt.get_source(url)
    links = src.cssselect('#comic img')
    lt.save_imgs(links)


if __name__ == '__main__':
    tasklist = list(f'{domain}/{i}' for i in range(1, 1960))
    with futures.ThreadPoolExecutor(50) as executor:
        executor.map(crawl, tasklist)