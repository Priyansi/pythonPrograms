def all_dec_sub_seq(arr):
    all_seq = []
    seq = []
    for ind, _ in enumerate(arr[:-1]):
        if arr[ind] > arr[ind+1]:
            seq.append(arr[ind])
        elif len(seq):
            seq.append(arr[ind])
            all_seq.append(seq)
            seq = []
    return all_seq


if __name__ == "__main__":
    arr = [1, 6, 5, 4, 9, 3, 2, 1, 10]
    print(all_dec_sub_seq(arr))
