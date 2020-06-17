# 0x11  Python - Network #1 :snake:

> Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991. It's often used as a “scripting language” for web applications. This means that it can automate specific series of tasks, making it more efficient. This project covers network implementations using Python. More complex scripts

At the end of this project, I was able to solve these questions:
  
* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

## Tasks :heavy_check_mark:

0. Script that fetches https://intranet.hbtn.io/status
1. Script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
2. Script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
3. Script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
4. Script that fetches https://intranet.hbtn.io/status
5. Script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
6. Script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
7. Script that takes in a URL, sends a request to the URL and displays the body of the response.
8. Script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
9. Script that takes your Github credentials (username and password) and uses the Github API to display your id
10. Script that takes 2 arguments in order to solve this challenge.
11. Script that takes in 3 strings and sends a search request to the Twitter API (Pending task)

## Results :chart_with_upwards_trend:

| Filename |
| ------ |
| [0-hbtn_status.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/0-hbtn_status.py)|
| [1-hbtn_header.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/1-hbtn_header.py)|
| [2-post_email.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/2-post_email.py)|
| [3-error_code.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/3-error_code.py)|
| [4-hbtn_status.py](hhttps://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/4-hbtn_status.py)|
| [5-hbtn_header.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/5-hbtn_header.py)|
| [6-post_email.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/6-post_email.py)|
| [7-error_code.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/7-error_code.py)|
| [8-json_api.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/8-json_api.py)|
| [9-starwars.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/9-starwars.py)|
| [10-my_github.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/10-my_github.py)|
| [100-github_commits.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/100-github_commits.py)|
| [101-starwars.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/101-starwars.py)|
| [102-starwars.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/102-starwars.py)|
| 103-search_twitter.py - Pending task|


## Additional info :construction:
### Resources

- Python 3.5
- PEP 8 1.7

### Try It On Your Machine :computer:	
```bash
git clone https://github.com/edward0rtiz/holbertonschool-higher_level_programming.git
cd 0x10-python-network_1
./FILENAME.py
```
