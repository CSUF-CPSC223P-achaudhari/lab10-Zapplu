import threading
import time

inventory = {
"101": ["Notebook Paper", 2],
"102": ["Pencils", 2],
"103": ["Pens", 6],
"104": ["Graph Paper", 1],
"105": ["Paper Clips", 1],
"106": ["Staples", 4],
"107": ["Stapler", 7],
"108": ["3 Ring Binder", 1],
"109": ["Printer Paper", 1],
"110": ["Notepad", 1]
}

def bot_clerk(items):
    cart = []
    lock = threading.Lock()

    fetch_list = [[],[],[]]
    for i, item in enumerate(items):
        fetch_list[i%3].append(item)

    threads = []
    for get in fetch_list:
        thread = threading.Thread(target=bot_fetcher, args=(get, cart, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return cart

def bot_fetcher(items, cart, lock):
    for num in items:
        time.sleep(inventory[num][1])
        name = inventory[num]
        with lock:
            cart.append([num, name[0]])