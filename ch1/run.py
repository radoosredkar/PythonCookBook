p = (1, 4)
x, y = p
print(x, y)

data = ["ACME", 50, 90.1, (2021, 4, 27)]
name, shares, price, date = data
print(name, date)
name, shares, price, (y, m, d) = data
print(shares, m)

word = "Hello"
a, b, c, d, e = word
print(a, d)
# Throwaway vars
data = ["ACME", 50, 90.1, (2021, 4, 27)]
_, shares, price, date = data


def drop_first_last(*grades):
    first, *middle, last = grades
    print(sum(middle) / len(middle))


drop_first_last(1, 5, 5, 5, 100)
record = ["Dave", "dave@test.com", 6, 5, 1977, "Halcom"]
name, mail, *rest, company = record
print(name, mail, rest, company)

records = [
    ("plus", 1, 2),
    ("minus", 3, 4),
    ("plus", 4, 5),
]


def plus(x, y):
    print("seštevam", x + y)


def minus(x, y):
    print("odštevam", x - y)


for tag, *args in records:
    if tag == "plus":
        plus(*args)
    elif tag == "minus":
        minus(*args)

line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
uname, *fields, homedir, sh = line.split(":")
print(uname, fields, homedir, sh)

items = list(range(13))
head, *tail = items
print(head, tail)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))

from collections import deque

print("Keep latest n items history")


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


with open("/home/rado/sw/python/PythonCookBook/test.txt") as f:
    for line, prevlines in search(f, "Lorem"):
        for pline in prevlines:
            print("HI" * 20)
            print(pline, end="")
            print("ST" * 20)

        print(line, end="")
        print("-" * 20)

print("Find n largest, smallest items in collection")

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares": 50, "price": 543.22},
    {"name": "FB", "shares": 200, "price": 21.09},
    {"name": "HPQ", "shares": 35, "price": 31.75},
    {"name": "YHOO", "shares": 45, "price": 16.35},
    {"name": "ACME", "shares": 75, "price": 115.65},
]

print("cheap", heapq.nsmallest(3, portfolio, key=lambda s: s["price"]))
print("expensive", heapq.nlargest(3, portfolio, key=lambda s: s["price"]))

print(nums)
(heapq.heapify(nums))
print(nums)
print(heapq.heappop(nums))
print(heapq.heappop(nums))

print("Priority Queue")


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


q = PriorityQueue()
q.push(Item("foo"), 1)
q.push(Item("bar"), 5)
q.push(Item("spam"), 4)
q.push(Item("grok"), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print("To make items comparable use touples or they cannot be compared")
print((1, Item("foo")) < (2, Item("test")))
print((1, 1, Item("foo")) < (1, 0, Item("test")))

print("Multidict")
zivila = {
    "pijace": ["pivo", "vino", "voda"],
    "hrana": ["burger", "kruh", "zelje", "klobase"],
}

import pprint

pprint.pprint(zivila)

from collections import defaultdict

zivila = defaultdict(list)
zivila["pijace"].append("pivo")
zivila["pijace"].append("vino")
zivila["pijace"].append("voda")
zivila["hrana"].append("burger")
zivila["hrana"].append("kruh")
zivila["hrana"].append("zelje")
zivila["hrana"].append("klobase")
zivila["hrana"].append("zelje")

pprint.pprint(zivila)


zivila = defaultdict(set)
zivila["pijace"].add("pivo")
zivila["pijace"].add("vino")
zivila["pijace"].add("voda")
zivila["hrana"].add("burger")
zivila["hrana"].add("kruh")
zivila["hrana"].add("zelje")
zivila["hrana"].add("klobase")
zivila["hrana"].add("zelje")

pprint.pprint(zivila)

pairs = [
    ["pijace", "pivo"],
    ["pijace", "vino"],
    ["pijace", "voda"],
    ["hrana", "burger"],
    ["hrana", "kruh"],
    ["hrana", "zelje"],
    ["hrana", "klobase"],
    ["hrana", "zelje"],
]

zivila = defaultdict(list)
for key, value in pairs:
    zivila[key].append(value)

pprint.pprint(zivila)

print("1.7 Keeping dictionary in order")

from collections import OrderedDict
import json

d = OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["spam"] = 3
d["grok"] = 4

for key, value in d.items():
    print(key, value)
print(json.dumps(d))

print("1.8 Calculating wiht dictionaries")
prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.75}
print(min(prices))  # Not ok is searchig min key)
print(min(prices.values()))  # Not ok finds only the smallest value
print(min(zip(prices.values(), prices.keys())))
print(sorted(zip(prices.values(), prices.keys())))

print("1.9. Finding Commonalities in Two Dictionaries")
a = {"x": 1, "y": 2, "z": 3}
b = {"w": 10, "x": 11, "y": 2}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
print("Make a new dict wiht certain keys removed")
c = {key: a[key] for key in a.keys() - {"z", "w"}}
print(c)

print("1.10. Removing Duplicates from a Sequence while Maintaining Order")


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

a = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 1, "y": 2}, {"x": 2, "y": 4}]
print(list(dedupe(a, key=lambda d: (d["x"], d["y"]))))

print("1.11. Naming a Slice")
record = "....................100.......513.25.........."
cost = int(record[20:23]) * float(record[30:36])
print(record)
print(cost)

SHARES = slice(20, 23)
PRICE = slice(30, 36)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
a = slice(5, 50, 2)
print(a.start, a.stop, a.step)
s = "HelloWorld"
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])
print("1.12. Determining the Most Frequently Occurring Items in a Sequence")

