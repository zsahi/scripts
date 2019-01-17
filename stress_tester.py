import urllib3
import time
import  requests
import threading

total_request_count = 100
number_of_threads = 50

http_proxy = ""#"http://127.0.0.1:8080"
https_proxy = ""#"https://127.0.0.1:8080"

timeout = 5
user_agent = 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'

response_ok = 0

url = "http://testphp.vulnweb.com/"
headers = {'User-Agent': user_agent}


class ScanningThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        send_request()

def send_request():
    global  response_ok
    try:
        r = requests.get(url, headers=headers, allow_redirects=True,
                         proxies={"http": http_proxy, "https": https_proxy}, verify=False,
                         timeout=timeout)
    except requests.exceptions.RequestException as e:
        return

    if r.status_code == 200:
        response_ok = response_ok + 1
        pass


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":
    print("Program Started!!!")
    threads = []
    start_time = time.time()
    for i in range(0, number_of_threads):
        threads.append(ScanningThread())

    for i in range(0, number_of_threads):
        threads[i].start()

    request_counter = number_of_threads

    while True:
        active_thread_count = threading.active_count()
        if active_thread_count <= number_of_threads:
            thread = ScanningThread()
            thread.start()
            threads.append(thread)
            request_counter = request_counter + 1
        else:
            time.sleep(1)
            print("==================================================")
            print("Active Threads Count: " + str(active_thread_count))
            print("==================================================")
            print("Requests Sent: ", str(request_counter))
            print("Response Ok: ", str(response_ok))

        if request_counter >= total_request_count:
            break


    for i in range(0, number_of_threads):
        threads[i].join()

    end_time = time.time()

    print("==================================================")
    print("Active Threads Count: " + str(active_thread_count))
    print("==================================================")
    print("Requests Sent: ", str(request_counter))
    print("Response Ok: ", str(response_ok))
    print("Time: ", str(end_time - start_time), " Seconds")
    print("=========== Number of requests completed !!! ===================")
    print("Exiting main thread.")
    exit(0)
