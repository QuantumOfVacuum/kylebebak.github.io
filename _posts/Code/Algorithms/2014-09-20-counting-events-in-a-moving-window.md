---
layout: post
title: "Counting Events in a Moving Time Window"
categories: code algorithms
tags: [algorithms, discrete-event-simulation]
---

## Detecting Anomalies
Imagine you're writing a program that reads a series of transactions in real time, and raises an alert whenever more than 50 occur in an hour. Or whenever the total value of these transactions exceeds 500 dollars. Full disclosure: I did this for a big client in Mexico that wanted to detect fraudulent transactions in their stores, both for issuing real-time alerts and for reviewing historical data. I'm not sure whether stores in the U.S. worry about this, but in any case this sort of problem gives rise to an interesting programming model called [discrete event simulation](https://en.wikipedia.org/wiki/Discrete_event_simulation).

This post doesn't explain DES &mdash; there are good explanations on the web, for example [this one](http://algs4.cs.princeton.edu/61event/). But here's the gist of it: DES contrasts with __continuous simulation__ by only examining and updating the state of the system when an event occurs. This model is perfectly suited for the counting problem, which is one of the simplest problems DES can address.

## The (Not) Moving Window
Let's say the transactions (henceforth events) of the previous month are in a relational database. As above, we want to flag every instance in which there were more than 50 events in an hour. One approach is to select the count of events and group them by hour, but this is flawed. __Let's say between 10 and 10:30 there are no events, and between 10:30 and 11 there are forty. Between 11 and 11:30 there are forty more, and again there are none between 11:30 and 12.__ The query would flag neither 10-11 nor 11-12 as suspicious, because the number of events in both hours is below the threshold. But the query would fail to notice that between 10:30 and 11:30 there were eighty events, and the threshold was exceeded.

Clearly, we can't group by hour to count events. We need more precision, so we consider the following: for each event, we take its timestamp `T` and select the count of events that fall between `T` and `T + 1h`. This will definitely work, but it requires one query per event. This is infeasible if there are lots of events.

But this inefficient solution leads to an insight. __Namely, we need an hour-long _"window"_ through which we can examine blocks of consecutive events.__ But instead of moving the window forward, event by event, we can stream the events through the window. This allows us to see when the threshold is exceeded, but issues __just one query__ to the database. It turns out a queue is the ideal structure for this "stationary" window.

## Using the Queue
The algorithm is dead simple. We stream the events out of the database and enqueue them in chronological order. As we enqueue each event, we compare it to the event on the front of the queue (the oldest event on the queue). If the difference in their timestamps is more than `1h`, we dequeue the oldest event. We repeat this process until the oldest event on the queue is within `1h` of the newest event of the queue. After this, we just count the events on the queue, __because they all occurred within a span of one hour__. If the count exceeds 50, well, you get the idea. Also, if we want to find hour-long intervals where the count is __below__ 50, we just reverse our inequality. Here's what the code looks like:


~~~py
q = Queue()
flagged_events = list()

for event in events:
  q.enqueue(event) # newest event is on back of queue
  while q.back().time() - q.front().time() > interval:
    q.dequeue()
  if q.length() > threshold:
    flagged_events.append(event)
~~~

## Performance
Any approach to solving this problem will need to look at all the events. To understand the performance of our approach, we consider that the queue is empty at the beginning, and is nearly empty (just one event remains) at the end.

On average then, for every event that goes on the queue, one comes off. So, for an __average iteration__ of the algorithm, we look at __three events__: the new one that goes on the back of the queue, the oldest one at the front of the queue (which usually gets dequeued), and the second oldest one (which usually doesn't get dequeued). We are reading `3N` events and making `2N` comparisons to process `N` events, which means our approach is __linear__ in the number of events.

