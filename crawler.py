import requests
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='web-site crawler made by V1russ with love')
    parser.add_argument('-u', '--url', type=str, metavar='', required=True, help='website url')
    parser.add_argument('-w', '--wordlist', type=str, metavar='', required=True, help='wordlist location')
    parser.add_argument('-d', '--depth', type=int, default=1, metavar='', required=False, help='depth scan')
    args = parser.parse_args()

    try:
        url = args.url
        a_file = open(args.wordlist, "r")
        list_of_lists = []
        url_list = []
        counter = 1

        if args.depth < 0:
            print("invalid depth, check your numbers.")
        elif args.depth > 9:
            print("The depth number is too big.")

        for line in a_file:
            stripped_line = line.strip()
            list_of_lists.append(stripped_line)
        a_file.close()

        print(f"begging the scanning of {url}")

        for word in list_of_lists:
            r_url = requests.request('GET', f"{url}/{word}")
            status = r_url.status_code
            if status == 200:
                print(r_url.url)
                url_list.append(r_url.url)

            else:
                continue

        while counter != args.depth:
            for word in list_of_lists:
                for url in url_list:
                    r_url = requests.request('GET', f"{url}/{word}")
                    status = r_url.status_code
                    if status == 200:
                        print(r_url.url)
                        url_list.append(r_url.url)
                    else:
                        continue
            counter += 1

    except Exception as e:
        print(f"error\n\t{e}")
