#!/bin/python2

import multiprocessing
import subprocess
import os

def ping_req( job_q, result_q ):
  #devnull is used for file path
  DEVNULL = open(os.devnull, 'w')
  while True:
    ip = job_q.get()
    #check if ip is null
    if ip is None:break

    try:
        #run command with args, wait to complete
        subrocess.check_call(['ping ','-c 1 ', ip], stdout=DEVNULL)
        result_q.put(ip)
    except:
        pass


if __name__ == '__main__':
  ip_range = 255

  #returns a process
  jobs = multiprocessing.Queue()
  results = multiprocessing.Queue()

  #activity ran in a separate process group = none, target = function, name = process
  pool = [ multiprocessing.Process(target=ping_req, args=(jobs,results))
            for i in range(ip_range) ]

  for p in pool:
      p.start()

  for i in range(1, 255):
      jobs.put('10.11.1.' + str(i))
      print("test")

  for p in pool:
      jobs.put(None)

  for p in pool:
      p.join()

  while not results.empty():
      ip = results.get()
      print(ip)
