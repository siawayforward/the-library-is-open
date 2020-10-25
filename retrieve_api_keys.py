#get keys for both API requests

def get_API_keys():
    with open('keys.txt', 'r') as file:
        key_value_pairs = ' '.join(file.readlines()).replace('\n', '')
        nyt_key = key_value_pairs.split('google,')[0].split('nyt,')[1].strip()
        google_key = key_value_pairs.split('google, ')[1].strip()
        file.close()
    return [nyt_key, google_key]