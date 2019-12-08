import time

start_time = time.time()
end_time = time.time()

difference = end_time - start_time

loops = 0
while difference < 1:
    end_time=time.time()
    difference= end_time - start_time
    loops = loops+1

print(difference)
print(loops)


start_time = time.time()
for element in range(loops):
    end_time=time.time()

difference2 = end_time - start_time
print(difference2)

if difference < difference:
    print("Else jest szybsze. For is {}".format(difference))
else:
    print("for jest szybszy. For is {}". format((difference2)))

# print(loops)

