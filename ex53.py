def resum(lst):
    return min(lst), max(lst), sum(lst) / len(lst)

def main():
    nums = [4, 6, 2, 8, 10]
    print("Mínim, Màxim, Mitjana:", resum(nums))

if __name__ == "__main__":
    main()