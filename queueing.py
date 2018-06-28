import random
import copy
qa = []
qb = []
solo = []
processed1 = []
processed2 = []
st1 = 4
st2 = 8
t = 6000
buffa = []
buffb = []
buff1 = []
buff2 = []


def avg(list):
    return sum(list) / len(list)


def bufminus(buff, proce):
    if buff != []:

        if buff[0][0] != 0:
            buff[0][0] -= 1
        elif buff[0][0] == 0:
            proce.append(buff[0].pop(1))
            del buff[:]


def bufr(buff, qa, qb):
    if buff == [] and qa != []:
        buff.append(qa.pop(0))
    elif buff == [] and qa == [] and qb != []:
        buff.append(qb.pop(0))


def bufrr(bufa, bufb, qa, qb):
    bufr(bufa, qa, qb)
    bufr(bufb, qb, qa)


def bufs(buffa, buffb, q):
    if buffa == [] and q != []:
        buffa.append(q.pop(0))
    if buffb == [] and q != []:
        buffb.append(q.pop(0))


def addtime(q):
    for x in range(len(q)):
        q[x][1] += 1


def oneq():
    range_arrival_interval = 13
    range_queue_time = 20
    av = range_arrival_interval
    pt = range_queue_time
    for y in range(int(t)):
        # print('bf1', buff1, 'bf2', buff2)
        bufminus(buffa, processed1)
        bufminus(buffb, processed1)
        bufminus(buff1, processed2)
        bufminus(buff2, processed2)
        bufrr(buff1, buff2, qa, qb)
        bufs(buffa, buffb, solo)
        addtime(solo)
        addtime(qa)
        addtime(qb)
        if random.randint(1, av) == 1:
            tmp = random.randint(1, pt)
            solo.append([tmp, 0])
            qa.append([tmp, 0])
        if random.randint(1, av) == 1:
            tmp = random.randint(1, pt)
            solo.append([tmp, 0])
            qb.append([tmp, 0])

    return processed1, processed2


# print(oneq())
print(oneq()[0], '\n', oneq()[1])
print(avg(oneq()[0]), avg(oneq()[1]))
