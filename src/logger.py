import json

def update_log(user, value, message):
    log = get_log()
    log_entry = {
        'value': value,
        'message': message
    }
    if not user in log:
        log[user] = []
    log[user].append(log_entry)
    write_log(log)


def get_log():
    with open('log.json') as f:
        return json.load(f)


def write_log(log):
    with open('log.json', "w") as f:
        return f.write(json.dumps(log))
