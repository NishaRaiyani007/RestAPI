def replace(s):
    not_index = s.find('not')
    poor_index = s.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        # Replace the 'not'...'poor' substring with 'good'
        res = s[:not_index] + 'good' + s[poor_index + 4:]
    else:
        res = s

    return res


s = "The weather is not poor today. It's not so poor, actually."

print(replace(s))
