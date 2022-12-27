def generate_affiliation_link(url):
    code = url.split("/dp/")[1].split("/")[0]
    return f"http://www.amazon.com/dp/{code}/?tag=pyb0f-20"
    

if __name__ == "__main__":
    links="""https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art
https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1
https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234
https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X
https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/
"""
    for url in links.splitlines():
        print(generate_affiliation_link(url))