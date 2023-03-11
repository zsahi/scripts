# this give precedence of https over http. & also www.doamin.com over domains.com
# Read input file
with open("input.txt", "r") as f:
    urls = f.readlines()

# Process URLs
processed_urls = []

uniqu_http = []

result_urls = []

urls = [line.strip() for line in urls if line.strip()]

for url in urls:
    url = url.strip()
    if url.startswith("http://"):
        url1 = url.replace("http://","https://")
        if url1 in urls:
            url = url1
    if url not in uniqu_http:
        uniqu_http.append(url)
    
for url in uniqu_http:
    if url.startswith("http://"):
        scheme = "http://"
    else:
        scheme = "https://"
    url1 = url.replace("http://","")
    url2 = url1.replace("https://","")

    if url2.startswith("www."):
        processed_urls.append(url)
    else:
        if  (scheme + "www." + url2) not in processed_urls:
            processed_urls.append(url)

# Write output file
with open("output.txt", "w") as f:
    f.write("\n".join(processed_urls))
