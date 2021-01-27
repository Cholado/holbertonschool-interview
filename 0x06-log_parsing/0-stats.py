#!/usr/bin/python3
"""
Module - Stats Log Parser
"""

if __name__ == '__main__':

    def printer(size, statusCodes):
        """
        Function - Printer
        Prints file size & status code if needed
        """
        a = sorted(statusCodes.keys())
        print("File size: {:d}".format(size))
        for i in a:
            if statusCodes[i] != 0:
                print("{}: {}".format(i, statusCodes[i]))

    size = 0
    statusCodes = {"200": 0, "301": 0, "400": 0,
                   "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    counter = 0
    try:
        with open(0) as file:
            for line in file:
                counter += 1
                arr = line.split()
                try:
                    size += int(arr[-1])
                except:
                    pass
                try:
                    status = arr[-2]
                    if status in statusCodes:
                        statusCodes[status] += 1
                except:
                    pass
                if counter % 10 == 0:
                    printer(size, statusCodes)
            printer(size, statusCodes)
    except KeyboardInterrupt:
        printer(size, statusCodes)
        raise
