import re        

def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    result_dict={}
    for line in passwd.strip().splitlines():
        user, _, _, _, name, *_ =line.split(':')
        name = re.sub(',+', ' ', name.rstrip(',')) or 'unknown'
        result_dict[user]=name

    return result_dict


test= """
postfix:x:108:112::/var/spool/postfix:/bin/false
ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash
"""

print(get_users(test))