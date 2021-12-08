#1/usr/bin/env python3

# with open("test.txt", 'r') as f:
with open("input.txt", 'r') as f:
    outputs = [x.replace('\n', '').split('|')[1].split(' ')[1:] for x in f.readlines()]

seg_count = [6,2,5,5,4,5,6,3,7,6]
easy_segs = [1, 4, 7, 8]

easy_count = 0
easy_seg_count = [seg_count[x] for x in easy_segs]
for i in outputs:
    for j in i:
        if(len(j) in easy_seg_count):
            easy_count += 1

print("1, 4, 7, 8 appearance times: {}".format(easy_count))