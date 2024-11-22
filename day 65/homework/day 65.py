def compare(s1, s2):
    def normalize_string(s):
        # Treat null, NULL, Nil, None as empty strings
        if s in (None, 'NULL', 'Nil', 'None'):
            return ''
        # Convert to uppercase and check for invalid characters
        upper_s = s.upper()
        if any(c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in upper_s):
            return ''
        return upper_s

    def sum_of_values(s):
        return sum(ord(c) for c in s)

    normalized_s1 = normalize_string(s1)
    normalized_s2 = normalize_string(s2)

    return sum_of_values(normalized_s1) == sum_of_values(normalized_s2)
