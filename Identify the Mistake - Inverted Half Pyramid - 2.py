n = int(input())

for row_num in range(1,n+1):
    row_output = "" * (row_num - 1)
    seq_num = n - row_num + 1
    while seq_num > 0:
        row_output = row_output + str(seq_num)
        seq_num = seq_num - 1
    print(row_output)
