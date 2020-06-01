def main():
    current_num = 0
    try:
        while True:
            print(f"{current_num}")
            current_num += 1
    except KeyboardInterrupt as kiex:
        print(f"\nWe counted all the way up to: {current_num}")
        raise kiex


try:
    main()
except KeyboardInterrupt as kiex2:
    print("Program finished")